import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# --- PATH & ARTIFACT LOADING ---
# Path ke model dan artefak preprocessing
MODEL_DIR = "model/"

# --- UI CONFIGURATION ---
st.set_page_config(
    page_title="Prediksi Status Kelulusan Mahasiswa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fungsi untuk memuat artefak dengan caching untuk performa
@st.cache_resource
def load_artifacts():
    """
    Memuat model dan artefak preprocessing yang disimpan.
    Menggunakan st.cache_resource agar tidak perlu memuat ulang setiap kali ada interaksi.
    """
    try:
        model = joblib.load(os.path.join(MODEL_DIR, 'model_status_mahasiswa.pkl'))
        scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))
        target_encoder = joblib.load(os.path.join(MODEL_DIR, 'target_encoder.pkl'))
        features = joblib.load(os.path.join(MODEL_DIR, 'selected_features.pkl'))
        return model, scaler, target_encoder, features
    except FileNotFoundError:
        return None, None, None, None

model, scaler, target_encoder, features = load_artifacts()


# --- SIDEBAR FOR USER INPUT ---
st.sidebar.header("Masukkan Data Mahasiswa")

def user_input_features():
    """
    Membuat widget di sidebar untuk input pengguna.
    """
    # Berdasarkan fitur yang dipilih dari notebook
    age_at_enrollment = st.sidebar.number_input('Usia saat Pendaftaran (Age at enrollment)', min_value=17, max_value=70, value=20)
    admission_grade = st.sidebar.slider('Nilai Pendaftaran (Admission grade)', 95.0, 190.0, 125.0)
    previous_qualification_grade = st.sidebar.slider('Nilai Kualifikasi Sebelumnya (Previous qualification grade)', 95.0, 190.0, 130.0)

    curricular_units_1st_sem_approved = st.sidebar.slider('SKS Lulus Semester 1 (Curricular units 1st sem approved)', 0, 26, 5)
    curricular_units_1st_sem_grade = st.sidebar.slider('Nilai Semester 1 (Curricular units 1st sem grade)', 0.0, 20.0, 12.0)
    curricular_units_1st_sem_enrolled = st.sidebar.slider('SKS Ditempuh Semester 1 (Curricular units 1st sem enrolled)', 0, 26, 6)

    curricular_units_2nd_sem_approved = st.sidebar.slider('SKS Lulus Semester 2 (Curricular units 2nd sem approved)', 0, 20, 5)
    curricular_units_2nd_sem_grade = st.sidebar.slider('Nilai Semester 2 (Curricular units 2nd sem grade)', 0.0, 20.0, 12.0)
    curricular_units_2nd_sem_enrolled = st.sidebar.slider('SKS Ditempuh Semester 2 (Curricular units 2nd sem enrolled)', 0, 23, 6)

    tuition_fees_up_to_date = st.sidebar.selectbox('Uang Kuliah Lunas (Tuition fees up to date)', ('Ya', 'Tidak'))
    scholarship_holder = st.sidebar.selectbox('Penerima Beasiswa (Scholarship holder)', ('Ya', 'Tidak'))
    debtor = st.sidebar.selectbox('Memiliki Hutang (Debtor)', ('Tidak', 'Ya'))
    gender = st.sidebar.selectbox('Jenis Kelamin (Gender)', ('Perempuan', 'Laki-laki'))
    displaced = st.sidebar.selectbox('Mahasiswa Pindahan (Displaced)', ('Ya', 'Tidak'))

    # Application_mode adalah numerik, jadi kita gunakan number_input
    application_mode = st.sidebar.number_input('Mode Pendaftaran (Application mode)', min_value=1, max_value=57, value=17)


    # Mapping input ke nilai numerik
    data = {
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Tuition_fees_up_to_date': 1 if tuition_fees_up_to_date == 'Ya' else 0,
        'Scholarship_holder': 1 if scholarship_holder == 'Ya' else 0,
        'Age_at_enrollment': age_at_enrollment,
        'Debtor': 1 if debtor == 'Ya' else 0,
        'Gender': 0 if gender == 'Perempuan' else 1, # Berdasarkan notebook: 0 -> Perempuan, 1 -> Laki-laki
        'Application_mode': application_mode,
        'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
        'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
        'Admission_grade': admission_grade,
        'Displaced': 1 if displaced == 'Ya' else 0,
        'Previous_qualification_grade': previous_qualification_grade
    }

    # Urutkan fitur sesuai dengan yang digunakan saat training
    features_df = pd.DataFrame(data, index=[0])
    return features_df[features] # Pastikan urutan kolom sesuai

# --- MAIN PANEL ---
st.title("🎓 Aplikasi Prediksi Status Kelulusan Mahasiswa")
st.write(
    "Aplikasi ini menggunakan model *Machine Learning* untuk memprediksi status kelulusan "
    "seorang mahasiswa (Lulus, Dropout, atau Masih Terdaftar) berdasarkan data akademik dan demografis mereka."
)
st.write("---")

# Cek apakah artefak berhasil dimuat
if model is None:
    st.error(
        "**Error:** File model atau artefak tidak ditemukan. "
        "Pastikan Anda telah menjalankan notebook `notebook.ipynb` untuk menghasilkan file-file yang diperlukan di dalam direktori `model/`."
    )
else:
    # Tampilkan input pengguna dalam bentuk tabel
    input_df = user_input_features()

    st.subheader("Data Mahasiswa yang Dimasukkan:")
    st.dataframe(input_df.style.highlight_max(axis=1))

    # Tombol untuk prediksi
    if st.button('🔮 Prediksi Status', use_container_width=True):
        # Preprocessing input
        input_scaled = scaler.transform(input_df)

        # Lakukan prediksi
        prediction_proba = model.predict_proba(input_scaled)
        prediction = model.predict(input_scaled)

        # Tampilkan hasil
        st.subheader("Hasil Prediksi")
        
        # Decode label prediksi
        status_prediksi = target_encoder.inverse_transform(prediction)[0]
        
        # Tampilkan status dengan gaya
        if status_prediksi == 'Graduate':
            st.success(f"**Prediksi Status:** Lulus (Graduate)")
        elif status_prediksi == 'Dropout':
            st.error(f"**Prediksi Status:** Dropout")
        else:
            st.info(f"**Prediksi Status:** Masih Terdaftar (Enrolled)")

        # Buat dataframe untuk probabilitas
        proba_df = pd.DataFrame(
            prediction_proba,
            columns=target_encoder.classes_,
            index=['Probabilitas']
        )
        st.write("Probabilitas untuk setiap kelas:")
        st.dataframe(proba_df.style.format("{:.2%}").highlight_max(axis=1, color='lightgreen'))

        # Visualisasikan probabilitas
        st.subheader("Visualisasi Probabilitas Prediksi")
        
        # Buat chart
        chart_data = proba_df.T.reset_index()
        chart_data.columns = ['Status', 'Probabilitas']
        
        import altair as alt
        chart = alt.Chart(chart_data).mark_bar().encode(
            x=alt.X('Probabilitas:Q', axis=alt.Axis(format='%')),
            y=alt.Y('Status:N', sort='-x'),
            color=alt.Color('Status:N', legend=None),
            tooltip=['Status', 'Probabilitas']
        ).properties(
            height=200
        )
        st.altair_chart(chart, use_container_width=True)

        st.info(
            "**Interpretasi:** Model memprediksi status mahasiswa dengan probabilitas tertinggi. "
            "Visualisasi di atas menunjukkan tingkat kepercayaan model untuk setiap kemungkinan status."
        )

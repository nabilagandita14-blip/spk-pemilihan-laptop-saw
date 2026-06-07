import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import *
from saw import *

# CONFIG HALAMAN


st.set_page_config(
    page_title="SPK Pemilihan Laptop",
    page_icon="💻",
    layout="wide"
)

# CUSTOM CSS

st.markdown("""
<style>

.stApp{
    background-color:#FFF8FC;
}

section[data-testid="stSidebar"]{
    background-color:#F6DCE7;
}

h1{
    color:#9A4D7A !important;
}

h2,h3{
    color:#B25C8A !important;
}

div[data-testid="metric-container"]{
    background:white;
    border:1px solid #F0D6E2;
    border-radius:15px;
    padding:15px;
}

.stButton > button{
    background:#D96C9D;
    color:white;
    border-radius:10px;
    border:none;
}

.stButton > button:hover{
    background:#C45A8A;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# DATABASE
# =========================

create_table()

# =========================
# HEADER
# =========================

st.title("💻 SPK Pemilihan Laptop Terbaik")
st.subheader("Metode Simple Additive Weighting (SAW)")

# =========================
# SIDEBAR
# =========================

st.sidebar.markdown("## 💻 Menu Sistem")

menu = st.sidebar.selectbox(
    "",
    [
        "📊 Dashboard",
        "➕ Tambah Laptop",
        "📋 Data Laptop",
        "🏆 Hasil SAW",
        "ℹ️ Tentang"
    ]
)

# =========================
# DASHBOARD
# =========================

if menu == "📊 Dashboard":

    st.header("📊 Dashboard Sistem")

    data = get_all_laptop()
    total_laptop = len(data)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💻 Total Laptop",
            total_laptop
        )

    with col2:
        st.metric(
            "⚙️Metode",
            "SAW"
        )

    with col3:
        st.metric(
            "📈 Status",
            "Aktif"
        )

    st.markdown("---")

    st.markdown("""
 🎓 Selamat Datang
Sistem Pendukung Keputusan Pemilihan Laptop Terbaik menggunakan metode **Simple Additive Weighting (SAW)**.
Metode ini membantu mahasiswa menentukan laptop terbaik berdasarkan:
- Harga
- RAM
- SSD
- Processor
- Merek
""")

# =========================
# TAMBAH LAPTOP
# =========================

elif menu == "➕ Tambah Laptop":

    st.header("➕ Tambah Data Laptop")

    nama = st.text_input("Nama Laptop")

    harga = st.number_input(
        "Harga",
        min_value=1.0
    )

    ram = st.number_input(
        "RAM (GB)",
        min_value=1.0
    )

    ssd = st.number_input(
        "SSD (GB)",
        min_value=1.0
    )

    processor = st.number_input(
        "Skor Processor",
        min_value=1.0
    )

    merek = st.number_input(
        "Skor Merek (1-5)",
        min_value=1.0,
        max_value=5.0
    )

    if st.button("💾 Simpan Data"):

        tambah_laptop(
            nama,
            harga,
            ram,
            ssd,
            processor,
            merek
        )

        st.success("✅ Data laptop berhasil disimpan.")

# =========================
# DATA LAPTOP
# =========================

elif menu == "📋 Data Laptop":

    st.header("📋 Data Laptop")

    data = get_all_laptop()

    if len(data) > 0:

        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Nama Laptop",
                "Harga",
                "RAM",
                "SSD",
                "Processor",
                "Merek"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("Belum ada data laptop.")

# =========================
# HASIL SAW
# =========================

elif menu == "🏆 Hasil SAW":

    st.header("🏆 Hasil Perankingan SAW")

    data = get_all_laptop()

    if len(data) > 0:

        df = pd.DataFrame(
            data,
            columns=[
                "id",
                "nama",
                "harga",
                "ram",
                "ssd",
                "processor",
                "merek"
            ]
        )

        hasil = hitung_saw(df)

        hasil["Ranking"] = range(
            1,
            len(hasil) + 1
        )

        st.dataframe(
            hasil[
                ["Ranking", "nama", "nilai"]
            ],
            use_container_width=True
        )

        st.success(
            f"🥇 Laptop Terbaik: {hasil.iloc[0]['nama']}"
        )

        fig, ax = plt.subplots(
            figsize=(8,4)
        )

        ax.bar(
            hasil["nama"],
            hasil["nilai"]
        )

        ax.set_title(
            "Ranking Laptop Berdasarkan SAW"
        )

        ax.set_ylabel(
            "Nilai Preferensi"
        )

        plt.xticks(rotation=30)

        st.pyplot(fig)

    else:
        st.warning("Belum ada data laptop.")

# =========================
# TENTANG
# =========================

elif menu == "ℹ️ Tentang":

    st.header("ℹ️ Tentang Sistem")

    st.write("""
Sistem Pendukung Keputusan (SPK) Pemilihan Laptop Terbaik dibuat untuk membantu mahasiswa menentukan laptop yang paling sesuai berdasarkan beberapa kriteria.

Metode yang digunakan adalah **Simple Additive Weighting (SAW)** yang melakukan normalisasi data dan menghitung nilai preferensi setiap alternatif.
""")

    st.write("""
### Kriteria Penilaian

- Harga
- RAM
- SSD
- Processor
- Merek
""")

    st.info("""
📚 Mata Kuliah: Cloud Computing

🎓 Proyek UAS

💻 Metode: Simple Additive Weighting (SAW)
""")
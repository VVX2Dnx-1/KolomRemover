import streamlit as st
import pandas as pd

def main():
    # Atur judul dan deskripsi aplikasi
    st.title("Aplikasi Penampil Kolom Data")
    st.write("Unggah file CSV atau Excel Anda untuk melihat dan memilih kolom data yang ingin ditampilkan.")

    # Buat komponen untuk mengunggah file
    uploaded_file = st.file_uploader("Pilih file CSV atau Excel", type=['csv', 'xlsx'])

    # Periksa apakah ada file yang diunggah
    if uploaded_file is not None:
        try:
            # Baca file yang diunggah menjadi DataFrame pandas
            # Coba baca sebagai CSV terlebih dahulu
            try:
                df = pd.read_csv(uploaded_file)
            except Exception as e:
                # Jika gagal, coba baca sebagai Excel
                df = pd.read_excel(uploaded_file)

            st.success("File berhasil diunggah dan dibaca!")

            # Dapatkan semua nama kolom dari DataFrame
            column_names = df.columns.tolist()

            # Tampilkan pilihan kolom menggunakan checkbox
            st.write("### Pilih Kolom untuk Ditampilkan")
            selected_columns = [col for col in column_names if st.checkbox(col, key=col)]

            # Tampilkan data dari kolom yang dipilih
            if selected_columns:
                st.write(f"### Menampilkan Data untuk Kolom: **{', '.join(selected_columns)}**")
                st.write("Berikut adalah seluruh data dari kolom yang Anda pilih:")
                # Tampilkan seluruh data dari kolom yang dipilih
                st.dataframe(df[selected_columns])

        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses file: {e}")

if __name__ == "__main__":
    main()
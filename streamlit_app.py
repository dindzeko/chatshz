import streamlit as st

# Inisialisasi session state jika belum ada
if 'show_description' not in st.session_state:
    st.session_state.show_description = False

# Fungsi untuk toggle state
def toggle_description():
    st.session_state.show_description = not st.session_state.show_description

# Menentukan teks tombol berdasarkan state
button_text = "▼ Klik untuk membuka penjelasan" if not st.session_state.show_description else "▲ Klik untuk kembali ke judul"

# Widget tombol dengan teks dinamis
st.button(button_text, on_click=toggle_description)

# Menampilkan deskripsi berdasarkan state
if st.session_state.show_description:
    st.write("""
    **Deskripsi:**  
    Ini adalah deskripsi yang muncul ketika tombol diklik.  
    Klik tombol lagi untuk menyembunyikan deskripsi ini.
    """)
else:
    st.write("**Judul Utama**")

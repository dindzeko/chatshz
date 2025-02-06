import streamlit as st

# Inisialisasi session state jika belum ada
if 'show_description' not in st.session_state:
    st.session_state.show_description = False

# Fungsi untuk toggle state
def toggle_description():
    st.session_state.show_description = not st.session_state.show_description

# Widget tombol
st.button("Klik untuk melihat deskripsi", on_click=toggle_description)

# Menampilkan deskripsi berdasarkan state
if st.session_state.show_description:
    st.write("""
    **Deskripsi:**  
    Ini adalah deskripsi yang muncul ketika tombol diklik.  
    Klik tombol lagi untuk menyembunyikan deskripsi ini.
    """)

import streamlit as st

# Impor fungsi dari file lain
from page.depresiasi import depresiasi
from page.sample import sample
from page.fuzzysearch import fuzzysearch
from page.querybuilder import querybuilder

# Fungsi untuk menambahkan CSS ke aplikasi Streamlit
def add_css(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Animasi CSS untuk transisi halaman
css_animation = """
<style>
/* Animasi fade-in */
.fade-in {
    animation: fadeIn 0.5s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* Gaya untuk sidebar */
.sidebar .sidebar-content {
    transition: margin-left 0.3s ease-in-out;
}
</style>
"""
# Tambahkan CSS ke aplikasi
add_css(css_animation)

# Halaman utama
def main_page():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("Main Page")
    st.write("Welcome")
    st.markdown('</div>', unsafe_allow_html=True)

# Navigasi
page_names_to_funcs = {
    "Main Page": main_page,
    "Depresiasi": depresiasi,
    "Sample": sample,
    "Fuzzy Searching": fuzzysearch,
    "Query Builder": querybuilder,
}

# Sidebar untuk memilih halaman
selected_page = st.sidebar.selectbox("Pilih halaman", page_names_to_funcs.keys())

# Panggil fungsi halaman yang dipilih
page_names_to_funcs[selected_page]()

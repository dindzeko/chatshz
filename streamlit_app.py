import streamlit as st

# Fungsi untuk menambahkan CSS ke aplikasi Streamlit
def add_css(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Animasi CSS untuk transisi halaman
css_styling = """
<style>
/* Header Profesional */
header {
    background-color: #2C3E50 !important;
    color: white !important;
    padding: 1rem;
    text-align: center;
    font-size: 1.5rem;
    font-weight: bold;
}
header::after {
    content: "Streamlining Your Auditing Process";
    display: block;
    font-size: 0.8rem;
    font-weight: normal;
    margin-top: 0.5rem;
}

/* Sidebar Modern */
.sidebar .sidebar-content {
    background-color: #34495E !important;
    color: white !important;
}
.sidebar .st-bd {
    color: white !important;
}
.sidebar .st-cq {
    background-color: #2C3E50 !important;
    border-radius: 0.5rem;
    transition: all 0.3s ease;
}
.sidebar .st-cq:hover {
    background-color: #1ABC9C !important;
    transform: scale(1.05);
}

/* Main Content Styling */
main {
    background-color: #ECF0F1 !important;
    padding: 1rem;
    border-radius: 0.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Tombol Modern */
button {
    background-color: #1ABC9C !important;
    color: white !important;
    border: none !important;
    border-radius: 0.5rem !important;
    padding: 0.5rem 1rem !important;
    transition: all 0.3s ease !important;
}
button:hover {
    background-color: #16A085 !important;
    transform: scale(1.05);
}

/* Animasi Fade-In */
.fade-in {
    animation: fadeIn 0.5s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
</style>
"""

# Tambahkan CSS ke aplikasi
add_css(css_styling)

# Tambahkan Font Awesome ke aplikasi
font_awesome_css = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
"""
st.markdown(font_awesome_css, unsafe_allow_html=True)

# Halaman utama
def main_page():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #2C3E50; font-size: 2.5rem;">Auditing Dashboard</h1>
        <p style="color: #7F8C8D; font-size: 1rem;">Streamlining Your Auditing Process</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("Welcome to the Auditing Dashboard!")
    st.markdown('</div>', unsafe_allow_html=True)

# Navigasi
page_names_to_funcs = {
    "🏠 Main Page": main_page,
    "📋 Sample": sample,
    "📊 Depresiasi": depresiasi,
    "🔍 Fuzzy Searching": fuzzysearch,
    "🛠️ Query Builder": querybuilder,
}

# Sidebar untuk memilih halaman
selected_page = st.sidebar.selectbox("Pilih halaman", page_names_to_funcs.keys())

# Panggil fungsi halaman yang dipilih
page_names_to_funcs[selected_page]()

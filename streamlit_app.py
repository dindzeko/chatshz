import streamlit as st

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

/* Warna profesional */
body {
    background-color: #f4f6f9;
    color: #2c3e50;
}
h1, h2, h3 {
    color: #1a5276;
}
.card {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin-bottom: 20px;
}
.cta-button {
    background-color: #1a5276;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    text-align: center;
}
.cta-button:hover {
    background-color: #133b5c;
}
</style>
"""
# Tambahkan CSS ke aplikasi
add_css(css_animation)

# Halaman utama
def main_page():
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    # Header Profesional
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="font-size: 36px; color: #1a5276;">Streamlining Your Auditing Process</h1>
        <p style="font-size: 18px; color: #5d6d7e;">Efficient tools for modern auditors.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Layout Kartu untuk Fitur Utama
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Create New Audit</h3>
            <p>Start a new audit process with guided steps.</p>
            <button class="cta-button">Create</button>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>View Reports</h3>
            <p>Access and review completed audit reports.</p>
            <button class="cta-button">View</button>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>Analyze Data</h3>
            <p>Perform data analysis for audit insights.</p>
            <button class="cta-button">Analyze</button>
        </div>
        """, unsafe_allow_html=True)
    
    # Dashboard Ringkasan
    st.markdown("""
    <h2 style="margin-top: 40px;">Audit Overview</h2>
    <p>Here’s a quick summary of your recent audits:</p>
    """, unsafe_allow_html=True)
    
    # Statistik Penting
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Audits", value="45")
    
    with col2:
        st.metric(label="Completed", value="30")
    
    with col3:
        st.metric(label="Pending", value="15")
    
    # Grafik Indikator Kinerja
    st.markdown("""
    <h3 style="margin-top: 40px;">Audit Progress</h3>
    """, unsafe_allow_html=True)
    progress_data = {"Completed": 30, "Pending": 15}
    st.bar_chart(progress_data)
    
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

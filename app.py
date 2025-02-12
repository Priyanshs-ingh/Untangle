import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Untangle - Audio Processing Suite",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme with purple and red accents
st.markdown("""
    <style>
    .stApp {
        background-color: #1A1A1A;
        color: #E0E0E0;
    }
    .sidebar .sidebar-content {
        background-color: #2D2D2D;
    }
    .stButton>button {
        background-color: #6B46C1;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #553C9A;
        transform: translateY(-2px);
    }
    .danger-button {
        background-color: #E53E3E !important;
    }
    .danger-button:hover {
        background-color: #C53030 !important;
    }
    .highlight-text {
        color: #805AD5;
    }
    .container {
        background-color: #2D2D2D;
        padding: 2rem;
        border-radius: 8px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .card {
        background-color: #363636;
        padding: 1.5rem;
        border-radius: 6px;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎵 Untangle")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "BPM Analyzer", "Stem Separator"]
)

# Home Page
if page == "Home":
    st.title("Welcome to Untangle")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='container'>
            <h3 class='highlight-text'>Your Advanced Audio Processing Suite</h3>
            <p>Transform and analyze your music with professional-grade tools.</p>
            <div class='card'>
                <h4>🎯 BPM Analysis</h4>
                <p>Detect tempo and adjust playback speed with precision</p>
            </div>
            <div class='card'>
                <h4>🎼 Stem Separation</h4>
                <p>Split your tracks into individual components</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='container'>
            <h3 class='highlight-text'>Getting Started</h3>
            <ol>
                <li>Choose a tool from the sidebar</li>
                <li>Upload your audio file</li>
                <li>Process and download the results</li>
            </ol>
            <div class='card'>
                <h4>💡 Pro Tips</h4>
                <ul>
                    <li>Supported formats: MP3, WAV</li>
                    <li>Maximum file size: 200MB</li>
                    <li>Best results with high-quality audio</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

# BPM Analyzer Page
elif page == "BPM Analyzer":
    st.title("BPM Analyzer & Speed Adjuster")
    
    with st.container():
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload your audio file", type=['mp3', 'wav'])
        
        if uploaded_file:
            st.audio(uploaded_file)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown("<h3 class='highlight-text'>BPM Detection</h3>", unsafe_allow_html=True)
                if st.button("Analyze BPM"):
                    with st.spinner("Analyzing BPM..."):
                        st.markdown("<h2>Loading...</h2>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown("<h3 class='highlight-text'>Speed Adjustment</h3>", unsafe_allow_html=True)
                st.slider("Target BPM", min_value=60, max_value=200, value=120)
                st.button("Process Audio")
                st.markdown("</div>", unsafe_allow_html=True)
                
        st.markdown("</div>", unsafe_allow_html=True)

# Stem Separator Page
elif page == "Stem Separator":
    st.title("Stem Separator")
    
    with st.container():
        st.markdown("<div class='container'>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='card'>
                <h3 class='highlight-text'>Extract Components</h3>
                <p>Separate your audio into:</p>
                <ul>
                    <li>🎤 Vocals</li>
                    <li>🥁 Drums</li>
                    <li>🎸 Bass</li>
                    <li>🎹 Piano</li>
                    <li>🎺 Other Instruments</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            uploaded_file = st.file_uploader("Upload your audio file", type=['mp3', 'wav'])
            if uploaded_file:
                st.audio(uploaded_file)
                
                separation_type = st.selectbox(
                    "Choose separation type",
                    ["2 stems (Vocals/Accompaniment)", 
                     "4 stems (Vocals/Drums/Bass/Other)", 
                     "5 stems (Vocals/Drums/Bass/Piano/Other)"]
                )
                
                if st.button("Start Separation"):
                    with st.spinner("Separating stems..."):
                        st.markdown("<h3>Processing...</h3>", unsafe_allow_html=True)
                        progress_bar = st.progress(0)
                        for i in range(100):
                            progress_bar.progress(i + 1)
                            
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='text-align: center; color: #805AD5;'>
    Made with ❤️ by Untangle Team<br>
    <small>Version 1.0.0</small>
</div>
""", unsafe_allow_html=True)
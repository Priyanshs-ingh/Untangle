import streamlit as st

class Pages:
    @staticmethod
    def render_home():
        st.title("Welcome to Untangle")
        col1, col2 = st.columns(2)
        
        with col1:
            st.header("🎵 Audio Processing Made Simple")
            st.write("""
            Untangle is your all-in-one solution for audio processing tasks.
            Choose from our suite of tools in the sidebar to get started.
            """)
            
        with col2:
            st.header("🚀 Features")
            st.write("- BPM Analysis and Speed Adjustment")
            st.write("- Stem Separation")
            st.write("- High-Quality Audio Processing")

    @staticmethod
    def render_bpm_analyzer():
        st.title("BPM Analyzer & Speed Adjuster")
        
        uploaded_file = st.file_uploader("Upload your audio file", type=['mp3', 'wav'])
        
        if uploaded_file is not None:
            st.audio(uploaded_file)
            
            col1, col2 = st.columns(2)
            with col1:
                st.button("Analyze BPM", key="analyze_bpm")
            with col2:
                speed_factor = st.slider("Speed Adjustment", 0.5, 2.0, 1.0, 0.1)

    @staticmethod
    def render_stem_separator():
        st.title("Stem Separator")
        
        uploaded_file = st.file_uploader("Upload your audio file", type=['mp3', 'wav'], key="stem_upload")
        
        if uploaded_file is not None:
            st.audio(uploaded_file)
            
            st.write("Select stems to extract:")
            col1, col2 = st.columns(2)
            with col1:
                vocals = st.checkbox("Vocals")
                drums = st.checkbox("Drums")
            with col2:
                bass = st.checkbox("Bass")
                other = st.checkbox("Other")
            
            if st.button("Separate Stems"):
                st.info("Processing... This may take a few minutes.")

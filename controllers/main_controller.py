import streamlit as st
from views.pages import Pages
from models.audio_processor import AudioProcessor
import os

class MainController:
    def __init__(self):
        self.pages = Pages()
        self.audio_processor = AudioProcessor()

    def setup_sidebar(self):
        st.sidebar.title("🎵 Untangle")
        st.sidebar.markdown("---")
        return st.sidebar.radio("Navigation", ["Home", "BPM Analyzer", "Stem Separator"])

    def handle_bpm_analysis(self, uploaded_file):
        try:
            # Save uploaded file temporarily
            temp_path = os.path.join("temp", uploaded_file.name)
            os.makedirs("temp", exist_ok=True)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Analyze BPM
            bpm = self.audio_processor.analyze_bpm(temp_path)
            
            # Clean up
            os.remove(temp_path)
            
            return bpm
        except Exception as e:
            st.error(f"Error analyzing BPM: {str(e)}")
            return None

    def handle_speed_adjustment(self, uploaded_file, target_bpm):
        try:
            # Save uploaded file temporarily
            temp_path = os.path.join("temp", uploaded_file.name)
            os.makedirs("temp", exist_ok=True)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Adjust speed
            output_path = self.audio_processor.adjust_speed(temp_path, target_bpm)
            
            # Read processed file
            with open(output_path, "rb") as f:
                processed_audio = f.read()
            
            # Clean up
            os.remove(temp_path)
            os.remove(output_path)
            
            return processed_audio
        except Exception as e:
            st.error(f"Error adjusting speed: {str(e)}")
            return None

    def handle_stem_separation(self, uploaded_file):
        try:
            # Save uploaded file temporarily
            temp_path = os.path.join("temp", uploaded_file.name)
            os.makedirs("temp", exist_ok=True)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Separate stems
            output_path = self.audio_processor.separate_stems(temp_path)
            
            # Get all generated files
            separated_files = {}
            for stem in ["vocals", "drums", "bass", "piano", "other"]:
                stem_path = os.path.join(output_path, os.path.splitext(uploaded_file.name)[0], f"{stem}.wav")
                if os.path.exists(stem_path):
                    with open(stem_path, "rb") as f:
                        separated_files[stem] = f.read()
            
            # Clean up
            os.remove(temp_path)
            os.removedirs(output_path)
            
            return separated_files
        except Exception as e:
            st.error(f"Error separating stems: {str(e)}")
            return None

    def route(self):
        page = self.setup_sidebar()
        
        if page == "Home":
            self.pages.render_home()
        
        elif page == "BPM Analyzer":
            uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
            if uploaded_file:
                bpm = self.handle_bpm_analysis(uploaded_file)
                if bpm:
                    st.success(f"Detected BPM: {bpm}")
                    
                    target_bpm = st.number_input("Target BPM", min_value=1, max_value=300, value=int(bpm))
                    if st.button("Adjust Speed"):
                        processed_audio = self.handle_speed_adjustment(uploaded_file, target_bpm)
                        if processed_audio:
                            st.audio(processed_audio, format="audio/wav")
        
        elif page == "Stem Separator":
            uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
            if uploaded_file and st.button("Separate Stems"):
                separated_files = self.handle_stem_separation(uploaded_file)
                if separated_files:
                    for stem, audio_data in separated_files.items():
                        st.subheader(stem.title())
                        st.audio(audio_data, format="audio/wav")

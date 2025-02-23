import streamlit as st
from controllers.main_controller import MainController
from views.styles import load_css

# Set page configuration
st.set_page_config(
    page_title="Untangle - Audio Processing Suite", 
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Initialize and run application
controller = MainController()
controller.route()
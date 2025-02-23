def load_css():
    return """
    <style>
    .stApp {
        background: linear-gradient(135deg, #121212 0%, #1E1E1E 100%);
        color: #F4F4F5;
    }
    
    .stButton button {
        background-color: #2D2D2D;
        color: #F4F4F5;
        border: 1px solid #3D3D3D;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        background-color: #3D3D3D;
        border-color: #4D4D4D;
    }
    
    .stTextInput input {
        background-color: #2D2D2D;
        color: #F4F4F5;
        border: 1px solid #3D3D3D;
    }
    
    .stSelectbox select {
        background-color: #2D2D2D;
        color: #F4F4F5;
    }
    
    h1, h2, h3 {
        color: #F4F4F5;
    }
    </style>
    """

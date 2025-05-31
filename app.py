import streamlit as st

st.set_page_config(page_title="NumaX", page_icon="🎨", layout="centered", initial_sidebar_state="expanded")

st.markdown(
    '''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');
    body, .main {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Playfair Display', serif;
    }
    .title {
        font-weight: bold;
        font-size: 36px;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        font-weight: bold;
        font-size: 28px;
        text-align: center;
        color: #e0e0e0;
        margin-bottom: 30px;
    }
    .sidebar .sidebar-content {
        background-color: #1e1e1e;
        color: #e0e0e0;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888888;
        font-size: 12px;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

st.markdown('<div class="title">Welcome to NumaX</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">NumaX — Where Emotion Finds Form</div>', unsafe_allow_html=True)

emotion = st.text_input("Enter Emotion", placeholder="e.g. calm, energetic, mysterious")
style = st.selectbox("Select Art Style", [
    "Abstract", "Watercolor", "Oil Painting", "Digital Art", "Minimalist", "Cubism", "Pop Art", "Surrealism"
])
palette = st.selectbox("Select Color Palette", [
    "Warm", "Cool", "Monochrome", "Pastel", "Vibrant", "Earth Tones", "Black & White"
])

if st.button("Generate Image"):
    st.success(f"Generating image with Emotion: '{emotion}', Style: '{style}', Palette: '{palette}' ...")
    st.image("https://via.placeholder.com/512x512.png?text=Generated+Image", caption=f"Emotion: {emotion}, Style: {style}, Palette: {palette}")

st.markdown('<div class="footer">© 2025 NumaX Project by Pari Shojaienasab</div>', unsafe_allow_html=True)

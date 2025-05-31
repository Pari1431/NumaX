import streamlit as st

st.set_page_config(page_title="NumaX", page_icon="🎨", layout="centered")

# CSS برای پس‌زمینه مشکی و فونت سفید
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap');
    body {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'Noto Sans', sans-serif;
    }
    .stApp {
        max-width: 600px;
        margin: auto;
        padding: 2rem;
    }
    h1 {
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    p.subtitle {
        text-align: center;
        font-size: 1.2rem;
        margin-top: 0;
        margin-bottom: 2rem;
        color: #bbbbbb;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

st.title("NumaX")
st.markdown('<p class="subtitle">✨ NumaX — Where Emotion Finds Form</p>', unsafe_allow_html=True)

# ورودی‌ها
emotion = st.text_input("Enter your emotion:")
style = st.text_input("Enter the artistic style:")
color_palette = st.text_input("Enter color palette (comma separated):")

if emotion or style or color_palette:
    st.markdown("---")
    st.subheader("Your Input:")
    if emotion:
        st.write(f"**Emotion:** {emotion}")
    if style:
        st.write(f"**Artistic Style:** {style}")
    if color_palette:
        st.write(f"**Color Palette:** {color_palette}")

    # اینجا میتونی کد تولید تصویر رو اضافه کنی
    st.info("Image generation feature will be added here soon.")

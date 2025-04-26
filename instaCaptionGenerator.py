import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Instagram Caption Generator")
st.title("AI Instagram Caption Generator")
api_key = st.secrets.get("google")

if not api_key:
    api_key = st.text_input("Enter your Gemini API Key: " , type="password")

if api_key:
    # genai.configure(api_key=api_key)
    genai.configure(api_key=st.secrets["google"]["api_key"])
    reel_description = st.text_area("Describe your reel: ")
    tone = st.selectbox("Choose the type of tone: ",
                        ["Funny", "Trendy", "Inspirational", "Professional"])

if st.button("Generate Captions"):
    if reel_description.strip() == "":
        st.warning("Enter your reel description")
    else:
        st.info("Genrating Your Description....")
        prompt = f"Write 5 {tone.lower()} Instagram captions for a reel about: '{reel_description}'. Each caption should be short, engaging, and trendy."

        # model = genai.GenerativeModel('gemini-pro')
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")
        response = model.generate_content(prompt)

        if response and response.text:
            captions = response.text.split("\n")
            for i, caption in enumerate(captions):
                if caption.strip() != "":
                    st.write(f"**Caption** {i+1}: **{caption.strip()}**")
        else:
            st.error("Failed to Generate caption.... Try Again Later")

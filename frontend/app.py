import streamlit as st
import requests

st.title("🚀 StartupLens AI")

idea = st.text_area(
    "Enter Startup Idea"
)

if st.button("Validate Idea"):

    with st.spinner("Analyzing..."):

        response = requests.post(
            "http://127.0.0.1:8000/validate",
            json={"idea": idea}
        )

        result = response.json()

        st.markdown(
            result["analysis"]
        )
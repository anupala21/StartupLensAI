import streamlit as st
import requests

st.title("🚀 StartupLens AI")

idea = st.text_area(
    "Enter Startup Idea"
)
if st.button("Validate Idea"):

    with st.spinner("Analyzing startup idea..."):

        response = requests.post(
            "http://127.0.0.1:8000/validate",
            json={"idea": idea}
        )

        result = response.json()
        #st.write(result)

        col1, col2 = st.columns(2)

        with col1:
            if "innovation_score" not in result:
                st.error("Backend did not return expected JSON")
                st.write(result)
                st.stop()

            st.metric(
                "Innovation Score",
                f"{result['innovation_score']}/10"
            )

            st.metric(
                "Market Potential",
                f"{result['market_potential']}/10"
            )

        with col2:
            st.metric(
                "Competition",
                result['competition_level']
            )

        st.metric(
            "Success Probability",
            f"{result['success_probability']}%"
        )

        st.progress(
            result["success_probability"] / 100
        )

        st.subheader("Recommendations")

        for rec in result["recommendations"]:
            st.write("✅", rec)
            st.divider()

st.subheader("🏢 Competitor Analysis")

if st.button("Find Competitors"):

    with st.spinner("Finding competitors..."):

        response = requests.post(
            "http://127.0.0.1:8000/competitors",
            json={"idea": idea}
        )

        result = response.json()

        st.markdown("### Top Competitors")

        for comp in result["competitors"]:
            st.write("🏢", comp)

        st.markdown("### Market Gap")

        st.info(
            result["market_gap"]
        )

        st.markdown("### Opportunity Level")

        st.success(
            result["opportunity_level"]
        )
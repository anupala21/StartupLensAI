import streamlit as st
import requests

st.set_page_config(
    page_title="StartupLens AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 StartupLens AI")

idea = st.text_area(
    "Enter Startup Idea",
    placeholder="Example: AI platform that helps students transform academic projects into startups."
)
st.info(
    "StartupLens AI uses Gemini API. Results depend on API availability."
)
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Validation",
    "🏢 Competitors Analysis",
    "📊 Market Research",
    "🚀 Blueprint"
])

# =====================================================
# VALIDATION TAB
# =====================================================

with tab1:

    if st.button("Validate Idea"):

        with st.spinner("Analyzing startup idea..."):

            response = requests.post(
                "http://127.0.0.1:8000/validate",
                json={"idea": idea}
            )

            result = response.json()

            if "innovation_score" not in result:
                st.error("Backend did not return expected JSON")
                st.write(result)
                st.stop()

            col1, col2 = st.columns(2)

            with col1:
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
                    result["competition_level"]
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

# =====================================================
# COMPETITOR TAB
# =====================================================

with tab2:

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

# =====================================================
# MARKET RESEARCH TAB
# =====================================================

with tab3:

    st.subheader("📊 Market Research")

    if st.button("Analyze Market"):

        with st.spinner("Analyzing market..."):

            response = requests.post(
                "http://127.0.0.1:8000/market-research",
                json={"idea": idea}
            )

            result = response.json()

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "TAM",
                    result["tam"]
                )

                st.metric(
                    "SAM",
                    result["sam"]
                )

            with col2:
                st.metric(
                    "SOM",
                    result["som"]
                )

                st.metric(
                    "Growth Rate",
                    result["growth_rate"]
                )

            st.subheader("🎯 Target Audience")

            for audience in result["target_audience"]:
                st.write("🎯", audience)
# =====================================================
# BLUEPRINT TAB
# =====================================================

with tab4:

    st.subheader("🚀 Startup Blueprint")

    if st.button("Generate Blueprint"):

        with st.spinner("Generating startup blueprint..."):

            response = requests.post(
                "http://127.0.0.1:8000/blueprint",
                json={"idea": idea}
            )

            result = response.json()

            st.markdown("## 📌 Executive Summary")
            st.info(result["executive_summary"])

            st.markdown("## ❗ Problem Statement")
            st.write(result["problem_statement"])

            st.markdown("## 💡 Solution")
            st.write(result["solution"])

            st.markdown("## 🎯 Target Audience")
            st.write(result["target_audience"])

            st.markdown("## 💰 Revenue Model")
            st.write(result["revenue_model"])

            st.markdown("## 🚀 Go-To-Market Strategy")
            st.write(result["go_to_market_strategy"])

            st.markdown("## 🏦 Funding Recommendation")
            st.success(result["funding_recommendation"])
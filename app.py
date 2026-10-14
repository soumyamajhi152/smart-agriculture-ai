import streamlit as st

st.set_page_config(
    page_title="Smart Agriculture AI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AI-Powered Smart Agriculture")
st.write("An AI-based agricultural decision-support dashboard.")

st.info(
    "This prototype demonstrates crop recommendations, "
    "irrigation guidance, and soil analysis."
)

page = st.sidebar.selectbox(
    "Choose a module",
    [
        "Home",
        "Crop Recommendation",
        "Irrigation Advisor",
        "Soil Analysis",
        "Business Insights"
    ]
)

if page == "Home":
    st.header("Project Overview")
    st.write("Business problem: Farmers need support choosing crops, "
             "managing irrigation, and understanding soil conditions.")
    st.write("Proposed solution: Use data and simple decision-support "
             "tools to assist agricultural decisions.")

elif page == "Crop Recommendation":
    st.header("🌾 Crop Recommendation")
    st.write("Enter soil and weather measurements.")

    n = st.number_input("Nitrogen (N)", 0.0, value=90.0)
    p = st.number_input("Phosphorus (P)", 0.0, value=40.0)
    k = st.number_input("Potassium (K)", 0.0, value=40.0)
    temperature = st.number_input("Temperature (°C)", value=25.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 80.0)
    ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)
    rainfall = st.number_input("Rainfall (mm)", 0.0, value=100.0)

    st.warning(
        "The trained crop prediction model has not yet been connected. "
        "These inputs are ready for integration with the model."
    )

elif page == "Irrigation Advisor":
    st.header("💧 Irrigation Advisor")
    moisture = st.slider("Soil moisture (%)", 0, 100, 25)
    rain = st.number_input("Expected rainfall (mm)", 0.0, value=10.0)

    if moisture < 30 and rain < 40:
        st.info("Irrigation may be needed soon.")
    elif moisture < 30:
        st.info("Check the rainfall forecast before irrigating.")
    elif moisture < 60:
        st.info("Monitor soil moisture and crop water needs.")
    else:
        st.success("Irrigation may not be needed immediately.")

    st.caption("Illustrative guidance only; thresholds need local validation.")

elif page == "Soil Analysis":
    st.header("🧪 Soil Analysis")
    n = st.number_input("Soil nitrogen", 0.0, value=40.0)
    p = st.number_input("Soil phosphorus", 0.0, value=30.0)
    k = st.number_input("Soil potassium", 0.0, value=35.0)
    ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)

    st.bar_chart({
        "Nutrient value": {
            "Nitrogen": n,
            "Phosphorus": p,
            "Potassium": k
        }
    })

    if ph < 5.5:
        st.warning("Observation: Soil is acidic.")
    elif ph > 7.5:
        st.warning("Observation: Soil is alkaline.")
    else:
        st.success("Observation: pH is within the illustrative range.")

    st.caption("Use laboratory soil tests and local agricultural guidance.")

elif page == "Business Insights":
    st.header("📊 Business Decisions")
    st.write("Potential business value:")
    st.markdown("""
    - Support crop selection using soil and weather data.
    - Help farmers monitor irrigation needs.
    - Improve understanding of soil measurements.
    - Explore future pest and disease detection.
    - Evaluate adoption, costs, and farmer usability before deployment.
    """)

st.divider()
st.caption("MBA Information Management Project | AI in Business")

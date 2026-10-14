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

    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    @st.cache_resource
    def train_crop_model():
        data = pd.read_excel("Crop_recommendation.xlsx")

        X = data[[
            "N", "P", "K", "temperature",
            "humidity", "ph", "rainfall"
        ]]
        y = data["label"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = RandomForestClassifier(
            n_estimators=100, random_state=42
        )
        model.fit(X_train, y_train)

        accuracy = accuracy_score(
            y_test, model.predict(X_test)
        )

        return model, accuracy

    try:
        model, accuracy = train_crop_model()

        st.success(
            f"Crop prediction model is ready! "
            f"Test accuracy: {accuracy * 100:.2f}%"
        )

        n = st.number_input("Nitrogen (N)", min_value=0.0, value=90.0)
        p = st.number_input("Phosphorus (P)", min_value=0.0, value=40.0)
        k = st.number_input("Potassium (K)", min_value=0.0, value=40.0)
        temperature = st.number_input("Temperature (°C)", value=25.0)
        humidity = st.number_input(
            "Humidity (%)", min_value=0.0,
            max_value=100.0, value=80.0
        )
        ph = st.number_input(
            "Soil pH", min_value=0.0,
            max_value=14.0, value=6.5
        )
        rainfall = st.number_input(
            "Rainfall (mm)", min_value=0.0, value=100.0
        )

        if st.button("🌱 Recommend Crop"):
            input_data = pd.DataFrame(
                [[n, p, k, temperature, humidity, ph, rainfall]],
                columns=[
                    "N", "P", "K", "temperature",
                    "humidity", "ph", "rainfall"
                ]
            )

            prediction = model.predict(input_data)[0]

            st.success(f"### Recommended Crop: {prediction.title()}")

            probabilities = model.predict_proba(input_data)[0]
            confidence = max(probabilities) * 100

            st.info(
                f"Model confidence: {confidence:.2f}%"
            )

            st.caption(
                "This recommendation is based on the dataset "
                "and model predictions. Actual crop suitability "
                "depends on local conditions and expert advice."
            )

    except Exception as e:
        st.error(f"Unable to load the crop model: {e}")
        st.info(
            "Check that Crop_recommendation.xlsx is in the "
            "repository and the required packages are installed."
        )
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

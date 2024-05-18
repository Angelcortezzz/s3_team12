import streamlit as st

# Define thresholds for each air quality parameter as ranges
thresholds = {
    "CO": {"good": (0.0, 2.0), "moderate": (2.0, 4.0), "usg": (4.0, 6.0), "unhealthy": (6.0, 8.0), "very_unhealthy": (8.0, 10.0), "hazardous": (10.0, float('inf'))},
    "NMHC": {"good": (0.0, 200.0), "moderate": (200.0, 400.0), "usg": (400.0, 600.0), "unhealthy": (600.0, 800.0), "very_unhealthy": (800.0, 1000.0), "hazardous": (1000.0, float('inf'))},
    "Benzene": {"good": (0.0, 5.0), "moderate": (5.0, 10.0), "usg": (10.0, 15.0), "unhealthy": (15.0, 20.0), "very_unhealthy": (20.0, 25.0), "hazardous": (25.0, float('inf'))},
    "NOx": {"good": (0.0, 50.0), "moderate": (50.0, 100.0), "usg": (100.0, 150.0), "unhealthy": (150.0, 200.0), "very_unhealthy": (200.0, 300.0), "hazardous": (300.0, float('inf'))},
    "NO2": {"good": (0.0, 10.0), "moderate": (10.0, 20.0), "usg": (20.0, 30.0), "unhealthy": (30.0, 40.0), "very_unhealthy": (40.0, 50.0), "hazardous": (50.0, float('inf'))},
    "Temperature": {"good": (-20.0, 15.0), "moderate": (15.0, 20.0), "usg": (20.0, 25.0), "unhealthy": (25.0, 30.0), "very_unhealthy": (30.0, 35.0), "hazardous": (35.0, float('inf'))},
    "RH": {"good": (0.0, 40.0), "moderate": (40.0, 50.0), "usg": (50.0, 60.0), "unhealthy": (60.0, 70.0), "very_unhealthy": (70.0, 80.0), "hazardous": (80.0, float('inf'))}
}

# Check air quality prediction
def predict_air_quality(co, nmhc, benzene, nox, no2, temp, rh):
    categories = ["good", "moderate", "usg", "unhealthy", "very_unhealthy", "hazardous"]
    predicted_category = "good"  # Initialize predicted category as "good"
    
    for param, param_thresholds in thresholds.items():
        for category, threshold_range in param_thresholds.items():
            if threshold_range[0] <= locals()[param] < threshold_range[1]:
                predicted_category = category
                break  # Exit the loop once a category is found
    
    return predicted_category

# Input sliders
st.title("Air Quality Prediction")
co = st.slider("CO", min_value=0.0, max_value=20.0, step=0.01, format="%.5f")
nmhc = st.slider("NMHC", min_value=0.0, max_value=2000.0, step=0.01, format="%.5f")
benzene = st.slider("Benzene", min_value=0.0, max_value=50.0, step=0.01, format="%.5f")
nox = st.slider("NOx", min_value=0.0, max_value=500.0, step=0.01, format="%.5f")
no2 = st.slider("NO2", min_value=0.0, max_value=100.0, step=0.01, format="%.5f")
temp = st.slider("Temperature", min_value=-20.0, max_value=50.0, step=0.01, format="%.5f")
rh = st.slider("RH", min_value=0.0, max_value=100.0, step=0.01, format="%.5f")

# Predict air quality
if st.button("Predict Air Quality"):
    air_quality_category = predict_air_quality(co, nmhc, benzene, nox, no2, temp, rh)
    st.write(f"The air quality is predicted as: {air_quality_category.capitalize()}")

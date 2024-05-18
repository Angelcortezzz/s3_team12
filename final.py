import streamlit as st

# Title
st.title("Air Quality")

# Define columns
col1, col2, col3 = st.columns(3)

# Sliders in the first column
with col1:
    co = st.slider("CO", min_value=0.0, max_value=10.0, step=0.01, format="%.5f")
    nmhc = st.slider("NMHC", min_value=0.0, max_value=1000.0, step=0.01, format="%.5f")
    benzene = st.slider("Benzene", min_value=0.0, max_value=50.0, step=0.01, format="%.5f")
    nox = st.slider("NOx", min_value=0.0, max_value=1000.0, step=0.01, format="%.5f")

# Sliders in the second column
with col2:
    no2 = st.slider("NO2", min_value=0.0, max_value=200.0, step=0.01, format="%.5f")
    temp = st.slider("Temperature", min_value=-20.0, max_value=50.0, step=0.01, format="%.5f")
    rh = st.slider("RH", min_value=0.0, max_value=100.0, step=0.01, format="%.5f")
    ah = st.slider("AH", min_value=0.0, max_value=50.0, step=0.01, format="%.5f")
# Define thresholds for each air quality parameter
thresholds = {
    "CO": {"good": 2.0, "moderate": 4.0, "usg": 6.0, "unhealthy": 8.0, "very_unhealthy": 10.0, "hazardous": 15.0},
    "NMHC": {"good": 200.0, "moderate": 400.0, "usg": 600.0, "unhealthy": 800.0, "very_unhealthy": 1000.0, "hazardous": 1500.0},
    "Benzene": {"good": 5.0, "moderate": 10.0, "usg": 15.0, "unhealthy": 20.0, "very_unhealthy": 25.0, "hazardous": 30.0},
    "NOx": {"good": 50.0, "moderate": 100.0, "usg": 150.0, "unhealthy": 200.0, "very_unhealthy": 300.0, "hazardous": 400.0},
    "NO2": {"good": 10.0, "moderate": 20.0, "usg": 30.0, "unhealthy": 40.0, "very_unhealthy": 50.0, "hazardous": 60.0},
    "Temperature": {"good": 15.0, "moderate": 20.0, "usg": 25.0, "unhealthy": 30.0, "very_unhealthy": 35.0, "hazardous": 40.0},
    "RH": {"good": 40.0, "moderate": 50.0, "usg": 60.0, "unhealthy": 70.0, "very_unhealthy": 80.0, "hazardous": 90.0}
}

# Check air quality classification
def classify_air_quality(co, nmhc, benzene, nox, no2, temp, rh):
    categories = ["good", "moderate", "usg", "unhealthy", "very_unhealthy", "hazardous"]
    worst_category = "good"  # Initialize worst category as "good"
    
    for param in thresholds:
        for category in categories:
            if locals()[param] > thresholds[param][category]:
                worst_category = category
    
    return worst_category

# Input sliders
st.title("Air Quality Classification")
co = st.slider("CO", min_value=0.0, max_value=20.0, step=0.01, format="%.5f")
nmhc = st.slider("NMHC", min_value=0.0, max_value=2000.0, step=0.01, format="%.5f")
benzene = st.slider("Benzene", min_value=0.0, max_value=50.0, step=0.01, format="%.5f")
nox = st.slider("NOx", min_value=0.0, max_value=500.0, step=0.01, format="%.5f")
no2 = st.slider("NO2", min_value=0.0, max_value=100.0, step=0.01, format="%.5f")
temp = st.slider("Temperature", min_value=-20.0, max_value=50.0, step=0.01, format="%.5f")
rh = st.slider("RH", min_value=0.0, max_value=100.0, step=0.01, format="%.5f")

# Classify air quality
air_quality_category = classify_air_quality(co, nmhc, benzene, nox, no2, temp, rh)
st.write(f"The air quality is classified as: {air_quality_category.capitalize()}")

# CSS to style the entire app with the background image
background_css = '''
<style>
body {
    background-image: url('https://e7.pngegg.com/pngimages/401/219/png-clipart-blue-cloud-art-cloud-computing-cloud-blue-cloud-thumbnail.png');
    background-size: cover;
}
</style>
'''

# Apply the CSS styling to the entire app
st.markdown(background_css, unsafe_allow_html=True)

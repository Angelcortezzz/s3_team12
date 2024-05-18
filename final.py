import streamlit as st

# CSS to style the slider thumb with a cloud image and set the background image for the entire app
cloud_slider_css = '''
<style>
body {
    background-image: url('https://e7.pngegg.com/pngimages/401/219/png-clipart-blue-cloud-art-cloud-computing-cloud-blue-cloud-thumbnail.png');
    background-size: cover;
}

.st-ck[data-baseweb="slider"] > .st-ck-thumb {
    background-image: url('https://e7.pngegg.com/pngimages/401/219/png-clipart-blue-cloud-art-cloud-computing-cloud-blue-cloud-thumbnail.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    width: 25px; /* Adjust the width of the cloud image */
    height: 25px; /* Adjust the height of the cloud image */
    border: none; /* Remove border */
    border-radius: 50%; /* Make it circular */
}
</style>
'''

# Apply the CSS styling to the entire app
st.markdown(cloud_slider_css, unsafe_allow_html=True)

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

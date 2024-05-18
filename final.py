import streamlit as st
import numpy as np
import tensorflow as tf



@st.cache_resource
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

model = load_model('C:/Users/robvi/Downloads/streamlit/model (3).h5')

st.title("Air Quality Prediction")


col1, col2, col3 = st.columns(3)

with col1:
    co = st.slider("CO", min_value=0.0, max_value=10.0, step=0.01, format="%.5f")
    nmhc = st.slider("NMHC", min_value=0.0, max_value=1000.0, step=0.01, format="%.5f")
    benzene = st.slider("Benzene", min_value=0.0, max_value=50.0, step=0.01, format="%.5f")
    nox = st.slider("NOx", min_value=0.0, max_value=1000.0, step=0.01, format="%.5f")

with col2:
    no2 = st.slider("NO2", min_value=0.0, max_value=200.0, step=0.01, format="%.5f")
    temp = st.slider("Temperature", min_value=-20.0, max_value=50.0, step=0.01, format="%.5f")
    rh = st.slider("RH", min_value=0.0, max_value=100.0, step=0.01, format="%.5f")
    ah = st.slider("AH", min_value=0.0, max_value=50.0, step=0.01, format="%.5f")

if st.button("Predict"):
    features = np.array([[co, nmhc, benzene, nox, no2, temp, rh, ah]])
    prediction = model.predict(features)
    st.write(f"Predicted Air Quality Value: {prediction[0][0]:.5f}")

# CSS to style the slider thumb with a cloud image
cloud_slider_css = '''
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
'''

st.markdown(cloud_slider_css, unsafe_allow_html=True)

import streamlit as st
import numpy as np
import tensorflow as tf

@st.cache_resource
def load_model(filepath):
    model = tf.keras.models.load_model(filepath)
    return model

st.title("Predicting Air Quality using LSTM Model")

model = load_model('model.h5')



import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the streamlit app page a title
st.title("Vehicle One Year Resale Value")

# input widget for getting user value for X (feature matrix value)
price = st.slider("Price[thousand dollars]", color="blue", min_value=0, max_value=100, value=20)

#after selecting the price, the user then submits the price value
if st.button("Predict"):
  # take the price value, and format the value the right way
  prediction = model.predict([[price]])[0].round(2)
  st.write("The predicted One Year Resale Value of your vehicle is", prediction, "thousand dollars")

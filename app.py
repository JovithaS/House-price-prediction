import streamlit as st
import joblib
 
#load the traind model
model = joblib.load("house_model.pkl")
 
st.title("House Price Prediction App")
st.write("Enter house details to predict price")
 
#User input fields
size = st.number_input("House Size (sz ft)")
bedrooms = st.number_input("Number of Bedrooms")
age = st.number_input("House Age")
 
#Prediction button
if st.button("Prdict Price"):
    prediction = model.predict([[size, bedrooms, age]])
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")
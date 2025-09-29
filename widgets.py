import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Widgets Example")

name = st.text_input("Enter your name")

age = st.slider("Select your age", 0, 100)

color = st.selectbox("Select your favorite color", ["Red", "Green", "Blue", "Yellow"])
if name:
    st.write(f"Hello, {name}!")
  
if age:
    st.write(f"You are {age} years old.")

if color:
    st.write(f"Your favorite color is {color}.")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write("Sample DataFrame:")
st.write(df)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.write(df)
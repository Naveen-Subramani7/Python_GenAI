import streamlit as st
import pandas as pd
import numpy as np

## Add Title
st.title("Hello Streamlit")

## Add Text
st.write("This is sample text")

## Add Dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## Display Dataframe
st.write("Dataframe")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

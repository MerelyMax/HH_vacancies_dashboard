import streamlit as st
import pandas as pd
import numpy as np
from datetime import time



st.header('Dataframes in the dashboard')
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.header('Sliders')
age = st.slider('How old are you?', 0, 130, 50)
st.write('I\'m' , age, 'years old')

appointment = st.slider(
       "Schedule your appointment:",
        value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)
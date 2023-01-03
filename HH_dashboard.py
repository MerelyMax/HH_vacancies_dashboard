import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

if __name__ == '__main__':

    st.header('Dataframes in the dashboard')
    df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

    st.header('Sliders')
    age = st.slider('How old are you?', 0, 130, 50)
    st.write('I\'m' , age, 'years old')

    appointment_time = st.slider('Schedule your appointment for:', 
                                value = (time(7,30), time(12,45)))
    st.write('Your appointment is scheduled for', appointment_time)


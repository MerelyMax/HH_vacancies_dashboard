import streamlit as st
import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')


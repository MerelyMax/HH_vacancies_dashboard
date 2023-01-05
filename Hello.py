import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

if __name__ == '__main__':
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Data analytic vacancies from hh.ru job search website")

    #st.sidebar.success("Select a demo above.")

    st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar**
    """
    )
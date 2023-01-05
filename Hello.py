import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

if __name__ == '__main__':
    st.set_page_config(
        page_title="About",
        page_icon="ℹ️",
    )

    st.write("# \"Data analytic\" jobs👨‍💻 - Analysis")
    st.write("(Skills, salary, etc)")
    st.write("### Data provided from hh.ru - job search site")

    #st.sidebar.success("Select a demo above.")

    st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar**
    """
    )
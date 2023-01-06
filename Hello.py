import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

if __name__ == '__main__':
    st.set_page_config(
        page_title="About",
        page_icon="ℹ️",
    )

    st.markdown("""
             # \"Data analyst\" jobs👨‍💻 - Analysis
             \n This dashboard presents statistics about Data Analyst jobs: *number of vacancies*, 
             *skills* required, *salary* and more. To discover all of the data, use pages 
             on the sidebar (on the left handside of the page).
             """)
    html_string = "<h3 style='text-align: center'> Data provided from hh.ru - job search website</h3>"
    st.markdown("""<h3 style='text-align: center'> 
                Data provided from hh.ru - job search website 
                </h3>""")
    
    st.markdown("""---""")
    
    #st.sidebar.success("Select a demo above.")

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
             # Data analyst jobs👨‍💻 - Analysis
             \n This dashboard presents **statistics about Data Analyst jobs**: 
             **number of vacancies**, **skills** required, **salary** and more. 
             To discover all of the data, use pages on the sidebar 
             (on the left handside of the page).
             """)
    # html_string = "<h3 style='text-align: center;'> Data provided from hh.ru - job search website</h3>"
    st.markdown("""
                **Data provided from hh.ru - job search website** 
                """)
    
    st.markdown("""---""")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Last updated:")
    with col2:
        st.write("Total processed entries:")

    #st.sidebar.success("Select a demo above.")

########################################################################################################
# Кусок кода с анимированным построением графика.
# Реализовать для это страницы?
# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")
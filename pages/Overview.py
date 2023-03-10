import streamlit as st
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Vacancies overview", page_icon="📈")

st.markdown("# Plotting Demo")

# Function to extract data fron .json file
def extract_json_file(file_name):
    f = open(file_name, mode='r', encoding='utf8')
    return json.loads('[' + f.read() + ']')

# Extracting data
data = extract_json_file(os.path.dirname(__file__) + '/vacancies_data.json')
df_data = pd.DataFrame(data)
area_jobs = df_data['area-name'].value_counts()

# Adding interactive filter
vac_num_choice = st.sidebar.slider(
                    'Max vacansies number:', min_value=int(area_jobs.min()), 
                                             max_value=int(area_jobs.max()), 
                                             step=1, value=10)

# Constructing plot
others = pd.Series(area_jobs[area_jobs.values < vac_num_choice].values.sum(),
                   index = ['Другие'])
area_jobs = area_jobs[area_jobs.values > vac_num_choice].append(others)

fig, ax = plt.subplots(figsize=(15,5))
hist1 = ax.bar(area_jobs.index, area_jobs.values)
ax.tick_params(axis='x', rotation=90, labelsize=12)
ax.tick_params(axis='y', labelsize=12)
ax.set_xlabel('City', fontsize=14)
ax.set_ylabel('Vacancies number', fontsize=13)
ax.bar_label(hist1)

st.pyplot(fig)
import streamlit as st
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Количество вакансий", page_icon="📈")

st.markdown("# Количество вакансий *аналитик данных* по городам России")

# Function to extract data fron .json file
def extract_json_file(file_name):
    f = open(file_name, mode='r', encoding='utf8')
    return json.loads('[' + f.read() + ']')

# Extracting data
data = extract_json_file(os.path.dirname(__file__) + '/vacancies_data.json')
df_data = pd.DataFrame(data)
area_jobs = df_data['area-name'].value_counts()

# Adding interactive filter
num_of_cities_option = st.sidebar.selectbox(
                    'Выберите количество городов для отображения:', 
                    ('Топ 5', 'Топ 10', 'Топ 20', 'Показать все'))
num_of_cities_dict = {
    'Топ 5' : 5,
    'Топ 10' : 10,
    'Топ 20' : 20,
    'Показать все' : area_jobs.count(),
}
# Constructing plot
# Add 'Others' category to a plot for numeric num_of_cities_option
if (num_of_cities_option != 'Показать все'):
    others = pd.Series(
        area_jobs[num_of_cities_dict[num_of_cities_option]:].values.sum(),
        index = ['Другие'])
    area_jobs = pd.concat([area_jobs[:num_of_cities_dict[num_of_cities_option]],
                                 others])

fig, ax = plt.subplots(figsize=(15,5))
hist1 = ax.bar(area_jobs.index, area_jobs.values)
ax.tick_params(axis='x', rotation=90, labelsize=12)
ax.tick_params(axis='y', labelsize=12)
ax.set_xlabel('City', fontsize=14)
ax.set_ylabel('Vacancies number', fontsize=13)
ax.bar_label(hist1)

st.pyplot(fig)
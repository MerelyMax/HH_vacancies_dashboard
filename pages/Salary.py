import streamlit as st
import json
import os
import numpy as np
import pandas as pd
import altair as alt
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import dateutil.parser

st.set_page_config(page_title="Salaries analysis", page_icon="📈")

# Function to extract data fron .json file
def extract_json_file(file_name):
    f = open(file_name, mode='r', encoding='utf8')
    return json.loads('[' + f.read() + ']')

# Extracting data
data = extract_json_file(os.path.dirname(__file__) + '/vacancies_data.json')
df_data = pd.DataFrame(data)
# Добавление нового столбца published_at_datetime - преобразование
# даты ISO860 str в тип datetime naive
df_data['published_at_datetime'] = df_data['published_at'].apply(lambda x: dateutil.parser.isoparse(
                                                                                x).replace(tzinfo=None))

# Adding interactive filters
job_counts_by_area = df_data['area-name'].value_counts()
city_choice = st.sidebar.selectbox(
    'Choose city:', 
    job_counts_by_area[job_counts_by_area.values > 10].keys())
currency_choice = st.sidebar.selectbox(
    'Choose currency:', 
    df_data['salary-currency'].dropna().unique())

# Constructing plots
# Медиана по городам в разрезе месяца
# Определим дату начала текущего месяца
# (отключим в целях тестирования)
# start_of_month = datetime(date.today().year, date.today().month, 1)
start_of_month = datetime(2023, 2, 1)

# Определим дату окончания текущего месяца
# (отключим в целях тестирования)
# end_of_month = start_of_month + relativedelta(months=1) - timedelta(days=1)
end_of_month = datetime(2023, 2, 28)
# Фильтруем данные: выбираем строки между датами текущего месяца
# Исключаем з/п в USD, а также None значения
data_for_barchart1 = df_data[(df_data['published_at_datetime'] >= start_of_month) 
                        & (df_data['published_at_datetime'] <= end_of_month)
                        & (df_data['salary-currency'] != 'USD')].dropna(
                            ).groupby('area-name', 
                                      sort=False,
                                      as_index = False).median().sort_values(by = 'salary-from',
                                                                                    ascending = False)           
barchart1 = alt.Chart(data_for_barchart1).mark_bar().encode(x = alt.X('area-name:O',
                                                                      sort=alt.EncodingSortField('salary-from', 
                                                                                                 op='min', 
                                                                                                 order='descending')),
                                                    y = alt.Y('salary-from:Q')
                                                    )
# Добавим подписи столбцам
text_for_barchart1 = barchart1.mark_text(
    align='center',
    baseline='middle',
    dy=-7  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='salary-from:Q')   
# ранее рисовал гистограмму
# hist2 = alt.Chart(df_data['salary-to'][(df_data['area-name'] == city_choice) & 
#                                         (df_data['salary-currency'] == currency_choice)].to_frame()
#                   ).mark_bar().encode(alt.X('salary-to:Q', bin = True),
#                                             y = 'count()',
#                                     )
data_for_boxplot = df_data[(df_data['published_at_datetime'] >= start_of_month) &
                           (df_data['published_at_datetime'] <= end_of_month) &
                           (df_data['salary-currency'] != 'USD')].dropna()

boxplot1 = alt.Chart(data_for_boxplot).mark_boxplot(extent=0.5
                                                    ).encode(x = alt.X('salary-from:Q'),
                                                            y = alt.Y('area-name:O', sort='-x'),

)

col1, col2 = st.columns(2)
    
with col1:
    st.write("Медиана нижнего порога зарплаты за текущий месяц (с " + 
             start_of_month.strftime('%d.%m.%y') + " по " +
             date.today().strftime('%d.%m.%y') + ")")
    st.altair_chart(barchart1 + text_for_barchart1, use_container_width = True)
with col2:
    st.write("Распределение нижнего порога зарплаты за текущий месяц (с " + 
             start_of_month.strftime('%d.%m.%y') + " по " +
             date.today().strftime('%d.%m.%y') + ")")
    st.altair_chart(boxplot1, use_container_width = True)
 
# Сгруппируем данные по месяцу и найдем медианное значение (среди всех городов)   
data_for_barchart2 = df_data.sort_values(by='published_at_datetime').groupby(
                                                df_data['published_at_datetime'].dt.month_name(),
                                                as_index=True, 
                                                sort=False)['salary-from'].median()
# Преобразуем Series в DataFrame где 2 столбца - (дата, медиана)
data_for_barchart2 = pd.DataFrame(data_for_barchart2,
                                  index=data_for_barchart2.index).reset_index()
barchart2 = alt.Chart(data_for_barchart2).mark_bar(
                                        ).encode(x = alt.X('published_at_datetime:O', sort=None),
                                                 y = alt.Y('salary-from:Q')
                                                    )
# Добавим подписи столбцам
text_for_barchart2 = barchart2.mark_text(
    align='center',
    baseline='middle',
    dy=-10  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='salary-from:Q')

st.altair_chart(barchart2 + text_for_barchart2, use_container_width = True)
# Showing statistics
# salary_from_stats = df_data['salary-from'][(df_data['area-name'] == city_choice) & 
#                         (df_data['salary-currency'] == currency_choice)].describe().to_frame()
# salary_to_stats = df_data['salary-to'][(df_data['area-name'] == city_choice) & 
#                     (df_data['salary-currency'] == currency_choice)].describe().to_frame()

# col1, col2 = st.columns(2)
    
# with col1:
#     st.write("Statistics for Salary-From")
#     st.dataframe(salary_from_stats)
# with col2:
#     st.write("Statistics for Salary-To")
#     st.dataframe(salary_to_stats)




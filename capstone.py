import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def extract_index_from_date(list):
    index = (((list[1]-1991)*4)+(list[0]-3))
    if index >= 0:
        return index
    else: 
        return -1

def extract_date_from_text(str):
    list = []
    q = str[1]
    list.append(int(q))
    year = str[-4:]
    list.append(int(year))
    index = extract_index_from_date(list)
    return index

city_dict = {'Canada': 1,
             'Newfoundland and Labrador': 2,
             'Prince Edward Island': 3,
             'Nova Scotia': 4,
             'New Brunswick': 5,
             'Quebec': 6,
             'Ontario': 7,
             'Manitoba': 8,
             'Saskatchewan': 9,
             'Alberta': 10,
             'British Columbia': 11,
             'Yukon': 12,
             'Northwest Territories': 13,
             'Nunavut': 14}

df = pd.read_csv('data\quarterly_canada_population.csv')
cities = df.columns

st.title("Population of canada")
url = "https://raw.githubusercontent.com/marcopeix/MachineLearningModelDeploymentwithStreamlit/master/12_dashboard_capstone/data/quarterly_canada_population.csv"
st.write("Source table can be found [here](%s)" % url)

with st.expander("See full data table"):
    st.dataframe(df)

with st.form(key="form 1", clear_on_submit=False):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("###### Choose a starting date")
        selectbox1 = st.selectbox("Quarter", key='selectbox 1', options=["Q1", "Q2", "Q3", "Q4"], index=0)
        slider1 = st.slider("Year", key='slider 1', min_value=1991, max_value=2023, value=1991, step=1)
    with col2:
        st.markdown("###### Choose a end date")
        selectbox2 = st.selectbox("Quarters", options=["Q1", "Q2", "Q3", "Q4"], key='selectbox2', index=0)
        slider2 = st.slider("Year", key='slider2' , min_value=1991, max_value=2023, value=2023, step=1)
    with col3:
        st.markdown("###### Choose a location")
        selectbox3 = st.selectbox("Choose a location", options=cities[-14:], key='selectbox3', index=0)
    st.form_submit_button(label="Analyze", type="primary")

start_date = selectbox1 + ' ' + str(slider1)
end_date = selectbox2 + ' ' + str(slider2)
territory = selectbox3

start_row = extract_date_from_text(start_date)
if start_row == -1 :
    st.warning('This is a warning message', icon='⚠️')
end_row =  extract_date_from_text(end_date)
start_date_population = (df.iloc[start_row, city_dict[territory]]).tolist()
end_date_population = (df.iloc[end_row, city_dict[territory]]).tolist()

Population_array = df.loc[start_row:end_row, territory]
time_list = num_list = num_list = list(range(start_row, end_row+1, 1))

tab1, tab2 = st.tabs(['Population change', 'Compare'])
with tab1:
    st.subheader(f"Population change from {start_date} to {end_date}")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label=start_date, value = start_date_population)
        st.metric(label=end_date, value = end_date_population , delta=end_date_population - start_date_population, delta_color="normal")
    with col2:
        fig, ax = plt.subplots()
        ax.plot(Population_array)
        # ax.set_title("title")
        ax.set_xlabel("Time")
        ax.set_ylabel("Population")
        ax.set_xticks([time_list[0], time_list[-1]])
        ax.set_xticklabels([start_date, end_date])
        fig.autofmt_xdate()
        st.pyplot(fig)
with tab2: 
    st.subheader("Compare with other locations")
    multiselect = st.multiselect("Chooe other locations", options=df.columns[1:])
    fig, ax = plt.subplots()
    for city in range(len(multiselect)):
        ax.plot(df.loc[start_row:end_row, multiselect[city]])
    ax.set_xlabel("Time")
    ax.set_ylabel("Population")
    ax.set_xticks([time_list[0], time_list[-1]])
    ax.set_xticklabels([start_date, end_date])
    fig.autofmt_xdate()
    st.pyplot(fig)


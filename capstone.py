import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data\quarterly_canada_population.csv')
cities = df.columns

st.title("Population of canada")
url = "https://raw.githubusercontent.com/marcopeix/MachineLearningModelDeploymentwithStreamlit/master/12_dashboard_capstone/data/quarterly_canada_population.csv"
st.write("Source table can be found [here](%s)" % url)

with st.expander("See full data table"):
    st.dataframe(df)

with st.form(key="form 1", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("###### Choose a starting date")
        selectbox1 = st.selectbox("Quarter", key='selectbox 1', options=["Q1", "Q2", "Q3", "Q4"], index=0)
        slider1 = st.slider("Year", key='slider 1', min_value=1991, max_value=2023, value=1991, step=1)
    with col2:
        st.markdown("###### Choose a end date")
        selectbox2 = st.selectbox("Quarters", options=["Q1", "Q2", "Q3", "Q4"], key='selectbox2', index=0)
        slider2 = st.slider("Year", key='slider2' , min_value=1991, max_value=2023, value=1991, step=1)
    with col3:
        st.markdown("###### Choose a location")
        selectbox3 = st.selectbox("Choose a location", options=cities[-14:], key='selectbox3', index=0)
    st.form_submit_button(label="Analyze", type="primary")

start_date = selectbox1 + ' ' + str(slider1)
end_date = selectbox2 + ' ' + str(slider2)

start_row = 
end_row =  

tab1, tab2 = st.tabs(['Population change', 'Compare'])
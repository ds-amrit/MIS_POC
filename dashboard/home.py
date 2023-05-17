import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt


# Display title
st.title('MIS DASHBOARD')

# Path to data
data_path = r"dashboard/finance_df.csv"

@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    return data
# Load data into df
df = load_data(data_path)
    

st.subheader('Chief KPI: Cash and Carry Retail Stores')

month_order = list(df.month)
c = alt.Chart(df).mark_bar().encode(
                x=alt.X('month', sort=month_order),
                y='# Cash&Carry Retail Stores')
st.altair_chart(c,use_container_width=True)

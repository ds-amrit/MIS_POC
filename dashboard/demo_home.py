# This notebook contains experiment layouts and plot designs for home.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

st.title('MIS DASHBOARD')

data_path = r"notebook\data\MIS 2018\finance_df.csv"
@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    return data
df = load_data(data_path)

st.subheader('Chief KPI: Cash and Carry Retail Stores')

st.bar_chart(df,x='month',y='# Cash&Carry Retail Stores')

def plot_barchart(x,y):
    fig,ax = plt.subplots()
    p = ax.bar(x,y, width=0.5, edgecolor="white", linewidth=0.7,color=['orange','blue','green'])
    ax.bar_label(p)
    return fig

fig = plot_barchart(df['month'], df['# Cash&Carry Retail Stores'])
st.pyplot(fig)


month_order = list(df.month)
c = alt.Chart(df).mark_bar().encode(
                x=alt.X('month', sort=month_order),
                y='# Cash&Carry Retail Stores')
st.altair_chart(c,use_container_width=True)
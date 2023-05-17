# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load Data
data_path = r"dashboard/finance_df.csv"

@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    return data

df = load_data(data_path)

# Page title
st.header("MIS Financial Summary")

# Define feature list for dropdown
feat_list = list(df.columns)[1:-1]

# Define months
months = list(df.month)

# Define Years
year = [2018, 2019, 2020]

# Assigns different colors to varibales in the plot 
color = iter(plt.cm.rainbow(np.linspace(0, 1, len(feat_list))))

def my_plot_c(data,featurelist):  
    '''
        This function returns the figure to plot the 
        list of variables passed in the feature list
    '''
    for f in featurelist:
        c = next(color)
        plt.plot(data[f],color=c, ls = "--", marker='o', ms=6, label=f)
    plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(len(months))),months, rotation='vertical')
    return plt

# Sidebar area
with st.sidebar:
    # Drop down to select year
    st.selectbox('Select Year',year)
    # Drop down to select KPIs
    cols = st.multiselect('Select KPIs to  plot',feat_list,feat_list[-1])
    
# Renders plot of selected cols from 
st.pyplot(my_plot_c(df,cols))
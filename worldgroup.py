from pandas import DataFrame as df
import pandas as pd
import numpy as np
import random
import plotly.express as px
from collections import Counter
import funcs
from funcs import get_countries, determine_age, determine_sex, get_region, create_table, make_map
import streamlit as st

worlddata = pd.read_csv('combined_pop_data2.csv')
worlddata = df(worlddata)

st.set_page_config(page_title = "World Population Simulator", layout = 'wide')

st.sidebar.title("WOrld Population Group Simulator")
group_size = st.sidebar.number_input("Enter group size:", min_value=1, value=10, step=10, max_value = 5000)

if st.sidebar.button("Generate Group"):
    countries, iso_list = get_countries(worlddata, group_size)
    table = create_table(countries, worlddata)

    st.success(f"Simulated {group_size} people based on global population data")

    st.subheader("Population Breakdown Table")
    st.dataframe(table)

    st.subheader('Population Distribution')
    fig = make_map(iso_list)
    st.plotly_chart(fig, use_countainer_width = True)

else:
    st.info("Enter a group size and click 'Generate Group' to begin.")

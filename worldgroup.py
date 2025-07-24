from pandas import DataFrame as df
import pandas as pd
import numpy as np
import random
import plotly.express as px
from collections import Counter
import funcs
from funcs import get_countries, determine_age, determine_sex, get_region, create_table, make_map, make_region_pie, make_group_pie_region, make_group_pie_age, make_age_pie
import streamlit as st

worlddata = pd.read_csv('combined_pop_data2.csv')
worlddata = df(worlddata)

st.set_page_config(page_title = "World Population Simulator", layout = 'wide')

st.sidebar.title("World Population Group Simulator")
group_size = st.sidebar.number_input("Enter group size:", min_value=1, value=10, step=10, max_value = 5000)

if st.sidebar.button("Generate Group"):
    countries, iso_list = get_countries(worlddata, group_size)
    table = create_table(countries, worlddata)
    if group_size == 1:
        st.success('A single person was randomly selected!')
    else:
        st.success(f"A group of {group_size} people was randomly selected from around the world!")

    st.subheader('Population Distribution')
    fig = make_map(iso_list)
    st.plotly_chart(fig, use_container_width = True)

    st.subheader("Population Breakdown Table")
    st.dataframe(table, use_container_width = True)

    st.subheader("")

    st.subheader('Population Composition Comparison')
    left_column, right_column = st.columns(2)

    with left_column:
        pie = make_group_pie_region(table)
        st.plotly_chart(pie, use_container_width = True)

    with right_column:
        pie2 = make_region_pie(worlddata)
        st.plotly_chart(pie2, use_container_width = True)

    with left_column:
        age_pie = make_group_pie_age(table)
        st.plotly_chart(age_pie, use_container_width = True)

    with right_column:
        age_pie2 = make_age_pie()
        st.plotly_chart(age_pie2, use_container_width = True)

else:
    st.info("Enter a group size and click 'Generate Group' to begin.")

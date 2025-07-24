from pandas import DataFrame as df
import pandas as pd
import numpy as np
import random
import plotly.express as px
from collections import Counter
import json

#from .models import globaldata

#Include functions from Jupyter Notebook

def get_countries(data, number):
    #queryset = globaldata.objects.all().values('c_id','iso3','country','pop_prob','male_ratio','median_age','sub15','sub65','senior','region')
    #globaldatadf = pd.DataFrame(queryset)
    citizens = random.choices(data['country'], weights = data['pop_prob'], k = number)
    iso_list = []
    for citizen in citizens:
        row = data.loc[data['country'] == citizen]
        vals = row.values
        iso_list.append(vals[0][1])
    return citizens, iso_list

def determine_age(data, country):
    #age range
    row = data.loc[data['country'] == country]
    vals = row.values
    age_dist = [vals[0][10],vals[0][11],vals[0][12]]
    age_brackets = ['Child (<15)','Adult (16-65)','Senior (65+)']
    age = random.choices(age_brackets, weights = age_dist, k=1)
    return age[0]

def determine_sex(data, country):
    row = data.loc[data['country'] == country]
    vals = row.values
    male_ratio = vals[0][6]
    base = random.random()
    if base <= male_ratio:
        sex = 'Male'
    else:
        sex = 'Female'
    return sex

def get_region(data, country):
    row = data.loc[data['country'] == country]
    vals = row.values
    region = vals[0][13]
    return region

def create_table(country_list, data):
    table = {'Country':[], 'Sex':[], 'Age_Range':[], 'Region':[]}
    for country in country_list:
        table['Country'].append(country)
        table['Sex'].append(determine_sex(data, country))
        table['Age_Range'].append(determine_age(data, country))
        table['Region'].append(get_region(data, country))
        table_results = pd.DataFrame(table)


    #pop_table = pd.DataFrame(table)
    #pop_table_sorted = pop_table.sort_values(by = 'Country')
    return table_results.sort_values(by = 'Country')

def make_map(iso_list):

    counts = Counter(iso_list)
    counts_table = pd.DataFrame.from_dict(counts, orient = 'index', columns = ['count'])
    counts_table.reset_index(inplace=True)
    counts_table.rename(columns={"index": "iso_code"}, inplace = True)
    #counts_table['count'] = counts_table["count"].astype(int)
    #print(counts_table)

    figure = px.choropleth(
        data_frame = counts_table,
        locations = 'iso_code',
        color = 'count',
        color_continuous_scale = 'algae')

    #fig_html = figure.to_html(full_html = False)

    return figure

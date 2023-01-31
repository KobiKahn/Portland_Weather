# IMPORTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# CALCULATE FUNCTIONS
def mean(data):
    total = sum(data)
    m = total / len(data)
    return m
def median(data):
    data.sort()
    if len(data) % 2 == 0:
        m = (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
    else:
        m = data[len(data) // 2]
    return m
def variance(data):
    new_list = [(val - mean(data)) ** 2 for val in data]
    v = mean(new_list)
    return v
def stand_dev(data):
    v = variance(data)
    s = math.sqrt(v)
    return s


# MAKE DICTIONARIES
temp_df = pd.read_csv('Temp.csv')
temp_df.set_index(temp_df['Date'], inplace=True)
pcp_df = pd.read_csv('Precipitation.csv')
pcp_df.set_index(temp_df['Date'], inplace=True)


# temp_df.drop(temp_df[temp_df < 0])
# for col_name in temp_df.iloc[:, 1:]:
temp_df.drop(temp_df[temp_df == -99.0], axis=1)

print(temp_df)

# GRAPH DATA
def graph_base_data(dict, year, month=None):
    if year != 0:
        x_data = list(dict.columns.values)[1:]
        y_data = dict.loc[year][1:]
        plt.title(f'{year}')
    else:
        x_data = dict.iloc[:, 0]
        y_data = dict[month]
        plt.title(f'{month}')

    plt.bar(x_data, y_data)
    plt.xticks(rotation=90)
    plt.show()

# graph_base_data(temp_df, 2022)
# graph_base_data(temp_df, 0, 'February Temp(F)')

# graph_base_data(pcp_df, 2015)
# graph_base_data(pcp_df, 0, 'February Inches')

# print(temp_df.loc[1895])

def find_stats(dict, year, month=None):
    if year != 0:
        for mon in dict.loc[year][1:]:

            print(mon)
        # mean_list =

# find_stats(temp_df, 1895)

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


temp_df[temp_df == -99] = np.NaN     # set all values that meet the condition to NaN
temp_df.dropna(axis = 0, inplace=True)             # remove the rows (axis=1) that have NaN in them

pcp_df[pcp_df == -99] = np.NaN     # set all values that meet the condition to NaN
pcp_df.dropna(axis = 0, inplace=True)             # remove the rows (axis=1) that have NaN in them

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
#
# graph_base_data(temp_df, 2021)
# graph_base_data(temp_df, 0, 'December Temp(F)')

# graph_base_data(pcp_df, 2015)
# graph_base_data(pcp_df, 0, 'February Inches')

# print(temp_df.loc[1895])

def find_stats(dict, year, month=None):
    if year != 0:
        mon_list = []
        for mon in dict.loc[year][1:]:
            mon_list.append(mon)
        mon_mean = mean(mon_list)
        mon_med = median(mon_list)
        mon_std = stand_dev(mon_list)
        mon_max = max(mon_list)
        mon_min = min(mon_list)
        return(mon_mean, mon_med, mon_std, mon_max, mon_min)

temp_dict = {}
for year in temp_df.iloc[:, 0]:
    temp_dict[year] = find_stats(temp_df, year)
print(temp_dict)

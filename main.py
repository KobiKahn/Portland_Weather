# IMPORTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
#

# MAKE DICTIONARIES
temp_df = pd.read_csv('Temp.csv')
temp_df.set_index(temp_df['Date'], inplace=True)
pcp_df = pd.read_csv('Precipitation.csv')
pcp_df.set_index(temp_df['Date'], inplace=True)

# REPLACE NEGATIVES WITH 0
temp_df = temp_df.clip(lower=0)
pcp_df = pcp_df.clip(lower=0)


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

graph_base_data(temp_df, 2022)
graph_base_data(temp_df, 0, 'February Temp(F)')

# graph_base_data(pcp_df, 'Date', 'February Inches')




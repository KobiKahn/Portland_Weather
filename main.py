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
pcp_df.reset_index(temp_df['Date'], inplace=True)

print(temp_df)

# GRAPH DATA
# def graph_base_data(dict, year_range, month):
#
#     fig = plt.figure()
#     x_data = dict[year]
#     y_data = dict[month]
#     plt.bar(x_data, y_data)
#     plt.xticks(rotation=90)
#
#     plt.show()
# #
# graph_base_data(temp_df, , 'January Temp(F)')
# graph_base_data(pcp_df, 'Date', 'February Inches')



# def graph_range(dict, year_range, month_range):








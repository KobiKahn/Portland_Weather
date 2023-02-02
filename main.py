# IMPORTS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


# MAKE PANDA DATAFRAMES
temp_df = pd.read_csv('Temp.csv')
temp_df.set_index(temp_df['Date'], inplace=True)
temp_df.drop(columns='Date', inplace=True)

pcp_df = pd.read_csv('Precipitation.csv')
pcp_df.set_index(pcp_df['Date'], inplace=True)
pcp_df.drop(columns='Date', inplace=True)

# RENAME COLUMNS SO IT IS EASIER
cols = [col[:3] for col in temp_df.columns]
temp_df.columns = cols
pcp_df.columns = cols

# DELETE ERROR ROWS
temp_df[temp_df == -99] = np.NaN     # set all values that meet the condition to NaN
temp_df.dropna(axis = 0, inplace=True)             # remove the rows (axis=1) that have NaN in them
pcp_df[pcp_df == -99] = np.NaN     # set all values that meet the condition to NaN
pcp_df.dropna(axis = 0, inplace=True)             # remove the rows (axis=1) that have NaN in them

# DO TEMP STATS FOR EACH MONTH
temp_df['Mean_M']= round(temp_df.loc[:,'Jan':'Dec'].mean(axis = 1), 1)
temp_df['Med_M'] = round(temp_df.loc[:,'Jan':'Dec'].median(axis = 1), 1)
temp_df['Std_M'] = round(temp_df.loc[:,'Jan':'Dec'].std(axis = 1), 1)
temp_df['Max_M'] = round(temp_df.loc[:,'Jan':'Dec'].max(axis = 1), 1)
temp_df['Min_M'] = round(temp_df.loc[:,'Jan':'Dec'].min(axis = 1), 1)

# DO TEMP STATS FOR EACH YEAR
temp_df['Mean_Y']= round(temp_df.loc[:,'Jan':'Dec'].mean(axis = 0), 1)
temp_df['Med_Y'] = round(temp_df.loc[:,'Jan':'Dec'].median(axis = 0), 1)
temp_df['Std_Y'] = round(temp_df.loc[:,'Jan':'Dec'].std(axis = 0), 1)
temp_df['Max_Y'] = round(temp_df.loc[:,'Jan':'Dec'].max(axis = 0), 1)
temp_df['Min_Y'] = round(temp_df.loc[:,'Jan':'Dec'].min(axis = 0), 1)



# DO PCP STATS
pcp_df['Mean_M'] =round(pcp_df.loc[:,'Jan':'Dec'].mean(axis = 1), 1)
pcp_df['Med_M'] = round(pcp_df.loc[:,'Jan':'Dec'].median(axis = 1), 1)
pcp_df['Std_M'] = round(pcp_df.loc[:,'Jan':'Dec'].std(axis = 1), 1)
pcp_df['Max_M'] = round(pcp_df.loc[:,'Jan':'Dec'].max(axis = 1), 1)
pcp_df['Min_M'] = round(pcp_df.loc[:,'Jan':'Dec'].min(axis = 1), 1)

pcp_df['Mean_Y'] =round(pcp_df.loc[:,'Jan':'Dec'].mean(axis = 0), 1)
pcp_df['Med_Y'] = round(pcp_df.loc[:,'Jan':'Dec'].median(axis = 0), 1)
pcp_df['Std_Y'] = round(pcp_df.loc[:,'Jan':'Dec'].std(axis = 0), 1)
pcp_df['Max_Y'] = round(pcp_df.loc[:,'Jan':'Dec'].max(axis = 0), 1)
pcp_df['Min_Y'] = round(pcp_df.loc[:,'Jan':'Dec'].min(axis = 0), 1)


print(temp_df)

# GRAPH DATA
def graph_base_data(dict, year, month=None):
    if year != 0:
        x_data = list(dict.columns.values)[:-5]
        y_data = round(dict.loc[year][:-5], 1)
        plt.title(f'{year}')
        print(x_data, y_data)
    else:
        x_data = dict.index
        y_data = dict[month]
        plt.title(f'{month}')

    plt.bar(x_data, y_data)
    plt.xticks(rotation=90)
    plt.show()

# graph_base_data(temp_df, 2021)
# graph_base_data(temp_df, 0, 'Dec')

# graph_base_data(pcp_df, 2015)
# graph_base_data(pcp_df, 0, 'Feb')



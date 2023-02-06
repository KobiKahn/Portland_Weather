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
temp_dict = {}
temp_dict['Mean_M'] = list(round(temp_df.loc[:,'Jan':'Dec'].mean(axis=0), 1))
temp_dict['Med_M'] = list(round(temp_df.loc[:,'Jan':'Dec'].median(axis = 0), 1))
temp_dict['Std_M'] = list(round(temp_df.loc[:,'Jan':'Dec'].std(axis = 0), 1))
temp_dict['Max_M'] = list(round(temp_df.loc[:,'Jan':'Dec'].max(axis = 0), 1))
temp_dict['Min_M'] = list(round(temp_df.loc[:,'Jan':'Dec'].min(axis = 0), 1))

# DO TEMP STATS FOR EACH YEAR
temp_dict['Mean_Y'] = list(round(temp_df.loc[:,'Jan':'Dec'].mean(axis=1), 1))
temp_dict['Med_Y'] = list(round(temp_df.loc[:,'Jan':'Dec'].median(axis = 1), 1))
temp_dict['Std_Y'] = list(round(temp_df.loc[:,'Jan':'Dec'].std(axis = 1), 1))
temp_dict['Max_Y'] = list(round(temp_df.loc[:,'Jan':'Dec'].max(axis = 1), 1))
temp_dict['Min_Y'] = list(round(temp_df.loc[:,'Jan':'Dec'].min(axis = 1), 1))


#PRCP STATS FOR EACH MONTH
pcp_dict = {}
pcp_dict['Mean_M'] = list(round(pcp_df.loc[:,'Jan':'Dec'].mean(axis=0), 1))
pcp_dict['Med_M'] = list(round(pcp_df.loc[:,'Jan':'Dec'].median(axis = 0), 1))
pcp_dict['Std_M'] = list(round(pcp_df.loc[:,'Jan':'Dec'].std(axis = 0), 1))
pcp_dict['Max_M'] = list(round(pcp_df.loc[:,'Jan':'Dec'].max(axis = 0), 1))
pcp_dict['Min_M'] = list(round(pcp_df.loc[:,'Jan':'Dec'].min(axis = 0), 1))

# DO PRCP STATS FOR EACH YEAR
pcp_dict['Mean_Y'] = list(round(pcp_df.loc[:,'Jan':'Dec'].mean(axis=1), 1))
pcp_dict['Med_Y'] = list(round(pcp_df.loc[:,'Jan':'Dec'].median(axis = 1), 1))
pcp_dict['Std_Y'] = list(round(pcp_df.loc[:,'Jan':'Dec'].std(axis = 1), 1))
pcp_dict['Max_Y'] = list(round(pcp_df.loc[:,'Jan':'Dec'].max(axis = 1), 1))
pcp_dict['Min_Y'] = list(round(pcp_df.loc[:,'Jan':'Dec'].min(axis = 1), 1))

# print(temp_dict)
# print()
# print(temp_dict['Med_M'])


# GRAPH DATA
def graph_base_data(title, df, year, month=None):
    if year != 0:
        x_data = list(df.loc[0:1,'Jan':'Dec'])
        y_data = round(df.loc[year][:], 1)
    else:
        x_data = df.index
        y_data = df[month]

    plt.title(title)
    plt.bar(x_data, y_data)
    plt.xticks(rotation=90)
    plt.show()


# graph_base_data('Temps for 2021', temp_df, 2021)
# graph_base_data('Temps for December', temp_df, 0, 'Dec')
# #
# graph_base_data('PRCP for 2015', pcp_df, 2015)
# graph_base_data('PRCP for Feb',pcp_df, 0, 'Feb')


def graph_stats(dict, title, option=0):
    if option==0:
        x_data = temp_df.index

        mean_list = dict['Mean_Y']
        med_list = dict['Med_Y']
        min_list = dict['Min_Y']
        max_list = dict['Max_Y']

        plt.bar(x_data, max_list, color='red')
        plt.bar(x_data, med_list, color='green')
        plt.bar(x_data, mean_list, color='black')
        plt.bar(x_data, min_list, color='blue')
        plt.legend(['MAX', 'MED', 'MEAN', 'MIN'])

    elif option==1:
        x_data = list(temp_df.loc[0:1,'Jan':'Dec'])



    plt.title(title)
    plt.show()

graph_stats(temp_dict, 'STATS FOR ALL YEARS')
# print(temp_dict['Med'])
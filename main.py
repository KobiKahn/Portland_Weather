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
temp_dict['Max_M'] = list(temp_df.loc[:,'Jan':'Dec'].max(axis = 0))
temp_dict['Min_M'] = list(temp_df.loc[:,'Jan':'Dec'].min(axis = 0))

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
pcp_dict['Max_M'] = list(pcp_df.loc[:,'Jan':'Dec'].max(axis = 0))
pcp_dict['Min_M'] = list(pcp_df.loc[:,'Jan':'Dec'].min(axis = 0))

# DO PRCP STATS FOR EACH YEAR
pcp_dict['Mean_Y'] = list(round(pcp_df.loc[:,'Jan':'Dec'].mean(axis=1), 1))
pcp_dict['Med_Y'] = list(round(pcp_df.loc[:,'Jan':'Dec'].median(axis = 1), 1))
pcp_dict['Std_Y'] = list(round(pcp_df.loc[:,'Jan':'Dec'].std(axis = 1), 1))
pcp_dict['Max_Y'] = list(pcp_df.loc[:,'Jan':'Dec'].max(axis = 1))
pcp_dict['Min_Y'] = list(pcp_df.loc[:,'Jan':'Dec'].min(axis = 1))



########### FUNCTIONS ############
########### FUNCTIONS ############
########### FUNCTIONS ############
########### FUNCTIONS ############

def cal_corr(list1, list2, option=0):
    if len(list1) == len(list2):
        i = -1
        prod_list = []
        min_sqr1 = []
        min_sqr2 = []
        for val in list1:
            i += 1
            prod_list.append(list1[i] * list2[i])
            min_sqr1.append(list1[i] ** 2)
            min_sqr2.append(list2[i] ** 2)

        numerator = ((len(list1) * sum(prod_list)) - (sum(list1) * sum(list2)))
        denominator = (math.sqrt(len(list1) * sum(min_sqr1) - sum(list1) ** 2) * math.sqrt(len(list2) * sum(min_sqr2) - sum(list2) ** 2))
        denominator = denominator.real
        correlation = numerator / denominator
        if option == 0:
            return (correlation)
        elif option == 1:
            return (sum(list1), sum(list2), sum(prod_list), sum(min_sqr1), len(list1))
    else:
        print('ERROR LISTS ARE NOT THE SAME LENGTH CANT COMPUTE')
        return False



def LSC(list1, list2):
    x_sum, y_sum, prod_sum, xsqr_sum, list_len = cal_corr(list1, list2, 1)
    matrix1 = [[xsqr_sum, x_sum], [x_sum, list_len]]
    matrix2 = [prod_sum, y_sum]
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    inv_mat1 = np.linalg.inv(matrix1)
    solution = np.dot(inv_mat1, matrix2)
    # a = slope b = y int
    a = solution[0]
    b = solution[1]
    return(a, b)

# MOVING FILTERS
def weight_avg_fil(f_list, w_len):
    output = []
    w_list = [1 for i in range(w_len)]
    for i in range(len(f_list)):
        if i <= len(f_list) - w_len:
            min_list = []
            min_list2 = []
            for j in range(w_len):
                min_list.append(f_list[i + j])
            for k in range(w_len):
                min_list2.append(min_list[k] * w_list[k])
            output.append(sum(min_list2)/sum(w_list))
    return(output)

# FIND ESTIMATES OF FUTURE TIMES
def calc_future(m, b, year):
    y = m * (year) + b
    return(y)

# GRAPH DATA
def graph_avg_weight(title, vals, df, w_len, option=0):
    x_data = df.index
    y_data = vals
    avg_list = weight_avg_fil(y_data, w_len)
    mov_x_data = df.index.values[9:-10]

    if option == 0:
        LSC_avg = avg_list[-30:-10]
        LSC_x = mov_x_data[-30:-10]
    else:
        LSC_avg = avg_list[-20:-10]
        LSC_x = mov_x_data[-20:-10]

    slope, y_int = LSC(LSC_x, LSC_avg)

    plt.plot(x_data, y_data)
    plt.plot(mov_x_data, avg_list, color='r')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.show()
    return(slope, y_int)


def graph_base_data(title, df, year, month=None):
    if year != 0:
        x_data = list(df.loc[0:1,'Jan':'Dec'])
        y_data = round(df.loc[year][:], 1)
        plt.bar(x_data, y_data)

    else:
        x_data = df.index
        y_data = df[month]
        plt.plot(x_data, y_data)

    plt.title(title)
    plt.xticks(rotation=90)
    plt.show()

def graph_stats(dict, title, df, option=0):
    if option==0:
        x_data = df.index

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
        counter = 0
        x_data = list(df.loc[0:1,'Jan':'Dec'])
        y_max = []
        y_min = []
        # GET MAX AND MIN LISTS
        for month in x_data:
            y_max.append(list(df.loc[df[month] == dict['Max_M'][counter]].index))
            y_min.append(list(df.loc[df[month] == dict['Min_M'][counter]].index))
            counter += 1

        # CLEAN UP MAX LIST
        counter = 0
        for date in y_max:
            if len(date) > 1:
                y_max[counter] = max(date)
            counter += 1
        # CLEAN UP MIN LIST
        counter = 0
        for date in y_min:
            if len(date) > 1:
                y_min[counter] = min(date)
            counter += 1

        # FIX STRINGS SO NO BRACKETS
        y_max = [i.strip('[]') if type(i) == str else str(i) for i in y_max]
        y_max = [i.strip('[]') for i in y_max]
        y_max = [int(i) for i in y_max]

        y_min = [i.strip('[]') if type(i) == str else str(i) for i in y_min]
        y_min = [i.strip('[]') for i in y_min]
        y_min = [int(i) for i in y_min]



        plt.ylim(1890, 2030)
        plt.bar(x_data, y_max, .5, color='pink')
        plt.bar(x_data, y_min, .3, color='aquamarine')
        plt.legend(['MAX', 'MIN'])

    plt.title(title)
    plt.show()




########### CALLING THE FUNCTIONS ############

temp_avg_mean = weight_avg_fil(temp_dict['Mean_Y'], 20)
pcp_avg_mean = weight_avg_fil(pcp_dict['Mean_Y'], 20)

mov_x_data = temp_df.index.values[9:-10]
temp_mean_df = pd.DataFrame(temp_avg_mean)
temp_mean_df.set_index(mov_x_data, inplace=True)


temp_span1 = temp_mean_df.loc[1904:1942].values.tolist()
temp_span2 = temp_mean_df.loc[1943:1979].values.tolist()
temp_span3 = temp_mean_df.loc[1980:].values.tolist()
temp_span1 = [i.strip('[]') if type(i) == str else str(i) for i in temp_span1]
temp_span1 = [i.strip('[]') for i in temp_span1]
temp_span1 = [float(i) for i in temp_span1]
temp_span2 = [i.strip('[]') if type(i) == str else str(i) for i in temp_span2]
temp_span2 = [i.strip('[]') for i in temp_span2]
temp_span2 = [float(i) for i in temp_span2]
temp_span3 = [i.strip('[]') if type(i) == str else str(i) for i in temp_span3]
temp_span3 = [i.strip('[]') for i in temp_span3]
temp_span3 = [float(i) for i in temp_span3]

year_span1 = temp_mean_df.loc[1904:1942].index.tolist()
year_span2 = temp_mean_df.loc[1943:1979].index.tolist()
year_span3 = temp_mean_df.loc[1980:].index.tolist()

correlation1 = cal_corr(temp_span1, year_span1)
correlation2 = cal_corr(temp_span2, year_span2)
correlation3 = cal_corr(temp_span3, year_span3)

temp_prcp_corr = cal_corr(temp_avg_mean, pcp_avg_mean)

print(correlation1)
print(correlation2)
print(correlation3)
print(temp_prcp_corr)

# slope, y_int = graph_avg_weight('TEMP MEAN FOR EVERY YEAR', temp_dict['Mean_Y'], temp_df, 20)
# graph_avg_weight('TEMP MED FOR EVERY YEAR', temp_dict['Med_Y'], temp_df, 20)
# graph_avg_weight('TEMP MIN FOR EVERY YEAR', temp_dict['Min_Y'], temp_df, 20)
# graph_avg_weight('TEMP MAX FOR EVERY YEAR', temp_dict['Max_Y'], temp_df, 20)

# graph_avg_weight('PCRP MEAN FOR EVERY YEAR', pcp_dict['Mean_Y'], pcp_df, 20, 1)
# graph_avg_weight('PCRP MED FOR EVERY YEAR', pcp_dict['Med_Y'], pcp_df, 20, 1)
# graph_avg_weight('PCRP MIN FOR EVERY YEAR', pcp_dict['Min_Y'], pcp_df, 20, 1)
# graph_avg_weight('PCRP MAX FOR EVERY YEAR', pcp_dict['Max_Y'], pcp_df, 20, 1)

# est_2030 = calc_future(slope, y_int, 2030)
# est_2035 = calc_future(slope, y_int, 2035)
# print(est_2025, est_2030, est_2035)
# est_2025 = calc_future(slope, y_int, 2025)


# graph_base_data('Temps for 2021', temp_df, 2021)
# graph_base_data('Temps for Jan', temp_df, 0, 'Jan')
# graph_base_data('PRCP for 2015', pcp_df, 2015)
# graph_base_data('PRCP for Feb',pcp_df, 0, 'Feb')


# graph_stats(temp_dict, 'STATS FOR ALL TEMP YEARS', temp_df)
# graph_stats(temp_dict, 'MAX AND MIN FOR TEMP MONTHS', temp_df, 1)
# graph_stats(pcp_dict, 'STATS FOR ALL PRCP YEARS', pcp_df)
# graph_stats(pcp_dict, 'MAX AND MIN FOR PRCP MONTHS', pcp_df, 1)
# print(temp_dict)





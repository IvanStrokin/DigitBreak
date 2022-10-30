import pandas as pd


def create_reformat_data(data_set):
    data = []
    data_reformat = []
    for i in range(len(data_set['Data'])):
        data.append(data_set['Data'][i].split(', '))
        if '[' in data[i][0]:
            data[i][0] = data[i][0][1:]
        if ']' in data[i][-1]:
            data[i][-1] = data[i][-1][:-1]
        data_person = [int(elem) for elem in data[i]]
        data_reformat.append(data_person)
    return data_reformat


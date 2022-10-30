from calculation_func import  get_param
from reformat_data import create_reformat_data
from pandas import ExcelWriter
import pandas as pd


def create_data_set(data_set, file_name):
    data_reformat = create_reformat_data(data_set)
    data = []
    print(data_set.columns)
    for index, row in data_set.iterrows():
        result = get_param(data_reformat[index])
        result.append(row.Presentation)
        data.append({'Частота': result[0], 'Амплитуда': result[1], 'Смещение': result[2], 'Повторение': result[3]})
    df_data = pd.DataFrame(data)
    writer = ExcelWriter(f'{file_name}.xlsx')
    df_data.to_excel(writer, f'{file_name}.xlsx')
    writer.save()

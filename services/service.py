import pandas
from pandas import DataFrame

from db.connect import DataBase


def transform_data(df: DataFrame) -> list[tuple]:
    data = []
    for i in df.iloc:
        data.append((i['company'], 'data1', 'Qliq', int(i['data_1_1']), int(i['data_1_5'])))
        data.append((i['company'], 'data2', 'Qoil', int(i['data_2_2']), int(i['data_2_6'])))
        data.append((i['company'], 'data1', 'Qliq', int(i['data_1_3']), int(i['data_1_7'])))
        data.append((i['company'], 'data2', 'Qoil', int(i['data_2_4']), int(i['data_2_8'])))
    return data


def parse_excel(filename):
    df = pandas.read_excel(filename, skiprows=3,
                           names=['id', 'company', 'data_1_1', 'data_2_2', 'data_1_3', 'data_2_4', 'data_1_5',
                                  'data_2_6', 'data_1_7', 'data_2_8'])
    return df


def save_data(df: DataFrame):
    data = transform_data(df)
    with DataBase('test_db') as db:
        db.execute_query("Insert into data (company_id, date_type, q_type, fact, forecast) VALUES(?,?,?,?,?)", data)

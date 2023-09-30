import csv
import pandas as pd


def extract_csv(csv_file):
    df = pd.read_csv(csv_file, sep=';')

    headers = df.columns.tolist()
    values = df.values.tolist()

    return headers, values


def csv_to_dict(csv_file, index_col=0, separator=';'):
    df = pd.read_csv(csv_file, sep=';')
    data_dict = df.to_dict(orient="records")
    return data_dict



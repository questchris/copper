import os
import io
import json
import pickle

import copper
import pandas as pd


def load(file_path):
    '''
    Loads a pickled dataset
    '''
    if len(file_path.split('.')) == 1:
        file_path = file_path + '.dataset'

    if file_path.endswith('dataset'):
        f = os.path.join(copper.project.data, file_path)
        pkl_file = open(f, 'rb')
        return pickle.load(pkl_file)

def save(dataset, name):
    f = os.path.join(copper.project.data, name + '.dataset')
    output = open(f, 'wb')
    pickle.dump(dataset, output)
    output.close()

def export(data, name, format='csv'):
    if type(data) is copper.Dataset:
        df = data.frame
    else:
        df = data

    if format == 'csv':
        fpath = os.path.join(copper.project.exported, name + '.csv')
        df.to_csv(fpath, encoding='utf-8')
    elif format == 'json':
        fpath = os.path.join(copper.project.exported, name + '.json')
        with io.open(fpath, 'w', encoding='utf-8') as outfile:
            json.dumps(df_to_json(df), outfile)

def df_to_json(df):
    d = [
            dict([(colname, row[i]) for i ,colname in enumerate(df.columns)])
                    for row in df.values]
    return json.dumps(d)

def read_csv(file_path, **args):
    file_path = os.path.join(copper.project.data, file_path)
    return pd.read_csv(file_path, **args)

import pandas as pd

def list_columns(dataframe):
        cols = dataframe.columns
        for i in range(len(cols)):
            print(f'{i+1}. {cols[i]}')
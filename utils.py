import numpy as np
import pandas as pd



def extract_data(file, header, index_col, dtype, converters, skiprows, parse_dates):

    '''
    Purpose:
        -Extracts data from Excel File and imports as Pandas DataFrame
    Inputs:
        -file: path to excel file (.csv)
    Outputs:
        -COVID19
    '''

    #Read CSV File
    data = pd.read_csv(filepath_or_buffer = file, header = header, index_col = index_col, dtype = dtype, converters= converters,
                       skiprows = skiprows, parse_dates = parse_dates)
    #Resort By Date
    #data_resorted = data.sort_values(by=['Date'])

    return data

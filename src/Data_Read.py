#  Data_Read.py:
def Read_n_Clean_csv_NaN_columns(URL_file: str, empty_DataFrame):
    '''
    To use:
    import Data_Read
    Read_n_Clean_csv_NaN_columns(URL_file: str, empty_DataFrame)

    imports URL_file, and drops in-place empty (NaN) columns
    '''

    import pandas as pd

    data_df_pd = pd.read_csv(URL_file)

    #  Check for column population with Nan's
    '''
    (data_rows, data_columns) = data_df_pd.shape
    cols_2_drop = []
    cols_2_drop_counter = 0
    for i in data_df_pd.columns:
        if data_df_pd[i].isna().sum() == data_rows:  # not a single data row all are NaN's
            cols_2_drop.append(i)  # add NaN column to drop
            print(f'Column "{i}" has no data rows and will be dropped')
            cols_2_drop_counter += 1
    print(
        f'Total of {cols_2_drop_counter} columns of are dropped as all NaNs of {data_columns} total')
    print(f'Dropped columns are : {cols_2_drop}')

    # Actual purge of empty columns (only NaNs)
    data_df_pd.drop(columns=cols_2_drop, inplace=True)
    '''

    #  Print remaining columns
    # print(f'Remaining columns are: {data_df_pd.head()}')
    # data_df_pd.info() # displays non-null counts

    return data_df_pd  # empty DataFrame is passed in to enable return of the resulting DF



def Clean_2col_df_NaN_rows(two_column_DataFrame):
    '''
    Receive two columns data frame, remove rows with
    NaNs in ether column
    '''
    # Ref: https://datatofish.com/rows-with-nan-pandas-dataframe/
    # Ref: https://datatofish.com/dropna/
    df_no_Nans = two_column_DataFrame.dropna()

    return df_no_Nans  # empty DataFrame is passed in to enable return of the resulting DF

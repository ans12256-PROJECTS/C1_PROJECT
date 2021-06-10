def Read_n_Clean_csv_NaN_columns(URL_file: str, empty_DataFrame):
    '''
    To use:
    import Data_Read
    Read_n_Clean_csv_NaN_columns(URL_file: str, empty_DataFrame)

    imports URL_file, and drops in-place empty (NaN) columns
    '''

    import pandas as pd

    data_df_pd = pd.read_csv(URL_file)
    # dtype = {'speed': int, 'period': str, 'warning': str, 'pair': int}
    # to clean at read time:
    # usecols: int | str | Sequence | None = ...,
    # df.to_csv('my_pandas_dataframe.csv', index=False)

    # explore data
    # Pandas DataFrame is easier to handle

    # print(data_df_pd.head(5))  # First 5 rows
    # Show headers as a column
    # print(data_df_pd.columns)
    # print(data_df_pd.shape)  # .describe, .size, .head)

    # data_df_pd.size

    # Data Cleaning / wrangling
    # ref: https://realpython.com/python-data-cleaning-numpy-pandas/
    # To drop unnecessary columns:
    # to_drop = ['Edition Statement',
    #    ...            'Corporate Author',
    #    ...            'Corporate Contributors',
    #    ...            'Former owner',
    #    ...            'Engraver',
    #    ...            'Contributors',
    #    ...            'Issuance type',
    #    ...            'Shelfmarks']

    # >> > df.drop(to_drop, inplace=True, axis=1)
    # df.drop(columns=to_drop, inplace=True)

    # https://datatofish.com/count-nan-pandas-dataframe/
    # (1) Count NaN values under a single DataFrame column:
    # df['column name'].isna().sum()
    # (2) Count NaN values under an entire DataFrame:
    # df.isna().sum().sum()
    # (3) Count NaN values across a single DataFrame row:
    # df.loc[[index value]].isna().sum().sum()

    #  Check for column population with Nan's
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

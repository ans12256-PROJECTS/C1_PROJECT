# Data_EDA.py:
def read_data(DataFrame=''):
    # Separate into a subroutine to pass df already in memory to avoid
    # re-read

    #  call data import script
    # Data_Read.py stored in the same dir 'scr'; Imports and cleans empty columns

    #     from datetime import datetime
    #     import df_2_plot        # Alexey's routine to plot scatter plot of Series(counts) vs index (years)
    #     import logging          # to dump diagnostics in src/output.txt
    #     import Data_Read        # Alexey's routine to read data, clean empty columns
    #     import pandas as pd
    #     import matplotlib.pyplot as plt
    #     import numpy as np

    # URL_file = 'https://data.wa.gov/resource/auvb-4rvk.csv'
    # 'https: // data.wa.gov/api/views/auvb-4rvk/rows.csv?accessType = DOWNLOAD'
    URL_file = '../data/WDFW-Coded_Wire_Tag_Fish_Recoveries.csv'

    try:
        df.head
        # print('df pandas DataFrame DOES exist, skipping reading again.')
        # catch when df is None
        # pass
    except AttributeError:   # Neah unlikely to happen
        print('df pandas DataFrame DOES exists, but is None.')
    # catch when it hasn't even been defined
    except UnboundLocalError: # local variable 'df' referenced before assignment
        print('NO df pandas DataFrame exists, reading data branch')
        # Empty DataFrame is passed as a parameter to get back one with data
        # df = Data_Read.Read_n_Clean_csv_NaN_columns(URL_file, pd.DataFrame())
        df = Read_n_Clean_csv_NaN_columns(URL_file, pd.DataFrame())
    except NameError:  # df does not exist => first run proceed to read data
        print('NO df pandas DataFrame exists, reading data branch')
        # Empty DataFrame is passed as a parameter to get back one with data
        # df = Data_Read.Read_n_Clean_csv_NaN_columns(URL_file, pd.DataFrame())
        df = Read_n_Clean_csv_NaN_columns(URL_file, pd.DataFrame())



    #     import matplotlib.pyplot as plt

    # x = df['returnyear']
    # y = df['species']
    # fig, axs = plt.subplots(figsize=(5, 10))
    # axs.scatter(x,y)

    # plt.show()  # Command required in VS Code to show figure
    #  Time series returnyear

    #  Check unique values
    # df['Species'].unique()
    # In[4]: df['Species'].unique()
    # Out[4]:
    # array(['Chinook', 'Coho', 'Chum', 'Steelhead', 'Pink', 'Sockeye',
    #        'Unknown', 'Atlantic Salmon', 'Cutthroat'], dtype=object)

    # /Users/alexey_imac/opt/anaconda3/lib/python3.8/site-packages/IPython/core/interactiveshell.py: 2757: DtypeWarning: Columns(1, 3, 9, 15, 18, 21, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37) have mixed types.Specify dtype option on import or set low_memory = False.
    # py3compat.execfile(
    #     Total of 0 columns of are dropped as all NaNs of 43 total
    #     Dropped columns are: []

    # https: // stackoverflow.com/questions/29376026/find-mixed-types-in-pandas-columns
    # Mixed Data Types
    # Find columns that change type:
    # for col in df.columns:
    #     weird = (df[[col]].applymap(type) !=
    #              df[[col]].iloc[0].apply(type)).any(axis=1)
    #     if len(df[weird]) > 0:
    #         print(col)

    # Verified Date
    # Run
    # Location Name
    # PSC Code
    # Location Code
    # Recovery Gear Type
    # PSNET Recovery Gear Type
    # Recovery Date
    # Sample Type
    # Tag Code
    # Sex
    # Fisher Type
    # Maturity
    # Project Fish Number
    # Scale Card Number
    # Otolith Number
    # First Release Date
    # Last Release Date
    # Release Site
    # Rearing Hatchery
    # Stock Name
    # Release Run
    # Release Agency
    # Bag Label Comments
    # Fish Comments
    # Release Comments

    # EDA
    # df.columns  # see columns names
    # df['Species'].unique()
    # df['Return Year'].unique()
    # df.dtypes  # check the data type of all columns
    # Return Year                         int64
    # Verified Date                      object
    # Species                            object
    # Run                                object
    # Location Name                      object
    # PSC Code                           object
    # Location Code                      object
    # Process Project                    object
    # Recovery Gear Type                 object
    # PSNET Recovery Gear Type           object
    # Bag Label                          object
    # Head Number                         int64
    # Recovery Date                      object
    # Sample Type                        object
    # Tag Result                         object
    # Tag Code                           object
    # Fork Length(cm)                  float64
    # Sex                                object
    # Fisher Type                        object
    # Maturity                           object
    # Mark                               object
    # Project Fish Number                object
    # Sample Card Number                float64
    # Sample Card Record Number         float64
    # Scale Card Number                  object
    # Scale Card Line Number            float64
    # Otolith Number                     object
    # Brood Year                        float64
    # First Release Date                 object
    # Last Release Date                  object
    # Release Site                       object
    # Rearing Hatchery                   object
    # Stock Name                         object
    # Release Run                        object
    # Release Agency                     object
    # Bag Label Comments                 object
    # Fish Comments                      object
    # Release Comments                   object
    # Released Tag Adclip Count         float64
    # Released Tag No Adclip Count      float64
    # Released Untag Adclip Count       float64
    # Released Untag No Adclip Count    float64
    # InternalId                          int64
    # dtype: object

    # Check for weird data types:
    # for i in df.columns:
    #     print(f'Unique values in column {i}, {df[i].unique()}')

    # for i in df.columns:
    #     logging.info(f'Unique values in column {i}, {df[i].unique()}')

    #  https://www.askpython.com/python/built-in-methods/python-print-to-file
    #  dump exploratory outputs to file:
    # using Python’s logging module to print to the file
    # import logging
    # Create the file
    # and output every level since 'DEBUG' is used
    # and remove all headers in the output
    # using empty format=''
    # logging.basicConfig(filename='output.txt', level=logging.DEBUG, format='')

    # logging.debug('Hi')
    # logging.info('Hello from AskPython')
    # logging.warning('exit')

    #  Clean rows where either of two (2) columns has a NaN to prepare for plot
    #  plt_2_cols_cleaned = Data_Read.Clean_2col_df_NaN_rows(df[['Return Year', 'Species']])
    plt_2_cols_cleaned = Clean_2col_df_NaN_rows(df[['Return Year', 'Species']])



    # import df_2_plot
    # df_2_plot.plot_two_cols(plt_2_cols_cleaned, params=0)
    # df2c becomes a series df2c.index
    df2c = plt_2_cols_cleaned.groupby(
        ['Return Year', 'Species']).size()  # No of all records per year
    # df_2_plot.plot_two_cols(df2c, 'Return Year', 'Total records')

    # DataFrame
    # df_tmp = pd.DataFrame({'count': plt_2_cols_cleaned.groupby(
    #         ['Return Year', 'Species']).size()})


    #  In[22]: df_tmp.head
    # Out[22]:
    # <bound method NDFrame.head of
    # Return Year Species    count
    # 1976        Chinook    14482
    #             Chum           5
    #             Coho       21934
    # 1977        Chinook     9913
    #             Chum           4
    # ...                      ...
    # 2020        Coho       14245
    #             Steelhead     12
    #             Unknown        4
    # 2021        Chinook       33
    #             Steelhead      1

    # [211 rows x 1 columns] >

    # https: // pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
    # https: // pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
    # df2c.loc[("Return Year", "Chinook")]
    # df2c.loc[("Chinook")]
    # df2c.loc["Chinook"]
    # health_df[health_df['Country Code'] == 'USA'][health_df['Indicator Name']
    #                                               == 'Age at first marriage, female'].iloc[:, 4:]

    # Ref. https://appdividend.com/2020/10/27/how-to-convert-python-string-to-date/
    # from datetime import datetime
    # date_str = '05/09/2019'

    # dto = datetime.strptime(date_str, '%m/%d/%Y').date()
    # print(type(dto))  # <class 'datetime.date'>
    # print(dto)  # 2019-05-09

    #  Data extraction
    df_tmp = df2c.reset_index()  # each species gets individual year
    df_tmp.rename(columns = {0:'Total Count'}, inplace = True) # summary column had name 0
    # df_tmp[df_tmp['Species'] == 'Coho'] # Year, Coho, count
    # df_2_plot = df_tmp[df_tmp['Species'] == 'Coho']
    # df_2_plot.head()
    # type(df_2_plot) # pandas.core.frame.DataFrame
    # df_2_plot.shape # (45, 3) 1976 ~2021, Year, Species, Count
    # df_2_plot.iloc[:,0]  # extracts year
    # df_2_plot.iloc[0,1] # 'Coho'

    # initialize figure
    fig, axs = plt.subplots(figsize=(15, 10))

    #     df_2_plot.plot_two_cols(
    #         df_tmp[df_tmp['Species'] == 'Coho'],
    plot_two_cols(
        df_tmp[df_tmp['Species'] == 'Coho'],
        y_lbl_in='Fish count', col_in='red', fig_in = fig,
        axs_in = axs, label_in = 'Coho', plt_type='s')

    #     df_2_plot.plot_two_cols(
    #         df_tmp[df_tmp['Species'] == 'Chinook'],
    plot_two_cols(
        df_tmp[df_tmp['Species'] == 'Chinook'],
        y_lbl_in='Fish count', col_in='blue', fig_in=fig,
        axs_in=axs, label_in = 'Chinook', plt_type='s')

    axs.legend(loc='upper right')  # [] required, otherwise single character as string is iterable
    axs.grid()


    plt.show()
    return df; # to make df available for main memory

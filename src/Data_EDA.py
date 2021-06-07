#  call data import script
# Data_Read.py stored in the same dir 'scr'; Imports and cleans empty columns

import Data_Read
import pandas as pd

URL_file = 'https://data.wa.gov/resource/auvb-4rvk.csv'
# Empty DataFrame is passed as a parameter to get back one with data
df = Data_Read.Read_n_Clean_csv_NaN_columns(URL_file, pd.DataFrame())

# df2.loc[: , "2005"] extract a column
#  time series by 'returnyear'
# EDA plot a few graphs against returnyear, maybe another subroutine

import matplotlib.pyplot as plt

x = df['returnyear']
y = df['species']
fig, axs = plt.subplots(figsize=(5, 10))
axs.scatter(x,y)

plt.show()  # Command required in VS Code to show figure
#  Time series returnyear

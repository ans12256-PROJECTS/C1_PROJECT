# WDFW-Coded Wire Tag Fish Recoveries

[data: 3.25M rows, 43 columns](https://data.wa.gov/Natural-Resources-Environment/WDFW-Coded-Wire-Tag-Fish-Recoveries/auvb-4rvk/data)

# Data correlation Pacific temperature vs Fish numbers
![Data Correlation](img/Salmon_Returns_n_El_Ninos.png)

# Hypothesis Testing
* Warm years do not affect fish return numbers
Ho = Warm years (delta T > threshould) do not affect fish returns
![Ho Testing](img/Ho_Hypothesis_Testing.png)

# Code Structure (Python)
## Reading / Cleaning subroutine
* [Data_Read.py](src/Data_Read.py)

## Visualization Subroutines
* [Data_EDA.py](src/Data_EDA.py)
* [df_2_plot.py](src/df_2_plot.py)
* [font_sizes.py](src/font_sizes.py)
* [ocean_temps.py](src/ocean_temps.py)


## Statistical Analysis Subroutines
* [calculate_t_test.py](src/calculate_t_test.py)

## Jupyter Mess
* [WDFW_visualizations.ipynb](notebooks/WDFW_visualizations.ipynb)

# Links, References
* [Presentation](https://docs.google.com/presentation/d/1alJ6Bj4SXtmc_QRkXHZ18kGtS4M2df1byW4_aMRXEak/edit#slide=id.gdf56791012_1_15)
* [Primary Data WDFW fish Recovery](https://data.wa.gov/Natural-Resources-Environment/WDFW-Coded-Wire-Tag-Fish-Recoveries/auvb-4rvk)
* [Secondary Data El Niño/La Niña](https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php)

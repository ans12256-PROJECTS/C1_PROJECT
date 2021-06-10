# Subroutine to plot two columns
def plot_two_cols(df_2_plot, y_lbl_in: str, col_in: str, fig_in, axs_in):
    '''
    plot_two_cols(df_2_plot, y_lbl_in: str, col_in: str)
    plot scatter plot of a panda three columns dataframe
    first column - years, second - species, third - counts
    parameters can be passed later

    df_2_plot.head() is passed in
        Return Year Species      0
    2          1976    Coho  21934
    5          1977    Coho  25826
    x = df_2_plot.iloc[:,0]  # years
    y = df_2_plot.iloc[:,2]  # counts
    x_lbl = df_2_plot.columns[0]
    y_lbl = df_2_plot.iloc[0,1] + ' salmon'

    '''
    # import matplotlib.pyplot as plt   # supposed to be done in main

    # fig, axs = plt.subplots(figsize=(15, 10)) # call in main to enable overlap

    x = df_2_plot.iloc[:, 0]  # years
    y = df_2_plot.iloc[:, 2]  # fish counts
    x_lbl = df_2_plot.columns[0]  # 'Return Year'
    y_lbl = y_lbl_in  # whatever is passed into the function
    # 1st row of middle ('Species') column
    g_legend = df_2_plot.iloc[0, 1]  # 'Coho'

    axs_in.scatter(x, y, color=col_in)
    axs_in.set_xlabel(x_lbl)
    axs_in.set_ylabel(y_lbl)
    # [] required, otherwise single character as string is iterable
    axs_in.legend([g_legend])
    axs_in.grid()
    # font sizes, etc. later
    # plt.show()   # perform in main
    pass

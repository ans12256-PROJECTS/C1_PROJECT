def font_sizes(font_size: int, f_legend: int):  # font_size = 10 ~ default
    '''
    font_sizes(font_size: int, f_legend: int)
    reset all graphs fonts to font_size.
    More fine-tuning is available individually
    if f_legend is passed, individual adjustment is performed
    '''
#     import matplotlib.pyplot as plt
    plt.rc('font', size=font_size) #controls default text size
    plt.rc('axes', titlesize=font_size) #fontsize of the title
    plt.rc('axes', labelsize=font_size) #fontsize of the x and y labels
    plt.rc('xtick', labelsize=font_size) #fontsize of the x tick labels
    plt.rc('ytick', labelsize=font_size) #fontsize of the y tick labels
    plt.rc('legend', fontsize=f_legend) #fontsize of the legend
    pass

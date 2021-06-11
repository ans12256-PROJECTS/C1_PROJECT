# Plot all data sub_series
# Get color cycler
#  https://stackoverflow.com/questions/53521396/how-to-implement-automatic-color-change-in-matplotlib-with-subplots
colors = plt.rcParams["axes.prop_cycle"]()

#  Initialize new figure
fig, axs = plt.subplots(2,1, figsize=(35, 25))

#  need list of unique colors
for i in df_tmp['Species'].unique(): # Check unique values in 'Species'
    #     print(f'Species = {i}')

    # Get the next color from the cycler
    c = next(colors)["color"]

    #  Plot all data
    plot_two_cols(
    df_tmp[df_tmp['Species'] == i],
    y_lbl_in='Fish count', col_in=c, fig_in=fig,
    axs_in=axs[0], label_in = i, plt_type='l', l_wdth=5)  # axs[0] 1st subplot

    # Second subplot
    # All but 'Chinook' or 'Coho'
    if (i != 'Chinook' and i != 'Coho'):
# @@@
        plot_two_cols(
        df_tmp[df_tmp['Species'] == i],
        y_lbl_in='Fish count', col_in=c, fig_in=fig,
        axs_in=axs[1], label_in = i, plt_type='l', l_wdth=5) # axs[1] 2nd subplot





# linewidth proportional to  ∆T°F  linewidth=6, alpha = 0.5
#  https://matplotlib.org/stable/gallery/misc/zorder_demo.html
# zorder = (lines~2)
transp_alpha = 0.15 # transparency setting 1-solid 0-invisible
# axs[0].vlines(2008, 0, 120000, colors='blue', linestyles='dashed',
#               label='2008 Crisis', linewidth=3, alpha = transp_alpha, zorder=0) # zorder=0 ~ behind graph
axs[0].legend(loc='upper left')  # [] required, otherwise single character as string is iterable
axs[0].grid()
# axs[0].set_facecolor('w')
# axs[0].set_xticks[]

# axs[1].vlines(2008, 0, 2250, colors='blue', linestyles='dashed',
#               label='2008 Crisis', linewidth=6, alpha = transp_alpha, zorder=0) # zorder=0 ~ behind graph
axs[1].legend(loc='upper left')  # [] required, otherwise single character as string is iterable
axs[1].grid()


# Ocean temps block

Ocean_Temps = [-0.05, 0.50, -0.10, 0.24, 0.26, -0.28, 1.01, 0.48, -0.49, -0.60,
               0.24, 1.28, -0.82, -0.61, 0.31, 0.64, 0.64, 0.33, 0.48, -0.16,
               -0.47, 1.17, -0.07, -1.23, -0.83, -0.30, 0.63, 0.26, 0.46, 0.03,
               0.06, -0.61, -0.78, 0.30, -0.48, -0.85, -0.15, -0.33, 0.11, 1.46,
               0.33, -0.21, 0.01, 0.48, -0.37, -0.85]

# Ref: https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php
Ocean_Temps = [-0.05, 0.50, -0.10, 0.24, 0.26, -0.28, 1.01, 0.48, -0.49, -0.60,
               0.24, 1.28, -0.82, -0.61, 0.31, 0.64, 0.64, 0.33, 0.48, -0.16,
               -0.47, 1.17, -0.07, -1.23, -0.83, -0.30, 0.63, 0.26, 0.46, 0.03,
               0.06, -0.61, -0.78, 0.30, -0.48, -0.85, -0.15, -0.33, 0.11, 1.46,
               0.33, -0.21, 0.01, 0.48, -0.37, -0.85]
# Normalize for line width use
# Line color - red/blue if <>0
OTmin = min(Ocean_Temps)
OTmax = max(Ocean_Temps)
#  not using numpy array - number, but rather list comprehension
# a[:] = [x - 13 for x in a]
Ocean_Temps_n=[]
# Ocean_Temps_n[:] = [(x - OTmin)/(OTmax - OTmin) for x in Ocean_Temps]
# Ocean_Temps_n[:] = [(x)/(OTmax - OTmin) for x in Ocean_Temps]  # remove - OTmin to preserve signs
temp_ampl = max(abs(OTmin), abs(OTmax))
Ocean_Temps_n[:] = [x/temp_ampl for x in Ocean_Temps] # max amplitude of 1 +/- does not matter

Ocean_Temps_Years = list(range(1976,2022))

#  now zip it all together
Temps_tpl_List = list(zip(Ocean_Temps_Years, Ocean_Temps_n))
# Temps_tpl_List[5][0] = 1981
# Temps_tpl_List[5][1] = -0.28

df_OT = pd.DataFrame(Temps_tpl_List, columns=['Year','*1.46°F change'])

# #  Initialize new figure
# fig, axs = plt.subplots(figsize=(15, 15))

# x = df_OT.loc[:, 'Year']
# y = df_OT.loc[:, '*1.46°F change']
# axs.scatter(x, y, color = 'green', label='El Niño/La Niña')
# axs.set_xlabel('Observation years')
# axs.set_ylabel('*1.46°F change')
# axs.set_title('El Niño(warm) / La Niña(cold) years')

# axs.legend(loc='upper left')  # [] required, otherwise single character as string is iterable
# axs.grid()

temp_gate = 0.5/1.46         # from 0 to +- 1, plot only if equal or more; turn 1.46(max delta)/0.5 = 1/x
temp_gate_title = round(temp_gate * 1.46, 1) # for graph text equivalent in deg celcius
temp_width_scale = 35     # max vertical line width
temp_alpha = 0.15        # transparency level (1 solid)


# log is a conditional print function if DEBUG=True set at the top of the notebook
# Changing DEBUG in a single cell to false disables all debugging log printouts

# For every year see if plot is needed, and what line thickness, and color; No labels
for i in range(df_OT.shape[0]):
    [year, temp] = df_OT.iloc[i] # get year and NORMALIZED temperature change
    log(f'i = {i}, year = {year}, temp = {temp}')
    if abs(temp) >= temp_gate: # plot only if temp change is significant
        log('Entered if abs(temp) >= temp_gate:')
        if temp < 0:
            vlc = 'blue' # cold La Niña year Vertical_Line_Color = vlc
            log('Assigned blue')
        else:
            vlc = 'red'  # warm El Niño year
            log('assigned red')

        vlw = int(abs(temp) * temp_width_scale)  # int max width if abs(i) = 1
        log(f'assigned line width {vlw}')

         # no labels - color and line widths speak for themselves
        x = year
        log(f'x = {x}, will try to plot vertical line vlc = {vlc}, vlw = {vlw}')
        axs[0].vlines(x, 0, 120000, colors=vlc, linestyles='solid',
                       linewidth=vlw, alpha = temp_alpha, zorder=0) # zorder=0 ~ behind graph

        axs[1].vlines(x, 0, 2250, colors=vlc, linestyles='solid',
                       linewidth=vlw, alpha = temp_alpha, zorder=0) # zorder=0 ~ behind graph

# plt.style.use('ggplot')

# plt.style.use('classic')
font_sizes(35, 25)  # call font sizes def overall and legend
#  https://stackoverflow.com/questions/17086847/box-around-text-in-matplotlib
axs[0].text(1983, 92000, \
'Vertical bars El Niño(warm/red)\n \
and La Niña (cold/blue)\n max width *1.46°C', backgroundcolor='w',
bbox=dict(facecolor='w', edgecolor='black', boxstyle='round,pad=1'))

axs[0].text(2000, 100000, \
f'Temperature delta\n"gate" = {temp_gate_title}°C', backgroundcolor='w',
bbox=dict(facecolor='w', edgecolor='black', boxstyle='round,pad=1'))

# @@@ bookmark - Ctrl+F @@@

plt.show()


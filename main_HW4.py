##########################################################################################
# Program Filename: ENGR 103 - HW 4
# Author: Jeyeong You
# Date: 05.25.2022
# Description:
#
# Input:
# Output:
##########################################################################################

# Importing libraries
import pandas as pd
import waves as w
import matplotlib.pyplot as plt

# Loading data
  # wave height data
file_path = 'C:/Users/user/Downloads/wave_height.csv'
wave_height = pd.read_csv(file_path)
wave_height  # shows full dataframe

  # buoy ID data in 2021
file_path = 'C:/Users/user/Downloads/46248h2021.csv'
buoyID_2021 = pd.read_csv(file_path)
buoyID_2021  # shows full dataframe

# Array
  # wave height data Array
hour1 = wave_height.loc[:,"Wave Height Hour 1"]
print(hour1)
hour2 = wave_height.loc[:,"Wave Height Hour 2"]
print(hour2)
hour3 = wave_height.loc[:,"Wave Height Hour 3"]
print(hour3)

  # buoy ID data Array
hs = buoyID_2021.loc[:,"WVHT"]  # the significant wave height
print(hs)
tp = buoyID_2021.loc[:,"PERIOD"]  # the significant wave height
print(tp)
year_buoy = buoyID_2021.loc[:,"YEAR"]  # the significant wave height
print(year_buoy)
month_buoy = buoyID_2021.loc[:,"MON"]  # the significant wave height
print(month_buoy)
day_buoy = buoyID_2021.loc[:,"DAY"]  # the significant wave height
print(day_buoy)
hour_buoy = buoyID_2021.loc[:,"HOUR"]  # the significant wave height
print(hour_buoy)
minute_buoy = buoyID_2021.loc[:,"MIN"]  # the significant wave height
print(minute_buoy)

# -----------------------------------------
print('For Hour 1 the Significant Wave height should be',round(w.sig_wave_height(hour1),2),'m.')  # studio7
print('----------------------Part2-A--------------------------')
# print(w.calc_inc_power(hs,tp))  # Part2-A
print('----------------------Part2-B--------------------------')
print(w.find_monthly_data(month_buoy, tp, 1))  # Part2-B
print('----------------------Part2-C--------------------------')
ave_hgt_tem_array = []
max_hgt_tem_array = []
ave_pwr_tem_array = []
max_pwr_tem_array = []
ave_period_tem_array = []
max_period_tem_array = []

for x in range(12):
    ave_wave_height, max_wave_height, ave_wave_power, max_wave_power, ave_wave_period, max_wave_period = w.max_avg_hgt_pwr_period(
        w.find_monthly_data(month_buoy, hs, x + 1), w.find_monthly_data(month_buoy, w.calc_inc_power(hs, tp), x + 1),
        w.find_monthly_data(month_buoy, tp, x + 1))

    temp_ave_wave_height = ave_wave_height
    ave_hgt_tem_array.append(temp_ave_wave_height)

    temp_max_wave_height = max_wave_height
    max_hgt_tem_array.append(temp_max_wave_height)

    print('In month', x+1,'the average wave height is', ave_wave_height,'m, and the max wave height is', max_wave_height,' m.')
print('--------------------------------------------------------------------')

for x in range(12):
    ave_wave_height, max_wave_height, ave_wave_power, max_wave_power, ave_wave_period, max_wave_period = w.max_avg_hgt_pwr_period(
        w.find_monthly_data(month_buoy, hs, x + 1), w.find_monthly_data(month_buoy, w.calc_inc_power(hs, tp), x + 1), w.find_monthly_data(month_buoy, tp, x + 1))

    print('In month', x+1,'the average wave power is', ave_wave_power,'kW/m, and the max wave power is', max_wave_power,' kW/m.')
print('--------------------------------------------------------------------')

for i in range(12):
    ave_wave_height, max_wave_height, ave_wave_power, max_wave_power, ave_wave_period, max_wave_period = w.max_avg_hgt_pwr_period(
        w.find_monthly_data(month_buoy, hs, i + 1), w.find_monthly_data(month_buoy, w.calc_inc_power(hs, tp), i + 1), w.find_monthly_data(month_buoy, tp, i + 1))

    temp_ave_wave_period = ave_wave_period
    ave_period_tem_array.append(temp_ave_wave_period)

    temp_max_wave_period = max_wave_period
    max_period_tem_array.append(temp_max_wave_period)
    print('In month', i+1,'the average wave period is', ave_wave_period,'s, and the max wave period is', max_wave_period,' s.')

print('----------------------Part3-A--------------------------')
Cov_array = []

for d in range(12):
    temp_cof = w.coeff_variation(w.find_monthly_data(month_buoy,hs,d+1))
    Cov_array.append(temp_cof)
    print('In month', d+1,'the coefficient of variation in significant wave height is', w.coeff_variation(w.find_monthly_data(month_buoy,hs,d+1)),'.')

print('----------------------Part3-B--------------------------')

print('In Jan. the WEC efficiency is',w.wec_power(114,20,771),'%')
print('In Feb. the WEC efficiency is',w.wec_power(73,20,562),'%')
print('In March the WEC efficiency is',w.wec_power(69,20,562),'%')
print('In April the WEC efficiency is',w.wec_power(20,20,268),'%')
print('In May the WEC efficiency is',w.wec_power(16,20,153),'%')
print('In June the WEC efficiency is',w.wec_power(17,20,153),'%')
print('In July the WEC efficiency is',w.wec_power(10,20,83),'%')
print('In Aug. the WEC efficiency is',w.wec_power(14,20,153),'%')
print('In Sep. the WEC efficiency is',w.wec_power(31,20,268),'%')
print('In Oct. the WEC efficiency is',w.wec_power(87,20,562),'%')
print('In Nov. the WEC efficiency is',w.wec_power(58,20,562),'%')
print('In Dec. the WEC efficiency is',w.wec_power(84,20,771),'%')

print('----------------------Part4--------------------------')
month_12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print('Part 4 - A')
plt.plot(month_12, ave_hgt_tem_array, 'g')
plt.plot(month_12, max_hgt_tem_array, 'r')
plt.grid()
plt.xlabel('Month in 2021')
plt.ylabel('Wave Height')
plt.text(1,10,'Red - max wave height / Green - ave wave height')
plt.show()
print('--------------------------------------------------------')

print('Part 4 - B')
plt.plot(month_12, ave_period_tem_array, 'g')
plt.plot(month_12, max_period_tem_array, 'r')
plt.grid()
plt.xlabel('Month in 2021')
plt.ylabel('Wave Period')
plt.text(2,16,'Red - max wave period / Green - ave wave period')
plt.show()
print('--------------------------------------------------------')

print('Part 4 - C')
plt.plot(month_12, Cov_array, 'r--')
plt.grid()
plt.xlabel('Month in 2021')
plt.ylabel('CoV')
plt.show()
print('--------------------------------------------------------')

print('Part 4 - D')
power_available_list = [w.available_power(114), w.available_power(73), w.available_power(69), w.available_power(20),
                        w.available_power(16), w.available_power(17), w.available_power(10), w.available_power(14),
                        w.available_power(31), w.available_power(87), w.available_power(58), w.available_power(84),]
power_WEC = [771, 562, 562, 268, 153, 153, 83, 153, 268, 562, 562, 771]

plt.plot(month_12, power_available_list, 'g')
plt.plot(month_12, power_WEC, 'r')
plt.grid()
plt.xlabel('Month in 2021')
plt.ylabel('Wave Power')
plt.text(3,2050,'Red - the power the WEC / Green - power available')
plt.show()
print('--------------------------------------------------------')

print('Part 4 - E')
energy_harvested = [w.wec_power(114,20,771), w.wec_power(73,20,562), w.wec_power(69,20,562),
                    w.wec_power(20,20,268), w.wec_power(16,20,153), w.wec_power(17,20,153),
                    w.wec_power(10,20,83), w.wec_power(14,20,153), w.wec_power(31,20,268),
                    w.wec_power(87,20,562), w.wec_power(58,20,562), w.wec_power(84,20,771)]
plt.plot(month_12, energy_harvested, 'r--')
plt.grid()
plt.xlabel('Month in 2021')
plt.ylabel('Energy Harvested by the WEC(%)')
plt.show()


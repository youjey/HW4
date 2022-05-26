import numpy as np

# Studio 7 adding
def sig_wave_height(hour):
    highest_hour = np.sort(hour)
    length = int(len(hour)/3)
    sig_wave_length = highest_hour[-length : -1]
    ave_sig_wave_length = np.average(sig_wave_length)
    return(ave_sig_wave_length)

# Part2-A
def calc_inc_power(significant_wave_height, peak_period):
    inc_wave_power_array = []
    for x in range(len(significant_wave_height)):
        inc_wave_power = 0.5 * (significant_wave_height[x]**2) * peak_period[x]  # incoming wave power per m of shoreline (kW/m)
        inc_wave_power_array.append(inc_wave_power)
    return(inc_wave_power_array)

# Part2-B
def find_monthly_data(month_inte_array, data_array, month_inte_number):  # 2-B
    temp_array = []
    for d in range(len(data_array)):
        if month_inte_array[d] == month_inte_number:
            temp_array.append(data_array[d])
    return(temp_array)

#Part2-C

def max_avg_hgt_pwr_period(wave_height_array, incoming_power_array, wave_period_array):  # 2-C
    max_wave_height = np.max(wave_height_array)
    ave_wave_height = np.average(wave_height_array)
    max_wave_power = np.max(incoming_power_array)
    ave_wave_power = np.average(incoming_power_array)
    max_wave_period = np.max(wave_period_array)
    ave_wave_period = np.average(wave_period_array)
    return(ave_wave_height , max_wave_height, ave_wave_power, max_wave_power, ave_wave_period, max_wave_period)

# part3-A
def coeff_variation(monthly_wave_height):
    CoV = np.std(monthly_wave_height) / np.mean(monthly_wave_height)
    return(CoV)

# part3-B
def wec_power( ave_wave_power, WEC_length, WEC_power):
    total_available_WEC = WEC_length * ave_wave_power
    energy_harvested = WEC_power / total_available_WEC * 100
    return(energy_harvested)

# part4-D
def available_power(ave_wavepower):
    available = ave_wavepower * 20
    return(available)
import numpy as np

def sig_wave_height(hour):
    highest_hour = np.sort(hour)
    length = int(len(hour)/3)
    sig_wave_length = highest_hour[-length : -1]
    ave_sig_wave_length = np.average(sig_wave_length)
    return(ave_sig_wave_length)
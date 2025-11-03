# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:09:55 2025

@author: nondondey64@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from  scipy.stats import linregress
from scipy import signal
import pandas as pd
from glob import glob
# datafile = glob('C:/Research/Data 316L-20230710/316L_Wrought/*')   #d=3000
datafile = glob('C:/Research/Data_Aluminium-20230623/group_21/*')     #d=18000
# datafile = glob('C:/Research/AM PE Data (Wrought, Good, Middle, Bad)-20230907/Pulse-Echo Data/100W-600/*') #d=3000
# datafile = glob('C:/Research/Data 316L-20230710/100W_600/*')       #d=3000
# datafile = glob('C:/Research/AM PE Data (Wrought, Good, Middle, Bad)-20230907/Pulse-Echo Data/CRR_10MHz - Wrought/*')       #d=3000

vel = []
absor_coef = []
r_square_coef=[]
r_square_vel=[]
t=0
'when runs the code, it will take two inputs peaks = assign no of peaks(such as 6 or 7 or8) and distance = minimum distance between peak to peak'
peaks=input('How many peaks?')
distance=input('Minimum distance between peaks?')
n = int(peaks)
dis=int(distance)
for data in datafile:
    a = np.loadtxt(data,float)
    x=a[:,0]   
    y=a[:,1]   # Amplitudes
   
# finding maximum peaks of individual echo 
    peak_index,_ = find_peaks(y, height=-1, distance=dis, prominence=None)  # To find maximum peak of each echo, we need to adjust minimum height and minimum distance between peaks for different data set.
    peak_values = []
    for j in range(len(peak_index)):
        peak = y[peak_index[j]]
        peak_values.append(peak) 
                                                                                         
    
# Identify each pulse echo peak and does pading to a lenth of original data
    # n = 5  # number of peaks to use in the correlation (there could be more in the time trace than this number)
    # The last peaks, being so small, they might not help - they can add large errors
    # peaks = []
    pad_sig = []
    amp = []            #maximum peak indices

    for k in range(n):
        c0 = int((peak_index[k]+peak_index[k+1])/2)
        c1 = int((peak_index[k+1]+peak_index[k+2])/2)   
        peak1 = y[c0:c1]
        pad1 = np.pad(peak1,(c0,len(y)-len(peak1)-c0),mode='edge')    
        pad_sig.append(pad1)
        amp.append(max(peak1))
        
        
                    
       
#This section is for correlation
    lag_index = []
    corr_amp=[]
    for i in range(len(pad_sig)):
    # Compute the correlation
        correlation = signal.correlate(pad_sig[0], pad_sig[i], mode='full', method='auto') 
    # Find the lag indices corresponding to the maximum correlation   
        lags = signal.correlation_lags(pad_sig[0].size, pad_sig[i].size, mode="full")
        lag = abs(lags[np.argmax(correlation)])  
        lag_index.append(lag) 
        
        
    sampling_rate = len(y)/(x[-1]-x[0])  #hz
    #  Calculate the time delay in seconds
    time_delay = lag_index/ sampling_rate
    
#For different number of peaks. Sometime less than 5 peaks    
    d = .0255 #in m #25.5 mm (Thickness of the sample)
    if n==6:  # no of echo amplidude will be using for the analysis
        depth = np.array([0, 2*d, 4*d, 6*d, 8*d, 10*d])
    elif n==7:
        depth = np.array([0, 2*d, 4*d, 6*d, 8*d, 10*d, 12*d])
    elif n==5:    
        depth = np.array([0, 2*d, 4*d, 6*d,8*d])            
    else: 
        depth = np.array([0, 2*d, 4*d])
#Linear fit for velocity    
    p_v = np.polyfit(time_delay, depth, 1)
#Calculation for R square of velocity
    pre_v = p_v[0]*time_delay+p_v[1]    
    vel.append(p_v[0])
    #r square using function
    slope, intercept, r_value, p_value, std_err = linregress(depth, pre_v)
    r_square_vel.append(r_value**2)

    
# For absorption coefficient  
    amplitude_ratio = amp[0]/amp
    log_amplitude_ratio = np.log(amplitude_ratio)
    p = np.polyfit(depth,log_amplitude_ratio, 1)
    
#Calculation for R square of absorption coefficient  
    pre = p[0]*depth+p[1]
    absor_coef.append(p[0])
    #r square using function
    slope, intercept, r_value, p_value, std_err = linregress(log_amplitude_ratio, pre)
    r_square_coef.append(r_value**2)

    
# plots for velocity  
    plt.subplot(4,3,t+1) 
    plt.plot(time_delay,depth,'ro', ms=5, mfc='None', lw=0.5, alpha=1, label='Data points')
    y_ = p_v[0]*time_delay + p_v[1]
    plt.plot(time_delay,y_,'g',label=f'Linear fit and R square = {round(r_square_vel[t],6)}')
    plt.axvline(x=0, color = 'k')
    plt.xlabel('Time delay')
    plt.ylabel('Depth')
    plt.legend(loc='upper left')
    plt.title(f'Signal={t}')
    plt.subplots_adjust(left=None, right=None, top=None, bottom=None,hspace=.5)
    plt.grid(True)
    plt.show() 
    # plt.tight_layout()
    t=t+1    
# Plot for absorption coefficient
    # plt.subplot(4,3,t+1) 
    # plt.plot(depth,log_amplitude_ratio,'ro', ms=5, mfc='None', lw=0.5, alpha=1, label='Data points')
    # y_ = p[0]*depth + p[1]
    # plt.plot(depth,y_,'g',label=f'Linear fit; R^2 = {round(r_square_coef[t],3)} and slope = {round(absor_coef[t],4)}')
    # plt.axvline(x=0, color = 'k')
    # plt.xlabel('Depth')
    # plt.ylabel('Log of amplitude ratio')
    # plt.legend(loc='upper left')
    # plt.title(f'Signal={t}')
    # plt.subplots_adjust(left=None, right=None, top=None, bottom=None,hspace=.6) 
    # plt.grid(True)
    # plt.show()
    # t=t+1 
  
    
    
# for velocity 
std_v = np.std(vel)
mean_vel = np.mean(vel)    
mean_r_square_vel = np.mean(r_square_vel)
d1 = {'Velocity ':vel,'    Values of R square':r_square_vel}
d2 = {'Average Velocity':[mean_vel], 'Average of R square':[mean_r_square_vel], 'Standard deviation of Velocity':[std_v] }
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
print(df1)
print()
print(df2)
print()

# for absorption coefficient
std_coef = np.std(absor_coef)
mean_ab_coef = np.mean(absor_coef)    
mean_r_square_coef = np.mean(r_square_coef)
d1 = {'Absorption coefficient ':absor_coef,'    Values of R square':r_square_coef}
d2 = {'Average absorption coef':[mean_ab_coef],'Average of R square':[mean_r_square_coef],'Std of coefficient':[std_coef] }
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
print(df1)
print()
print(df2)

# #plot to show velocity, average velocity and standard deviation
# indices = np.arange(len(datafile))
# # Plot velocity
# plt.plot(indices, vel, 'ro', ms=5, mfc='None', lw=0.5, alpha=1,label='Velocity')
# # Plot average velocity as a horizontal line
# plt.axhline(mean_vel, color='b', linestyle='--', label='Average Velocity')
# # Plot standard deviation as a shaded region around the average
# plt.fill_between(indices, mean_vel - std_v, mean_vel + std_v, color='gray', alpha=0.5, label='Standard Deviation')
# # Add labels, title, legend, etc.
# plt.xlabel('Time')
# plt.ylabel('Velocity')
# plt.title('Velocity, Average, and Standard Deviation of Velocity')
# plt.legend()
# plt.grid(True)




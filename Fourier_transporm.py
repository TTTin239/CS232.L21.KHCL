"""Họ và tên: Trần Trung Tín
MSSV: 19522351
Lớp: CS232.L21.KHCL"""

# Python example - Fourier transform using numpy.fft method

import numpy as np
import matplotlib.pyplot as plt

# How many time points are needed i,e., Sampling Frequency
samplingFrequency = 100;

# At what intervals time points are sampled
samplingInterval = 1 / samplingFrequency;

# Begin time period of the signals
beginTime = 0;

# End time period of the signals
endTime = 10; 

# Frequency of the signals
signal1Frequency = 5;
signal2Frequency = 8;
signal3Frequency = 10;
signal4Frequency = 14;

# Time points
time = np.arange(beginTime, endTime, samplingInterval);

# Create sine waves
amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)
amplitude3 = np.sin(2*np.pi*signal3Frequency*time)
amplitude4 = np.sin(2*np.pi*signal4Frequency*time)

# Create subplot
figure, axis = plt.subplots(6, 1)
plt.subplots_adjust(hspace=1)

# Time domain representation for sine wave 1
axis[0].set_title('Sine wave with a frequency of 5 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')

# Time domain representation for sine wave 2
axis[1].set_title('Sine wave with a frequency of 8 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')

# Time domain representation for sine wave 3
axis[2].set_title('Sine wave with a frequency of 10 Hz')
axis[2].plot(time, amplitude3)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')

# Time domain representation for sine wave 4
axis[3].set_title('Sine wave with a frequency of 14 Hz')
axis[3].plot(time, amplitude4)
axis[3].set_xlabel('Time')
axis[3].set_ylabel('Amplitude')

# Add the sine waves
amplitude =  amplitude3 + amplitude4 + amplitude1 + amplitude2

# Time domain representation of the resultant sine wave
axis[4].set_title('Sine wave with multiple frequencies')
axis[4].plot(time, amplitude)
axis[4].set_xlabel('Time')
axis[4].set_ylabel('Amplitude')

# Frequency domain representation
fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(amplitude)/4))] # Exclude sampling frequency
tpCount     = len(amplitude)
values      = np.arange(int(tpCount/4))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

# Frequency domain representation
axis[5].set_title('Fourier transform depicting the frequency components')
axis[5].plot(frequencies, abs(fourierTransform))
axis[5].set_xlabel('Frequency')
axis[5].set_ylabel('Amplitude')

plt.show()
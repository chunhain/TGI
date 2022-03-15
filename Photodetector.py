# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:54:00 2022

@author: Herroh
"""


from daqmx import NIDAQmxInstrument, AnalogInput

# tested with NI USB-6001
# which has the following digital inputs:
#  - port0/line0 through line7
#  - port1/line0 through line3
#  - port2/line0

# first, we allocate the hardware using the automatic hardware
# allocation available to the instrument; this is safe when there
# is only one NIDAQmx instrument, but you may wish to specify a
# serial number or model number for a safer experience
daq = NIDAQmxInstrument()

print(daq)

# the easiest way to get a single sample is to select the analog input
# attribute on the daq and interrogate its `value` attribute
print(f'daq.ai0.value: {daq.ai0.value:.3f}V')
print(f'daq.ai1.value: {daq.ai1.value:.3f}V')
print(f'daq.ai2.value: {daq.ai2.value:.3f}V')
print(f'daq.ai3.value: {daq.ai3.value:.3f}V')

# you will start throwing errors if you interrogate
# inputs that don't exist on the device (uncomment to see!)
#print(f'daq.ai4.value: {daq.ai4.value:.3f}V')

# for more nuanced control over the analog
# input, we could use the `capture` method

values = daq.ai0.capture(
    sample_count=5, rate=100,
    max_voltage=10.0, min_voltage=0,
    mode='differential', timeout=10.0
)

# frequency = daq.ai0.find_dominant_frequency(sample_count=500, rate=10,
#     max_voltage=10.0, min_voltage=0,
#     mode='differential', timeout=50.0
    # )

# :return: the frequency found to be at the highest amplitude; this is often the fundamental frequency in many domains

print(f'values: {values} V')
# print(f'values: {frequency} V')


# note that the values come back as type `numpy.ndarray`
print(f'type(values): {type(values)}')
# print(f'type(frequency): {type(frequency)}')


# if you already know your device name, you might be
# happier going straight to the `AnalogInput` constructor:
ai0 = AnalogInput(device='Dev1', analog_input='ai0')

# we can do anything that we could have
# done previously with the daq.aiX
print(f'ai0.value: {ai0.value:.3f}V')
# print(f'ai0.frequency: {ai0.frequency:.3f}V')



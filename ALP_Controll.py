# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:00:27 2022

@author: Herroh
"""
import os

path = 'D:/PhD/Herroh_GI/python/DMD_Control'
os.chdir(path)


import numpy as np
from ALP4 import *
import time

# Load the Vialux .dll
DMD = ALP4(version = '4.2')
# Initialize the device
DMD.Initialize()

# Binary amplitude image (0 or 1)
bitDepth = 1    
imgBlack = np.zeros([DMD.nSizeY,DMD.nSizeX])
imgWhite = np.ones([DMD.nSizeY,DMD.nSizeX])*(2**8-1)
imgSeq  = np.concatenate([imgBlack.ravel(),imgWhite.ravel()])

# Allocate the onboard memory for the image sequence
DMD.SeqAlloc(nbImg = 2, bitDepth = bitDepth)
# Send the image sequence as a 1D list/array/numpy array
DMD.SeqPut(imgData = imgSeq)
# Set image rate to 50 Hz
DMD.SetTiming(pictureTime = 20000)

# Run the sequence in an infinite loop
DMD.Run()

time.sleep(100)

# Stop the sequence display
DMD.Halt()
# Free the sequence from the onboard memory
DMD.FreeSeq()
# De-allocate the device
DMD.Free()
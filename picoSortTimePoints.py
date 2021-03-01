# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:17:43 2021

@author: caitl
"""
# MAKE A BACKUP BEFORE RUNNING PLEASE! haven't added that bit yet
import shutil
import os
import glob
import fnmatch

# Copy/paste path to folder with raw data
baseDirectory = 'copy/path/file/here'
os.chdir(baseDirectory)

# Experimental setup: location of wells used on plate, number of laser channels for acquisition
usedWells = ['B02', 'B03', 'B04', 'B05', 'C02', 'C03', 'C04', 'C05']
channels = 2

# Set to the first time point folder in the base directory , eg if "TimePoint_42" is the first file, change this to 42
timePointStart = 1

# Set duration of imaging time (hours) and the interval time (hours) between images. Total should give number of folders
durationHours = 16
intervalHours = 0.5
timePointTotal = timePointStart + (durationHours / intervalHours)

# Start with renaming, so that when they get moved, you know what time point the file is from
while timePointStart <= timePointTotal:
    timePointFolder = baseDirectory + '/TimePoint_' + str(timePointStart)
    for filename in os.listdir(timePointFolder):
        if filename.endswith('.tif'):
            os.rename(os.path.join(timePointFolder, filename), os.path.join(timePointFolder, str(timePointStart) + '_' + filename))
            continue   
    timePointStart = timePointStart + 1

channels = list(range(channels + 1))
del channels[0]

# Make and move files from timepoint folders into folders and subfolders for each well and channel  
for folder in usedWells:
    os.mkdir(os.path.join(baseDirectory, folder))
    for subfolder in channels:
        os.mkdir(os.path.join(baseDirectory + '/' + folder, folder + '_' + str(subfolder)))
for i in range(len(usedWells)):
    for name in glob.glob(baseDirectory + '/TimePoint_*/*' + usedWells[i] + '*'):
        for c in channels:
            if fnmatch.fnmatch(name, '*_w' + str(c) + '.tif'):
                shutil.move(name, os.path.join(baseDirectory, usedWells[i] + '/' + usedWells[i] + '_' + str(c) + '/'))

# Get rid of now empty time point folders
for folder in glob.glob(baseDirectory + '/TimePoint_*/'):
    os.rmdir(folder)
### ImageXpress Pico
Designed based on export files from ImageXpress Pico microscope from Molecular Devices

#### picoSortTimePoints.py
Re-sorting exported images by well and laser channel instead of time points from live imaging data. Assumes time point folders are named: 'TimePoint_\*' and file names contain well number (eg. A02) and channel (\_w2).

Input:
- Line 14: file path to base directory containing all the timepoint files
- line 18: wells that were imaged, as strings
- line 19: number of channels acquired
- line 22: number of the first time point folder, in case it's not 1
- line 25: duration of the live imaging session
- line 26: time of acquisition intervals

What it does:
1. Renames files based on which timepoint folder the images are located in. Adds time point number to the start of the file name.
2. Makes folders and subfolders for each well and channels, respectively.
3. Sorts images from each time point into corresponding folders according to well number and channel.
4. Removes empty time point folders.

Output: list of folders named for each well containing images from each channel 

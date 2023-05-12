#!/usr/bin/env python
# coding: utf-8
# Authors: Rebekah Esmaili (STC) and Amy Huff (IMSG)

import s3fs
import datetime
from pathlib import Path
import os

directory_path = Path.cwd()
subdir = 'data'

# Create a new directory because it does not exist
isExist = os.path.exists(directory_path / subdir)
if not isExist:
   os.makedirs(directory_path / subdir)

# Connect to the AWS S3 bucket
fs = s3fs.S3FileSystem(anon=True)

# Download NUCAPS -----------------------------------------------
bucket = 'noaa-jpss'
satellite = 'NOAA20'
sensor = 'SOUNDINGS'
product = 'NOAA20_NUCAPS-OLR'

# optional: use specific date
year = 2023
month = 4
day = 22

# optional: use today's date 
# dt = datetime.datetime.now()
# year = dt.strftime('%Y')
# month = dt.strftime('%m')
# day = dt.strftime('%d')

# optional: start/end hour-min
start_time = '0000'
end_time = '2359'

files_path = bucket + '/' + satellite + '/'  + sensor + '/' + product + '/' + str(year) + '/' + str(month).zfill(2) + '/' + str(day).zfill(2)
files = fs.ls(files_path)

matches = [file for file in files if (file.split('/')[-1].split('_')[3][9:13] >= start_time and file.split('/')[-1].split('_')[3][9:13] <= end_time)]

for match in matches:
    print("Downloading: ", match)
    fs.get(match, str(directory_path / subdir / match.split('/')[-1]))

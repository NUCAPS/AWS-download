# Downloading NUCAPS from the NODD

NOAA products are available via cloud resources as part of the [NOAA Open Data Dissemination](https://www.noaa.gov/information-technology/open-data-dissemination) (NODD) program.

The NODD duplicates the data available on NOAA CLASS and is updated in near-real time. The program starts ~Oct 2022, so the entire record is not available.

It's straightforward to download real-time data using scripting languages like Python. The repository contains a simple sample script to query AWS for the NUCAPS OLR.

## Pre-requisites

You will need python (I recommend [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)). You will also need the [s3fs](https://s3fs.readthedocs.io/en/latest/) package. The installation syntax is below, type it into the Terminal (MacOS/Linux users) or the Anaconda Prompt (Windows users)

```bash
conda install s3fs -c conda-forge
```

## Editing the script
You will need to open up the ```download_data.py``` file and edit the date product and date range that you are downloading. The script can be easilly altered to download another JPSS product.

select the product:
```python
product = 'NOAA20_NUCAPS-EDR'
# other choices: NOAA20_NUCAPS-EDR, NOAA20_NUCAPS-CCR, NOAA20_NUCAPS-OLR
```

Update the date range:

```python
year = 2023
month = 4
day = 22

start_time = '0000'
end_time = '2359'
```

You can also download the most recent data using:
```python
# use today's date 
dt = datetime.datetime.now()
year = dt.strftime('%Y')
month = dt.strftime('%m')
day = dt.strftime('%d')

start/end hour-min
one_hour_ago = dt - datetime.timedelta(hours=1)

start_time = one_hour_ago.strftime('%H%m')
end_time = dt.strftime('%H%m')
```

Save and exit the script when you are done.

## Running the Script
To run the script, simply type:

```bash
python download_data.py
```

## Need additional help?

See our [tutorial](https://github.com/modern-tools-workshop/AMS-python-workshop-2023/blob/main/download_satellite_data.ipynb) from AMS 2023 on downloading data from the cloud.

## Authors
Code developed by Rebekah Esmaili ([STC](https://www.stcnet.com/)) and Amy Huff ([IMSG](https://imsg.com/)).
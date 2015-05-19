# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:25:31 2015

@author: bcook
"""
# This program will process the European Grape Harvest Data, converting to day 
# of year and anomalizing relative to some defined interval. Original Harvest 
# dates are presented as the number of days after 31 August.

#%%
# Setup the Analysis
reset -f

import calendar
import datetime
import numpy as np
import netCDF4
import os
import matplotlib
import copy
from matplotlib import pyplot as plt
import scipy
import seaborn as sns
import pandas as pd
import scipy.stats as stats
from mpl_toolkits.basemap import Basemap, cm
from matplotlib import interactive
interactive(True)

# Suppress Warnings
import warnings
warnings.filterwarnings('ignore')

# Embeds plots inside the notebook (use in iPython Notebook)
#%matplotlib inline

# Last year in np.arange is excluded
#     Generate year vectors for exploratory analyses over different time periods
base_period      = np.arange(1600,1901)   # baseline period for anomaly calculation
period_1600_1980 = np.arange(1600,1981)   # 1600-1980
period_1901_1950 = np.arange(1901,1951)   # 1951-1980
period_1951_1980 = np.arange(1951,1981)   # 1951-1980
period_1981_2007 = np.arange(1981,2008)   # 1981-2007

# Column Headers for Time Span Specific Data Frames
col_txt=["1600-1900","1600-1980","1901-1950","1951-1980","1981-2007"]

# Other Variables
mon=np.arange(1,9)                   # month vector, used for converting to DOY               
infile = '../data/europe2012ghd.csv'  # Name of the original data file

#%%
# Dataframe adjustments
# Import the original Daux data into a dataframe
df=pd.read_csv(infile)

# Rename Columns
df.columns = df.loc[2,:]
df=df.rename(columns = {'Abb.':'Year'})

# Delete Header Rows
df = df.drop(df.index[:3])

# Make the Index the 'Year' and then Drop from the Dataframe
df.index = df.loc[:,'Year']
del(df['Year'])

# Pull out year series and convert to 64 float precision. These are the variables
# I will operate on.
yr=np.int64(df.index)
ghd=np.float64(df.loc[:,:])

# New ghd matrix that will be converted to day of year
ghd_doy=copy.deepcopy(ghd) # need to use copy statement to make a proper copy of a variable

#%%
# Pull out Specific sites for the core index
#core_names=['Als','Auv','Bor','Bur','Cha2','Lan','LLV','Spa','SRv','Swi']
#core_names=['Als','Bor','Bur','Cha2','Lan','LLV','SRv','Swi']

#core_names=['Als','Bor','Bur','Cha2','LLV','SRv','Swi']
core_names=['Als','Bor','Bur','Cha2','Lan','LLV','SRv','Swi']

core_locs=np.int64(np.zeros(np.size(core_names)))

# Find locations for these series in the dataframe
for loop_series in enumerate(core_names):
    print(loop_series)
    core_locs[loop_series[0]] = np.int64(np.where(df.columns==loop_series[1])[0])

# Locations in the data frame
print("")
print("Core Sites, Column Locations")
print(core_locs)

#%%
# Convert to Day of Year from Day relative to August 31
for loop_yr in enumerate(yr):
    
    # Year index and current year
    i_yr = loop_yr[0]; curr_yr = loop_yr[1];       

    # Initialize day of year for August 31   
    doy_aug31 = 0
    
    # Month Loop-January to August
    for loop_mon in enumerate(mon):        
        # Month Index and Current Month      
        i_mon = loop_mon[0]; curr_mon = loop_mon[1];       
        # Add days to doy_aug31
        doy_aug31=doy_aug31+calendar.monthrange(curr_yr,curr_mon)[1]

    # Convert GHD to DOY     
    ghd_doy[i_yr,:]=ghd_doy[i_yr,:]+doy_aug31





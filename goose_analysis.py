import numpy as np
from qgis.utils import iface
from qgis.core import *
from datetime import datetime
import os
from analysis.anova import *
from preprocessing.stack_tiff import *
from preprocessing.import_shapefile import *
from preprocessing.get_temperature import *
from preprocessing.import_raster import *
from preprocessing.get_arrays import *
from postprocessing.time_series import *
from postprocessing.heatmap import *


##################### IMPORTANT ##########################

#The code only works if the project folder path is defined#
#Modify the example below #
project_folder=os.path.join('/Users','sebastiangarzon','Desktop','PythonProject')
                          
####################### PREPROCESSING #########################

#### Relative paths Files ####
raster_folder = os.path.join(project_folder,'databases','raster')
shp_folder=os.path.join(project_folder,'databases','shapefiles')
raster_tif_path=os.path.join(raster_folder,'stacked.tif')
figures_folder=os.path.join(project_folder,'figures')

#### Stack rasters ####
single_tif_to_stacked(raster_folder)

#### Load Shapefile ####
shp_points=import_shp(shp_folder,"points")

#### Load Raster #####
temp_raster=import_raster(raster_tif_path)

#### Extract raster temperature information and add it to the shapefile ###
get_month_band_temperature(shp_points,temp_raster)

#### Extract arrays for analysis ####
x, y, ids, months, years, temps,timestamps = extract_arrays(shp_points, excludeNone = True)


####################### ANALYSIS #########################

##### Statistical analysis #####

# Create fake month indicators for testing
tot_animals = 4
tot_months = 6
np.random.seed(seed = 1234)
month = np.repeat(np.arange(1,tot_months+1,1), tot_animals)

# Create fake individual indicators for testing
ind = []
for i in range(1,tot_months+1):
    ind.append(list(range(1, tot_animals+1)))
ind = np.array(ind).flatten()
temp = np.random.normal(size = len (month))

# Check function
F, pval = repeated_measures_oneway_anova(temp, month, ind)


####################### POST-PROCESSING #########################


# Timeseries plot
timeseries_path=os.path.join(figures_folder,'timeseries_geese.png')
plot_timeseries(ids,timestamps,temps,timeseries_path)


# Dynamic heatmap
figpath = os.path.join(figures_folder,'monthly_heatmap.png')
monthly_heatmap(x, y, months, 5, 25, figpath)
import numpy as np
from qgis.utils import iface
from qgis.core import *
import os
from analysis.anova import *
from preprocessing.stack_tiff import *
from preprocessing.import_shapefile import *
from preprocessing.get_temperature import *
from preprocessing.import_raster import *
from preprocessing.get_arrays import *
from postprocessing.heatmap import *

##################### IMPORTANT ##########################

#The code only works if the project folder path is defined#
#Modify the example below #
project_folder=os.path.join('/Users','PythonProject')
                          
####################### PREPROCESSING #########################

#### Relative paths Files ####
raster_folder = os.path.join(project_folder,'databases','raster')
shp_folder=os.path.join(project_folder,'databases','shapefiles')
raster_tif_path=os.path.join(raster_folder,'stacked.tif')

#### Stack rasters ####
single_tif_to_stacked(raster_folder)

#### Load Shapefile ####
shp_points=import_shp(shp_folder,"points")

#### Load Raster #####
temp_raster=import_raster(raster_tif_path)

#### Extract raster temperature information and add it to the shapefile ###
get_month_band_temperature(shp_points,temp_raster)

#### Extract arrays for analysis ####
x, y, ids, months, years, temps = extract_arrays(shp_points, excludeNone = True)

####################### ANALYSIS #########################

##### Statistical analysis #####
figpath = os.path.join(project_folder,'figures','anova.png')
temps_avg, seasons_avg, ids_avg = seasonal_individual_averages(temps, months, ids)
F, pval = repeated_measures_oneway_anova(temps_avg, seasons_avg, ids_avg, figpath)


####################### POST-PROCESSING #########################

# Dynamic heatmap
figpath = os.path.join(project_folder,'figures','monthly_heatmap.png')
monthly_heatmap(x, y, months, 5, 25, figpath)

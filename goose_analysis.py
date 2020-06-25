import numpy as np
from qgis.utils import iface
from qgis.core import *
import os
from analysis.anova import *
from preprocessing.stack_tiff import *
from preprocessing.import_shapefile import *
from preprocessing.get_temperature import *
from preprocessing.import_raster import *

##################### IMPORTANT ##########################
#The code only works if the project folder path is defined#
#Modify the example below #

project_folder=os.path.join('/Users','PythonProject')

##########################################################

#### Relative paths Files ####

raster_folder = os.path.join(project_folder,'databases','raster')
shp_folder=os.path.join(project_folder,'databases','shapefiles')
raster_tif_path=os.path.join(raster_folder,'stacked.tif')

#### Preprocessing ####

single_tif_to_stacked(raster_folder)

#### Load datasets ####

#### Shapefile ####
shp_points=import_shp(shp_folder,"points")

#### Raster #####
temp_raster=import_raster(raster_tif_path)

#### Extract raster temperature information and add it to the shapefile ###

get_month_band_temperature(shp_points,temp_raster)

##### ANOVA ANALYSIS #####

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
repeated_measures_oneway_anova(temp, month, ind)

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
from analysis.get_table import *
from postprocessing.time_series import *
from postprocessing.rasterplot import *
from postprocessing.heatmap import *
from postprocessing.monthly_distribution import *
from postprocessing.individuals_distribution import *
from postprocessing.plot_trajectories import *
from postprocessing.get_summary import *


##################### IMPORTANT ##########################

#The code only works if the project folder path is defined#
#Modify the example below #
project_folder=os.path.join('/Users','PythonProject')

                          
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
anova_path = os.path.join(project_folder,'figures','Fig7_anova.png')
temps_avg, seasons_avg, ids_avg = seasonal_individual_averages(temps, months, ids)
F, pval = repeated_measures_oneway_anova(temps_avg, seasons_avg, ids_avg, anova_path)

# month/individual table
table_path = os.path.join(figures_folder,'Tab1_month_individual_table.png')
plot_table(ids, years, months, temps, table_path)


####################### POST-PROCESSING #########################

# plot trajectories
layer=import_shp(shp_folder,"lines")
path = os.path.join(figures_folder,'Fig1_bird_trajectories.png')
plot_trajectories(layer, path )

# Raster temperature maps
rastermap_path=os.path.join(figures_folder,'Fig2_temperature_rastermap.png')
plot_temp_rasters(temp_raster, -30, 30, rastermap_path)

# Timeseries plot
timeseries_path=os.path.join(figures_folder,'Fig3_timeseries_geese.png')
plot_timeseries(ids,timestamps,temps,timeseries_path)

# individuals-distribution joyplot 
ind_path = os.path.join(figures_folder,'Fig4_individuals_distribution.html')
individuals_distribution(ids, temps, ind_path)

# monthly-distribution joyplot 2007
monthly_path = os.path.join(figures_folder,'Fig5-1_monthly_distribution_2007.html')
monthly_distribution(2007, months, years, temps, monthly_path)

# monthly-distribution joyplot 2008 
monthly_path = os.path.join(figures_folder,'Fig5-2_monthly_distribution_2008.html')
monthly_distribution(2008, months, years, temps, monthly_path)

# Dynamic heatmap
heatmap_path = os.path.join(figures_folder,'Fig6_monthly_heatmap.png')
monthly_heatmap(x, y, months, 5, 25, heatmap_path)

# Temperature summary for all geese
table_path = os.path.join(figures_folder,'Tab2_individual_summary_table.png')
get_sum(ids, years, temps,table_path)
# Spatio-temporal analysis of white-fronted geese temperature trajectories

Carles Milà, Giulia Molisse, Sebastián Garzón, Parichay Mandal (2020)
Westfälische Wilhelms-Universität

# Manual

#to do

# Requirements

1. In file `goose_analysis.py` modify `project_folder` variable to the current location of this folder on your computer.

2. Run this code by using the QGIS python-IDE.

3. This project use python modules and QGIS so it is requiered an additional configuration:

  - In QGIS, go to Settings -> Options
  - In the window that appears, go to the tab System
  - In that tab, go to the Environment section
  - Check the box "Use custom variables"
  - Add a variable `PYTHONPATH` and as the value add the `path` where your modules are located (same as `project_folder` from requirement 1)
  - Restart QGIS
  
  # Individual contributions
  
| Script name |  Section|  Carles | Giulia   | Sebastian | Parichay |
|:-------------:|:---------:|:---------:|:----------:|:---------:|:---------:|
|`goose_analysis.py`|Main|S|S|M|S|
|`stack_tiff.py`|Preprocessing|||M||
|`import_raster.py`|Preprocessing||M|S||
|`import_shapefile.py`|Preprocessing|||M||
|`get_temperature.py`|Preprocessing|||S|M|
|`get_arrays.py`|Preprocessing|M||S||
|`anova.py`|Analysis|M||||
|`get_table.py`|Analysis||||M|
|`heatmap.py`|Postprocessing|M||||
|`individual_distributions.py`|Postprocessing||M|||
|`monthly_distributions.py`|Postprocessing||M|||
|`plot_trajectories.py`|Postprocessing||||M|
|`rasterplot.py`|Postprocessing|M||||
|`timeseries.py`|Postprocessing|||M||

**M** = Main contributor  
__S__ = Secondary contributor 

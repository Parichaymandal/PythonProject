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
|`goose_analysis.py`|Main|X<sup>(**)</sup>|X<sup>(**)</sup>|X<sup>(*)</sup>|X<sup>(**)</sup>|
|`stack_tiff.py`|Preprocessing|||X||
|`import_raster.py`|Preprocessing||X<sup>(*)</sup>|X<sup>(**)</sup>||
|`import_shapefile.py`|Preprocessing|||X||
|`get_temperature.py`|Preprocessing|||X<sup>(**)</sup>|X<sup>(*)</sup>|
|`get_arrays.py`|Preprocessing|X<sup>(*)</sup>||X<sup>(**)</sup>||
|`anova.py`|Analysis|X||||
|`get_table.py`|Analysis||||X|
|`heatmap.py`|Postprocessing|X||||
|`individual_distributions.py`|Postprocessing||X|||
|`monthly_distributions.py`|Postprocessing||X|||
|`plot_trajectories.py`|Postprocessing||||X|
|`rasterplot.py`|Postprocessing|X||||
|`timeseries.py`|Postprocessing|||X||

**X** = Single main contributor  
__X<sup>(*)</sup>__ = Main contributor  
__X<sup>(**)</sup>__ = Secondary contributor

# Different place... same temperature? Spatio-temporal analysis of white-fronted geese temperature trajectories

Carles Milà, Giulia Molisse, Sebastián Garzón, Parichay Mandal (2020).  
Westfälische Wilhelms-Universität. 

# Description

This repository contains the supplementary material required to reproduce the findings of the study *Spatio-temporal analysis of white-fronted geese temperature trajectories*.

# Software requirements
- Python 3
- QGIS (3.x any version)

# Manual for reproducibility

1. Clone this repository
2. Add `points.shp` and `lines.shp` of geese trajectories into `databases/shapefiles`. The GPS data used for this study must be requested from the authors on the [Movebank platform](https://www.datarepository.movebank.org/handle/10255/move.750). We are **not** authorized to distribute the dataset.
3. In file `goose_analysis.py` modify `project_folder` variable to the current location of this folder on your computer
4. Modify QGIS configuration for Python:
- Go to Settings -> Options
- In the window that appears, go to the tab *System*
- In that tab, go to the *Environment* section
- Check the box `Use custom variables`
- Add a variable `PYTHONPATH` and as the value add the `path` where your modules are located (same as `project_folder` from step 3)
- Restart QGIS
5. RUN `goose_analysis.py` script by using the QGIS - Python IDLE. After running the script figures of this study are going to be available in the `figures` folder.

  # Individual contributions
  
| Script name |  Section|  Carles | Giulia   | Sebastian | Parichay |
|:-------------:|:---------:|:---------:|:----------:|:---------:|:---------:|
|`goose_analysis.py`|Main|*S*|*S*|**M**|*S*|
|`stack_tiff.py`|Preprocessing||**M**|||
|`import_raster.py`|Preprocessing||**S**|**M**||
|`import_shapefile.py`|Preprocessing|||**M**||
|`get_temperature.py`|Preprocessing|||*S*|**M**|
|`get_arrays.py`|Preprocessing|**M**||*S*||
|`anova.py`|Analysis|**M**||||
|`get_table.py`|Analysis||||**M**|
|`get_summary.py`|Analysis||||**M**|
|`heatmap.py`|Postprocessing|**M**||||
|`individual_distributions.py`|Postprocessing||**M**|||
|`monthly_distributions.py`|Postprocessing||**M**|||
|`plot_trajectories.py`|Postprocessing||||**M**|
|`rasterplot.py`|Postprocessing|**M**||||
|`timeseries.py`|Postprocessing|||**M**||

**M** = Main contributor  
*S* = Secondary contributor 

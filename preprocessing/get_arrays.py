import numpy as np
from osgeo import gdal, ogr
from qgis.core import *
from qgis.PyQt.QtCore import QVariant

def extract_arrays(layer, excludeNone):
    '''Function to extract numpy arrays from a QgsVectorLayer for analysis
        
    Parameters
        ----------
        vectorlayer : qgis._core.QgsVectorLayer
            A point vector layer with the follwoing attributes:
                "TEMP", "month", "ind_ident"
        excludeNone : boolean
            A boolean indicated if None values for TEMP should be excluded in 
            all arrays

    Returns
        -------
        x: numpy.ndarray (float)
            longitude in WGS84
        y: numpy.ndarray (float)
            latitude in WGS84
        ids: numpy.ndarray (integer)
            bird identifiers
        months: numpy.ndarray (integer)
            month of the year of the measurement
        years: numpy.ndarray (integer)
            year of the measurement            
        temps: numpy.ndarray (integer)
            temperature (Kelvin) of the measurement
    
    '''
    # Extract data
    x = []
    y = []
    ids = []
    months = []
    years = []
    temps = []
    features = layer.getFeatures()
    for feat in features:
        # If we are asked to ignore records with NULL temperature
        if excludeNone:
            if feat['TEMP']:
                x.append(feat['long'])
                y.append(feat['lat'])
                ids.append(int(feat['ind_ident']))
                months.append(feat['month'])
                years.append(int(feat['time_str'][3:7]))
                temps.append(feat['TEMP'])
        # Otherwise take all
        else:
            x.append(feat['long'])
            y.append(feat['lat'])
            ids.append(feat['ind_ident'])
            months.append(feat['month'])
            years.append(int(feat['time_str'][3:7]))
            temps.append(feat['TEMP'])
            
    # Convert to array
    x = np.asarray(x)
    y = np.asarray(y)
    ids = np.asarray(ids)
    months = np.asarray(months)
    years = np.asarray(years)
    temps = np.asarray(temps)
    
    return x, y, ids, months, years, temps
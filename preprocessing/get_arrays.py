import numpy as np
from osgeo import gdal, ogr
from qgis.core import *
from qgis.PyQt.QtCore import QVariant
from datetime import datetime

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
        temps: numpy.ndarray (double)
            temperature (Celsius) of the measurement
    
    '''
    # Extract data
    x = []
    y = []
    timestamps=[]
    ids = []
    months = []
    years = []
    temps = []
    features = layer.getFeatures()
    for feat in features:
        # If we are asked to ignore records with NULL temperature
        if excludeNone:
            if feat['TEMP']>0:
                x.append(feat['long'])
                y.append(feat['lat'])
                timestamps.append(datetime.strptime(feat['timestamp'],"%Y-%m-%d %H:%M:%S"))
                ids.append(int(feat['ind_ident']))
                months.append(feat['month'])
                years.append(int(feat['time_str'][3:7]))
                temps.append(feat['TEMP'])
        # Otherwise take all
        else:
            x.append(feat['long'])
            y.append(feat['lat'])
            timestamps.append(datetime.strptime(feat['timestamp'],"%Y-%m-%d %H:%M:%S"))
            ids.append(feat['ind_ident'])
            months.append(feat['month'])
            years.append(int(feat['time_str'][3:7]))
            temps.append(feat['Temp']>0)
    
    # Convert to array
    x = np.asarray(x)
    y = np.asarray(y)
    timestamps=np.asarray(timestamps)
    ids = np.asarray(ids)
    months = np.asarray(months)
    years = np.asarray(years)
    temps = np.asarray(temps) - 273.15 # To celsius
    
    return x, y, ids, months, years, temps, timestamps

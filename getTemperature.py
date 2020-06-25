import pandas
import numpy as np
from osgeo import gdal, ogr


def latLon_to_XY(raster, lon, lat):
    '''
        Parameters:
        ____________
            raster: GDAL raster object
            lon: longitude
            lat: latitude
            
        Returns:
        ____________
            x,y: x and y coordinates corresponding to longitude and latitude
    '''
    gt = raster.GetGeoTransform()
    x0, y0 , width , hight = gt[0], gt[3], gt[1], gt[5]
    x = (lon - x0)/w
    y = (lat - y0)/h
    
    return x,y
    
def dateTimeStringToIndex(dateTime):
    
    '''
        Parameters
        ____________
            dateTime: string
                in "JAN2007" format
        
        Returns
        ____________
            index: integer
                corresponding band index to the dateTime
    '''
    monthDict={
    "JAN":1,
    "FEB":2,
    "MAR":3,
    "APR":4,
    "MAY":5,
    "JUN":6,
    "JUL":7,
    "AUG":8,
    "SEP":9,
    "OCT":10,
    "NOV":11,
    "DIC":12
    }
    
    yearDict = {
    "2007" : 0,
    "2008" : 1
    }
    month = dateTime[:3]
    year = dateTime[3:9]
    
    index = 12 * yearDict[year] + monthDict[month]
    
    return index
    
    

def getTemperature(path, x, y, dateTime, type = 'point'):
    
    '''
        Parameters
        ____________
            path: string
                directory of the .tif file
                
            x: float
                longitude/raster pixel x-coordinates
                
            y: float
                latitude/raster pixel y-coordinates
                
            dateTime: string
                in "JAN2007" format
                
            type: string
                determines if the point in cartesian x,y or geographical lat lon
    '''
    
    # Convert lon lat to raster pixel point
    if(type == 'geo'):
        x, y = latLon_to_XY(x,y)
    
    #Open raster file
    raster = gdal.Open(path)
    if(raster is None):
        print('Could not open raster file')
    
    # Obtain point value
    point_value = []
    for idx in range(raster.RasterCount):
        band = raster.GetRasterBand(idx+1)
        intval = band.ReadAsArray(y,x,1,1)
        point_value.append(intval[0,0])
        
    point_value = np.array(point_value)
    index = dateTimeStringToIndex(dateTime)
    
    band = raster.GetRasterBand(index)
    intval = band.ReadAsArray(y,x,1,1)
    
    #print(point_value)
    print(intval[0,0])
    
    return point_value[index-1]

# Usage
'''
path = '/Users/parichay/Desktop/Desktop/Academic/Semester2/PIG/PythonProject/databases/raster/raster.tif'
print(getTemperature(path,40,55,'DIC2008'))
'''
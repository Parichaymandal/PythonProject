import numpy as np
from osgeo import gdal, ogr
from qgis.core import *
from qgis.PyQt.QtCore import QVariant

def get_month_band_temperature(layerShp,rlayer):
    
    caps=layerShp.dataProvider().capabilities()
    
    # Check if the analysis columns are already in the file, if yes delete
    fields = layerShp.dataProvider().fields()
    index_remove = []
    i = 0
    for field in fields:
        fieldname = field.name()
        if fieldname in ["time_str", "raster", "TEMP"]:
            index_remove.append(i)
        i += 1
    if caps:
        if len(index_remove)>0:
            res = layerShp.dataProvider().deleteAttributes(index_remove)
    
    # Add new columns to the shapefile
    if caps & QgsVectorDataProvider.AddAttributes:
        res1=layerShp.dataProvider().addAttributes([QgsField("time_str",QVariant.String)])
        res2=layerShp.dataProvider().addAttributes([QgsField("raster",QVariant.String)])
        res3=layerShp.dataProvider().addAttributes([QgsField("TEMP",QVariant.String)])
        
    id=0
    yearValue=[]
    monthValue=[]
    idKey=[]
    long=[]
    lat=[]
    monthDict={"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DIC"}
    
    for featureSHP in layerShp.getFeatures():
        year=featureSHP["timestamp"][0:4]
        month=featureSHP["timestamp"][5:7]
        long_value=featureSHP["long"]
        lat_value=featureSHP["lat"]
        
        yearValue.append(year)
        monthValue.append(month)
        long.append(long_value)
        lat.append(lat_value)
        idKey.append(id)
        id+=1

    time_encode=[]
    rasterband=[]
    temperatures=[]
    
    for i in range(len(monthValue)):
        year=yearValue[i]
        month=monthDict[monthValue[i]]
        encode=month+year
        multiplier=1
        if year=="2008":
            multiplier=2
        band_num=int(monthValue[i])*multiplier
        
        x=long[i]
        y=lat[i]
        temp=str(get_temperature(rlayer,band_num,x,y,type='geo'))
        temperatures.append(temp)
        rasterband.append(band_num)
        time_encode.append(encode)
        
    if caps & QgsVectorDataProvider.AddAttributes:
        for i in idKey:
            attrs_time={13:time_encode[i]}
            dict_time={i:attrs_time}
            
            attrs_band={14:rasterband[i]}
            dict_band={i:attrs_band}
            
            attrs_temperature={15:temperatures[i]}
            dict_temperature={i:attrs_temperature}
            
            layerShp.dataProvider().changeAttributeValues(dict_time)
            layerShp.dataProvider().changeAttributeValues(dict_band)
            layerShp.dataProvider().changeAttributeValues(dict_temperature)
            
        layerShp.updateFields()

def latLon_to_XY(rlayer, lon, lat):
    '''
        Parameters:
        ____________
            rlayer: GDAL raster object
            lon: longitude
            lat: latitude
            
        Returns:
        ____________
            x,y: x and y coordinates corresponding to longitude and latitude
    '''
    gt = rlayer.GetGeoTransform()
    inv_gt=gdal.InvGeoTransform(gt)
    x,y=gdal.ApplyGeoTransform(inv_gt,lon,lat)

    return x,y
    

def get_temperature(rlayer,band_num,x,y,type='point'):
    
    '''
        Parameters
        ____________
            rlayer: GDAL raster object
                
            x: float
                longitude pixel x-coordinates
                
            y: float
                latitude pixel y-coordinates
                
            type: string
                determines if the point in cartesian x,y or geographical lat lon
    '''
    
    # Convert lon lat to raster pixel point

    if(type == 'geo'):
        x, y = latLon_to_XY(rlayer,x,y)
        
    # Obtain point value
   
    band = rlayer.GetRasterBand(band_num)
    info = band.ReadAsArray(x,y,1,1)

    if info is None:
        temp=0
    else:
        temp = info[0,0]
        if temp<0:
            temp=0
    return temp
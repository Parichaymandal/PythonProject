import os
import ogr

def importShapefile_ogr(path,geometry):
    
        """Loads the shapefile depending on the desired geometry (lines or points)

        Parameters
        ----------
        path : str
            path to shapefile folder
            
        geomtry:str
            desired geometry (lines or points)

        Returns
        -------
        osgeo.org.DataSource
            opened shapefile with ogr

    """
        if(geometry not in ("points","lines")):
                print("Geometry input not valid")
        else:
            geometry_file=geometry+".shp"
            print('### Opening %s ###' % geometry_file)
            shape_file=os.path.join(path,geometry_file)
            layerShp=iface.addVectorLayer(shape_file,"shape:","ogr")
            
            if not layerShp:
                print("Shapefile failed to load!")
            
            else:
                return(layerShp)


def add_time_band_columns(layerShp):
    
    caps=layerShp.dataProvider().capabilities()
    
    if caps & QgsVectorDataProvider.AddAttributes:
        res=layerShp.dataProvider().addAttributes([QgsField("time_str",QVariant.String)])
        res2=layerShp.dataProvider().addAttributes([QgsField("raster",QVariant.String)])
        
    id=0
    yearValue=[]
    monthValue=[]
    idKey=[]
    monthDict={"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DIC"}
    
    for featureSHP in layerShp.getFeatures():
        year=featureSHP["timestamp"][0:4]
        month=featureSHP["timestamp"][5:7]
        yearValue.append(year)
        monthValue.append(month)
        idKey.append(id)
        id+=1

    time_encode=[]
    rasterband=[]
    
    for i in range(len(monthValue)):
        year=yearValue[i]
        month=monthDict[monthValue[i]]
        encode=month+year
        multiplier=1
        if year=="2008":
            multiplier=2
        band=int(monthValue[i])*multiplier
        rasterband.append(band)
        time_encode.append(encode)
        
    if caps & QgsVectorDataProvider.AddAttributes:
        for i in idKey:
            attrs_time={13:time_encode[i]}
            dict_time={i:attrs_time}
            attrs_band={14:rasterband[i]}
            dict_band={i:attrs_band}
            layerShp.dataProvider().changeAttributeValues(dict_time)
            layerShp.dataProvider().changeAttributeValues(dict_band)
            layerShp.updateFields()
    return(layerShp)

# WWU - PIGis - SS2020

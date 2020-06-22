import os
import ogr


def importShapefile(path,geometry):
    
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

        shp_driver=ogr.GetDriverByName('ESRI Shapefile')
        shapefile=shp_driver.Open(shape_file,0)
        
        if not shapefile:
            print("Shapefile failed to load, they file may be missing!")
        else:
            layer=shapefile.GetLayer(0)
            attributes=layer.GetLayerDefn()
            numfeat=layer.GetFeatureCount()
            numatt=attributes.GetFieldCount()
            
            print('### Shapefile %s succesfully opened: %s features and %s attribute(s)' % (geometry_file, numfeat,numatt))
        return(shapefile)

# WWU - PIGis - SS2020

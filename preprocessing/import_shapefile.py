import os
import ogr
from qgis.utils import iface
from qgis.core import *

def import_shp(path,geometry):
    
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

# WWU - PIGis - SS2020

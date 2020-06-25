import os
import gdal 

# define function to load a raster 
def import_raster(path):
    
    '''
    Loads a raster with gdal
    -----
    Parameters:
    Path -> string
    '''
    
    rlayer = gdal.Open(path)
    if not rlayer:
        print ('Layer failed to load! The path might be wrong')
    else:
        print ('the raster is loaded!')
        get_raster_info(rlayer)
    return rlayer

# define function to get general info from the raster

def get_raster_info(rlayer):
    
    '''
    calls loadrast() function and prints general information about the multiband raster
    ----
    Parameters:
    rlayer -> gdal open layer
    ----
    Prints:
    Number of colums and rows;
    Raster projection
    '''
    coln = rlayer.RasterXSize
    rows = rlayer.RasterYSize
    
    print('Columns:', coln, 'Rows', rows)

    rast_spatial_ref = rlayer.GetProjection()
    print('Raster spatial ref is', rast_spatial_ref)

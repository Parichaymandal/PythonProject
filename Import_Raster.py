import os
import gdal 

# place here your path to the multiband raster
path = os.path.join('C://', 'Users', 'Giulia', 'Desktop', 'tif_folder','stacked.vrt')


# define function to load the raster 
def loadrast(path):
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
    return rlayer
 
# uncomment below to call loadrast() function 
loadrast(path)  


# define function to get general info from the raster
def getrastinfo(path):
    '''
    calls loadrast() function and prints general information about the multiband raster
    ----
    Parameters:
    path -> string
    ----
    Returns:
    number of colums and rows;
    for each band: band number, No Data Value, Minimum Value, Maximum Value
    '''
    # call the function to load the raster
    rlayer=loadrast(path)
    # show 
    coln = rlayer.RasterXSize
    rows = rlayer.RasterYSize
    print('raster columns:', coln, 'raster rows', rows)
    # low let's loop through every band and get min and max value
    for band in range(1,25):
        searchband = rlayer.GetRasterBand(band)
        print ('\nwe are at band number:', band)
        print ('NoDataValue', searchband.GetNoDataValue())
        print ('MinValue', searchband.GetMinimum())
        print ('MaxValue', searchband.GetMaximum())
    return searchband

# uncomment below to call getrastinfo() function
getrastinfo(path)



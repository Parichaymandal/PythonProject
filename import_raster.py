import os
import gdal 

# place here your path to the multiband raster
path = os.path.join('C:\\', 'Users','Giulia','Desktop','raster_output','24MonthsStack.vrt')


# define function to load the raster 
def loadrast(path):
    rlayer = gdal.Open(path)
    if not rlayer:
        print ('Layer failed to load! The path might be wrong')
    else:
        print ('the raster is loaded!')
    return rlayer
 
# uncomment below to call loadrast() function 
#loadrast(path)  


# define function to get general info from the raster
def getrastinfo(path):
    # call the function to load the raster
    loadrast(path)
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
# getrastinfo(path)



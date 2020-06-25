import gdal
import os

# write here your path to the tifs folder
tif_fold = os.path.join('databases','raster')

def SingleTifToStacked(tif_fold):
    '''
    this function takes a list of single band tifs and transform them into:
    - first, a stacked .vrt
    - second, a stacked multiband .tif
    
    ----
    Parameters:
    tif_fold -> string
    
    ----
    Returns:
    .vrt and .tif
    '''
    # path of files location 
    filenames = ['01.2007.tif','02.2007.tif','03.2007.tif','04.2007.tif','05.2007.tif','06.2007.tif','07.2007.tif','08.2007.tif',
    '09.2007.tif','10.2007.tif','11.2007.tif','12.2007.tif','01.2008.tif','02.2008.tif','03.2008.tif','04.2008.tif','05.2008.tif',
    '06.2008.tif','07.2008.tif','08.2008.tif','09.2008.tif','10.2008.tif','11.2008.tif','12.2008.tif']
    # loop through each tif in the folder
    tifs = [os.path.join(tif_fold, road) for road in filenames]
    
    # output location for vrt file
    outvrt_fold = os.path.join(tif_fold, 'stacked.vrt') 
    # stack list of tifs into vrt file
    outvrt = gdal.BuildVRT(outvrt_fold, tifs, separate=True)
    # output location for tif file
    outtif_fold = os.path.join (tif_fold, 'stacked.tif')
    # converts vrt into tif
    outtif = gdal.Translate(outtif_fold, outvrt)
    
    return print ('.vrt and .tif created', outvrt, outtif) 
    
# uncomment below to run the function
# SingleTifToStacked(tif_fold) 

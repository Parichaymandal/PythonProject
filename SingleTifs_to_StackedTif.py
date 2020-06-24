import gdal
import os

# path of files location 
fold_path = os.path.join('C://', 'Users', 'Giulia', 'Desktop', 'tif_folder')

filenames = ['01.2007.tif','02.2007.tif','03.2007.tif','04.2007.tif','05.2007.tif','06.2007.tif','07.2007.tif','08.2007.tif',
'09.2007.tif','10.2007.tif','11.2007.tif','12.2007.tif','01.2008.tif','02.2008.tif','03.2008.tif','04.2008.tif','05.2008.tif',
'06.2008.tif','07.2008.tif','08.2008.tif','09.2008.tif','10.2008.tif','11.2008.tif','12.2008.tif']
tifs = [os.path.join(fold_path, road) for road in filenames]

# output location for vrt file
outvrt = os.path.join('C://', 'Users', 'Giulia', 'Desktop', 'tif_folder', 'stacked.vrt') 
# stack list of tifs into vrt file
outds = gdal.BuildVRT(outvrt, tifs, separate=True)

# output location for tif file
outtif = os.path.join ('C://', 'Users', 'Giulia', 'Desktop', 'tif_folder', 'stacked.tif')
# converts vrt into tif
outds = gdal.Translate(outtif, outds)
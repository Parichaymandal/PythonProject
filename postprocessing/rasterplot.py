import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import math


def plot_temp_rasters(rstack, minr, maxr, path):
    """Function to map monthly temperature rasters""
    
    Parameters
        ----------
        rstack: osgeo.gdal.Dataset
            Stack of temperature rasters
        minr: integer
            Minimum for the temperature range colour ramp
        maxr: integer
            Maximum for the temperature range colour ramp
        path: string
            path where to export the figure
    """    
    # Create fake figure to extract common colour scale for later
    fig1, ax1 = plt.subplots()
    im = plt.imshow(np.array([[minr, maxr],[minr, maxr]]),
                    cmap = cm.coolwarm, vmin=minr, vmax=maxr)
    plt.close()

    # Create figure
    fig, axes = plt.subplots(6, 4, figsize=(14, 10), sharex=True, sharey=True)

    for m in range(24):
        
        m2 = m+1
        
        # Read band
        band = rstack.GetRasterBand(m2)
        temp = band.ReadAsArray()
        temp = temp-272.15
        
        # Filter sea, drop empty rows/columns, convert to celsius
        temp[temp == temp.min()] = None
        temp = temp[5:,17:]
        
        # Map!
        rowplot = math.ceil(m2/4)-1
        colplot = (m2-1)%4
        axes[rowplot, colplot].imshow(temp, cmap = cm.coolwarm,
                                      vmin=minr, vmax=maxr)
        
        # Subplot title, with some index trickery
        year = math.floor((m2-1)/12) + 2007
        month = (m2-1)%12 +1
        axes[rowplot, colplot].set_title(str(month) + '-' + str(year))

    # Final touches to the map
    fig.colorbar(im, ax=axes.ravel().tolist())
    fig.suptitle('Monthly mean temperature rasters (ºC)', fontsize=16)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(path)
    plt.show()

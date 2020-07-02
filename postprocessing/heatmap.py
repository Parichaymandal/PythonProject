import numpy as np
from matplotlib import pyplot as plt
import math

# Heatmap algorithm adapted from:
# https://www.geodose.com/2018/01/creating-heatmap-in-python-from-scratch.html

#DEFINE GRID SIZE AND RADIUS(h)
grid_size=1
radius=10

def monthly_heatmap(x, y, month, grid_size, h, path):
    """Function to compute a monthly heatmap""
    
    Parameters
        ----------
        y: numpy.ndarray (float)
            1-dimensional numpy array with x coordinates
        x: numpy.ndarray (float)
            1-dimensional numpy array with y coordinates
        month : numpy.ndarray (integer)
            1-dimensional numpy array with month identifiers
        grid_size: integer
            size of the raster in which density will be computed
        h: integer
            neighbourhood radius to compute density
        path: string
            path where to export the heatmap figure
    """
    
    
    print("Processing heatmap...")
    
    # We get data boundaries
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    
    # We construct a raster for the output
    x_grid=np.arange(x_min-h,x_max+h,grid_size)
    y_grid=np.arange(y_min-h,y_max+h,grid_size)
    x_mesh, y_mesh=np.meshgrid(x_grid,y_grid)
    
    # Centre point of the grid
    xc=x_mesh+(grid_size/2)
    yc=y_mesh+(grid_size/2)
    
    # Heatmap plot
    fig, axes = plt.subplots(3, 4, figsize=(16, 10), sharex=True, sharey=True)
    
    # Loop by month
    for m in range(1,13):
                
        # Loop by feature
        x_plot = []
        y_plot = []
        for index in range(len(x)):
            # Extract those of the corresponding months
            if month[index] == m:
                x_plot.append(x[index])
                y_plot.append(y[index])
                
        # Processing
        intensity_list=[]
        for j in range(len(xc)):
            intensity_row=[]
            for k in range(len(xc[0])):
                kde_value_list=[]
                for i in range(len(x_plot)):
                    # Calculate distance
                    d=math.sqrt((xc[j][k]-x_plot[i])**2+(yc[j][k]-y_plot[i])**2) 
                    # If distance is within radius
                    if d<=h:
                        p=kde_quartic(d,h)
                    else:
                        p=0
                    kde_value_list.append(p)
                # Sum intensity values
                p_total=sum(kde_value_list)
                intensity_row.append(p_total)
            intensity_list.append(intensity_row)
    
        # Plot
        intensity = np.array(intensity_list)
        rowplot = math.ceil(m/4)-1
        colplot = (m-1)%4
        axes[rowplot,colplot].pcolormesh(x_mesh, y_mesh, intensity)
        axes[rowplot,colplot].set_title("Month: " + str(m))
    
    # Add general labels, show and write to disk
    fig.text(0.5, 0.06, 'longitude', ha='center')
    fig.text(0.09, 0.5, 'latitude', va='center', rotation='vertical')
    fig.show()
    plt.savefig(path)
    
    print("Heatmap successfully exported!")
    
    

# Quartic Kernel function
def kde_quartic(d,h):
    """Compute kernel density (quartic function)
    Parameters
        ----------
        d : float
            distance from point to cell
        h : float
            neighbourhood radius
    """
    
    dn = d/h
    P = (15/16)*(1-dn**2)**2
    return P

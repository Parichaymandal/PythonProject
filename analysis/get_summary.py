import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def get_sum(ids,years,temps, path):
    
    '''
    Calculates and plots the table of the mean, max, and min temperatures per individual
        
        Parameters:
        ____________
            ids: 1D np.array 
                Array of goose ids
            years: 1D np.array
                Array of years of all the datas
            temps: 1D np.array
                Array of temperatures
            path: string
                where the figure going to be saved
    
    '''
    
    # construct a dataframe from the values
    data  = pd.DataFrame({'ids': ids, 'years': years, 'temp': temps})
    # aggregate data
    data = data.groupby('ids').agg({'years': ( lambda x: x.unique().tolist()),'temp': [np.mean, 'max','min']})
    # reshape years column
    yrs = np.array(data['years']).reshape(7,)
    
    # construct the table
    table = pd.DataFrame({'Recorded Year': yrs,'Mean Temp C': np.round(data['temp']['mean'], 2),'Max Temp C': np.round(data['temp']['max'], 2), 'Min Temp C': np.round(data['temp']['min'],2)})    
    # Defining rows and columns color
    row_colors = plt.cm.BuPu(np.linspace(0, 0.5, len(table.index)))
    col_colors = plt.cm.BuPu(np.linspace(0.5, 0.5, len(table.columns)))
    
    # Plotting setup
    fig, ax = plt.subplots(figsize=(8,4))
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    
    # Plot and save
    ax.table(cellText=table.values, colLabels=table.columns, rowLabels = table.index,rowColours = row_colors, colColours= col_colors, loc='center')
    fig.tight_layout()
    plt.show()
    plt.savefig(path)
    

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def get_table(ids,years, months, temps):
    '''
        Calculates the mean temperatures per individual per month
        
        Parameters:
        ____________
            ids: 1D np.array 
                Array of goose ids
            years: 1D np.array
                Array of years of all the datas
            months: 1D np.array
                Array of years of all the data
            temps: 1D np.array
                Array of temperatures
                
        Returns:
        __________
            month/individual dataframe 
    '''
    # Make dataframe from input parameters
    data  = pd.DataFrame({'ids': ids,'months': months, 'years': years, 'temp': temps})
    # Get all unique goose ids
    unique_ids = list(np.unique(data['ids']))
    # Get unique months
    unique_months = list(np.unique(data['months']))
    # Get unique years
    unique_years = list(np.unique(data['years']))
    
    # Create a np.array with the colums for individual goose, rows for months (months per year * year)
    temperature = np.zeros((len(unique_ids),len(unique_months)*len(unique_years)))
    
    # calculate and aggregate mean temperature for each goose for each month
    for year in range(len(unique_years)):
        year_data = data[data['years'] == unique_years[year]]
        i = 0
        for id in unique_ids:
            #Aggregating
            temp_data = year_data[year_data['ids']== id]
            temp_data = temp_data.groupby('months').agg({'temp': 'mean'})
            temp_data.columns = ['temp']
            
            #Filling temperature array
            for j in range(12*year, (year+1) * 12, 1):
                try:
                  temperature[i,j] = np.round(temp_data['temp'][j%12+1], 2)
                except:
                  temperature[i,j] = None
            i = i +1      
    
    #Creating a row labels for the dataframe    
    row_labels = []
    for year in range(len(unique_years)):
        for month in unique_months:
            row_labels.append(month + year*12)
    
    #Constructing the dataframe
    df = pd.DataFrame(data= temperature.T,    # values
                index= row_labels,    # 1st column as index
                columns= unique_ids)
                
    #Returns dataframe
    return df
    
def plot_table(ids,years, months, temps, path):
    '''
    Plot the table of the mean temperatures per individual per month
        
        Parameters:
        ____________
            ids: 1D np.array 
                Array of goose ids
            years: 1D np.array
                Array of years of all the datas
            months: 1D np.array
                Array of years of all the data
            temps: 1D np.array
                Array of temperatures
            path: string
                directory, where the figure going to be saved
    
    '''
    
    # Get month/individual dataframe 
    dataframe = get_table(ids,years, months, temps)
    
    # Construct dictionaries to replace numeric vallues to string month/year names
    month_dict = { 1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY', 6:'JUN', 7:'JUL', 8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}
    year = ['2007','2008']
    
    # Contructing string row indexes
    rows = []
    for row in range(len(dataframe.index)):
        yr = year[int (row / 13)]
        mon = month_dict[(row % 12) +1]
        rows.append(mon +yr)
    
    # Defining rows and columns color
    row_colors = plt.cm.BuPu(np.linspace(0, 0.5, len(dataframe.index)))
    col_colors = plt.cm.BuPu(np.linspace(0.5, 0.5, len(dataframe.columns)))
    
    # Plotting setup
    fig, ax = plt.subplots(figsize=(12, 6))
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    
    # Plot and save
    ax.table(cellText=dataframe.values, colLabels=dataframe.columns, rowLabels = rows,rowColours = row_colors, colColours= col_colors, loc='center')
    fig.tight_layout()
    plt.show()
    plt.savefig(path)
    
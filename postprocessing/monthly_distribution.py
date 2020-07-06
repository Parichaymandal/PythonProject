import plotly.graph_objs as go
from plotly.colors import n_colors
import plotly.offline as pyo
import numpy as np


def monthly_distribution(sample_year, months, years, temps, monthly_path):
    '''
    Function to compute the monthly temperature distribution
    
    Parameters
        ----------
        sample_year: year of your choice (integer)
            it is either 2007 or 2008
        months : numpy.ndarray (integer)
            1-dimensional numpy array with month identifiers
        temps: numpy.ndarray (integer)
            temperature (Celsius) of the measurement
        years: numpy.ndarray (integer)
            year of the measurement
        monthly_path: string
            path where to export the distribution in .html
    '''
    
    unique_months = np.unique(months)
    names = ['Jan. {y}'.format(y = sample_year),'Feb. {y}'.format(y = sample_year),
            'Mar. {y}'.format(y = sample_year), 'Apr. {y}'.format(y = sample_year), 
            'May {y}'.format(y = sample_year), 'Jun. {y}'.format(y = sample_year),
            'Jul. {y}'.format(y = sample_year),'Aug. {y}'.format(y = sample_year),
            'Sept. {y}'.format(y = sample_year), 'Oct. {y}'.format(y = sample_year),
            'Nov. {y}'.format(y = sample_year), 'Dec. {y}'.format(y = sample_year)]                
    colors = n_colors('rgb(10, 200, 197)', 'rgb(10, 200, 197)', 12, colortype='rgb')    
    fig = go.Figure()
    for month, color, name in zip(unique_months, colors, names):
        fig.add_trace(go.Violin(x=temps[((months== month)& (years== sample_year)).nonzero()[0]], line=dict(color=color),
                                orientation = 'h', side='positive', points=False,
                                name=name))
    fig.layout.update(title='Distribution of Monthly Temperatures ({y})'.format(y = sample_year),
                   xaxis=dict(title="Temperature (C°)") )
    pyo.plot(fig, filename=monthly_path)
 
# uncomment to test this function 
# monthly_distribution(2007, months, years, temps, os.path.join('monthly_path')) 

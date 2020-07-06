import plotly.graph_objs as go
from plotly.colors import n_colors
import plotly.offline as pyo
import numpy as np


def individuals_distribution(ids, temps, ind_path):
    unique_ids = np.unique(ids)
    names = ["Goose 72364", "Goose 72413", "Goose 72417", "Goose 73053",
            "Goose 73054", "Goose 79694", "Goose 79698"]                
    colors = n_colors('rgb(85, 116, 0)', 'rgb(85, 116, 0)', 7, colortype='rgb')    
    fig = go.Figure()
    for goose, color,name in zip(unique_ids, colors, names):
        fig.add_trace(go.Violin(x=temps[ids == goose], line=dict(color=color),
                                orientation = 'h', side='positive', points=False,
                                name=name))
    fig.layout.update(title='Distribution of Individual Temperatures ',
                    xaxis=dict(title="Temperature (C°)") )
    
    pyo.plot(fig, filename=ind_path)
  
# uncomment to test this function  
# individuals_distribution(ids, temps, os.path.join('C:\\','Users','Giulia','Desktop','PythonProject','distribution_individuals.html')) 


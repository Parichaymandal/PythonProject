##############################################################################
#                          Repeated mesures ANOVA                            #  
##############################################################################

import numpy as np

def repeated_measures_oneway_anova(y, x, i):
    """Function to compute repeated measures one-way ANOVA for a variably y 
    with groups x, in which each individual i is measures several times."""
    
    # Data checks: numpy array
    if type(y) != np.ndarray or type(x) != np.ndarray or type(i) != np.ndarray:
        raise Exception('Inputs must be of type numpy.ndarray')
    
    # Data checks: Same length
    if len(list(set([len(x), len(y), len(i)]))) != 1:
        raise Exception('Input arrays must have the same length')
            
    # Total sum of squares (SST)
    mean_all = np.mean(y)
    SST = np.sum((y-mean_all)**2)
    print('SST: '+ str(SST))
    
    # Between sum of squares (SSB)
    mean_x = []
    n_i = len(set(i))
    for s in np.unique(x):
        tmp = y[np.where(x == s)]
        mean_x.append(np.mean(tmp))
    SSB = np.sum(n_i * ((mean_x-mean_all)**2))
    print('SSB: '+ str(SSB))
        
    # Within sum of squares (SSW)
    mean_w = {}
    for t in np.unique(x):
        tmp = y[np.where(x == t)]
        mean_w[t] = np.mean(tmp)
    ss_w = []
    for u in range(y.shape[0]):
        ss_w.append((y[u] - mean_w[x[u]])**2)
    SSW = np.sum(ss_w)    
    print('SSW: '+ str(SSW))
        
    # Subject sum of squares (SSS)
    mean_i = []
    n_x = len(set(x))
    for v in np.unique(i):
        tmp = y[np.where(i == v)]
        mean_i.append(np.mean(tmp))
    SSS = np.sum(n_x * ((mean_i-mean_all)**2))
    print('SSS: '+ str(SSS))
    
    # Error variability (SSE)
    SSE = SSW - SSS 
    print('SSR: '+ str(SSE))
        
    # F statistic
    MSB = SSB/(n_x-1)
    MSE  = SSE/((n_x-1)*(n_i-1))
    F = MSB/MSE
    print('F: ' + str(F))
    
    # Contrast (F distribution)
    
    # Return results

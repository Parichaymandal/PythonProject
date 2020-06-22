##############################################################################
#                          Repeated mesures ANOVA                            #  
##############################################################################

import numpy as np

# Create fake month indicators for testing
np.random.seed(seed = 1234)
month = np.repeat(np.arange(1,13,1), 10)

# Create fake individual indicators for testing
ind = []
for i in range(1,13):
    ind.append(list(range(1, 11)))
ind = np.array(ind).flatten()    

# Create temperature data for testing
temp = np.random.normal(size = len (month))

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
    n_x = len(set(x))
    for s in np.unique(x):
        tmp = y[np.where(x == s)]
        mean_x.append(np.mean(tmp))
    SSB = np.sum(n_x * (mean_x-mean_all)**2)
    print('SSB: '+ str(SSB))
        
    # Within sum of squares (SSW)
    mean_w = {}
    for s in np.unique(i):
        tmp = y[np.where(i == s)]
        mean_w[s] = (np.mean(tmp))
    ss_w = []
    for r in range(y.shape[0]):
         ss_w.append((y[r] - mean_w[i[r]])**2)
    SSW = np.sum(ss_w)    
    print('SSW: '+ str(SSW))
    
    # Subject variability (SSS)
    
    # Residual variability (RSS)
    
    # Checks
    
    # F statistic
    
    # Contrast
    
    # Results


# Check function
repeated_measures_oneway_anova(temp, month, ind)

import numpy as np
from scipy.stats import f

def repeated_measures_oneway_anova(y, x, i):
    """Function to compute repeated measures one-way ANOVA for a variable y 
    with groups x, in which each individual i is measured several times.
    
    Parameters
        ----------
        y : numpy.ndarray
            1-dimensional numpy array with outcome measurements
        x : numpy.ndarray
            1-dimensional numpy array with group indentifiers
        i : numpy.ndarray
            1-dimensional numpy array with individual indentifiers

        Returns
        -------
        F: numpy.float64
            F test statistic
        pval: numpy.float64
            P-value of the test
    """
    
    # Running message
    print('Computing repeated measures anova analysis:')
    
    # Data checks: numpy array
    if type(y) != np.ndarray or type(x) != np.ndarray or type(i) != np.ndarray:
        raise Exception('Inputs must be of type numpy.ndarray')
    
    # Data checks: Same length
    if len(list(set([len(x), len(y), len(i)]))) != 1:
        raise Exception('Input arrays must have the same length')
            
    # Total sum of squares (SST)
    mean_all = np.mean(y)
    SST = np.sum((y-mean_all)**2)
    print('SST: '+ str(round(SST,2)))
    
    # Between sum of squares (SSB)
    mean_x = []
    n_i = len(set(i))
    for s in np.unique(x):
        tmp = y[np.where(x == s)]
        mean_x.append(np.mean(tmp))
    SSB = np.sum(n_i * ((mean_x-mean_all)**2))
    print('SSB: '+ str(round(SSB, 2)))
        
    # Within sum of squares (SSW)
    mean_w = {}
    for t in np.unique(x):
        tmp = y[np.where(x == t)]
        mean_w[t] = np.mean(tmp)
    ss_w = []
    for u in range(y.shape[0]):
        ss_w.append((y[u] - mean_w[x[u]])**2)
    SSW = np.sum(ss_w)    
    print('SSW: '+ str(round(SSW, 2)))
        
    # Subject sum of squares (SSS)
    mean_i = []
    n_x = len(set(x))
    for v in np.unique(i):
        tmp = y[np.where(i == v)]
        mean_i.append(np.mean(tmp))
    SSS = np.sum(n_x * ((mean_i-mean_all)**2))
    print('SSS: '+ str(round(SSS, 2)))
    
    # Error variability (SSE)
    SSE = SSW - SSS 
    print('SSR: '+ str(round(SSE, 2)))
        
    # F statistic
    df1 = n_x-1
    MSB = SSB/df1
    df2 = (n_x-1)*(n_i-1)
    MSE  = SSE/df2
    F = MSB/MSE
    print('F: ' + str(round(F, 2)))
    
    # Compute p-value (F distribution)
    pval = 1-f.cdf(F, df1, df2)
    print('p-value: '+ str(round(pval, 4)))
    
    # Return results
    return F, pval

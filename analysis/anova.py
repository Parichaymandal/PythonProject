import numpy as np
from scipy.stats import f
from matplotlib import pyplot as plt

def seasonal_individual_averages(y, x, i):
    """Function that computes grouped averages of y by factors x (month) and i
    (individual identifier). x are considered to be months and are grouped 
    according to meteorological seasons (Northern Hemisphere)
    
    Parameters
        ----------
        y : numpy.ndarray
            1-dimensional numpy array with outcome measurements
        x : numpy.ndarray
            1-dimensional numpy array with month indentifiers
        i : numpy.ndarray
            1-dimensional numpy array with individual indentifiers

        Returns
        -------
        y_avg : numpy.ndarray
            outcome averages by season and identifier
        x_avg : numpy.ndarray
            season identifiers
        i_avg : numpy.ndarray
            individual identifiers
            
    """
    y_avg = []
    x_avg = []
    i_avg = []
    
    # Loop through all unique values for x and i
    for xi in ['winter', 'spring', 'summer', 'autumn']:
        for ii in np.unique(i):
            y_mean = []
            # Loop through all elements of the array
            for k in range(len(y)):
                if xi == 'winter':
                    if x[k] in [12,1,2] and i[k] == ii:
                        y_mean.append(y[k])
                elif xi == 'spring':
                    if x[k] in [3,4,5] and i[k] == ii:
                        y_mean.append(y[k])
                elif xi == 'summer':
                    if x[k] in [6,7,8] and i[k] == ii:
                        y_mean.append(y[k])
                elif xi == 'autumn':
                    if x[k] in [9,10,11] and i[k] == ii:
                        y_mean.append(y[k])
            # Calculate mean
            y_mean = np.mean(y_mean)
            # And store results
            y_avg.append(y_mean)
            x_avg.append(xi)
            i_avg.append(ii)
    
    # Convert to array and return results
    y_avg = np.array(y_avg)
    x_avg = np.array(x_avg)
    i_avg = np.array(i_avg)
    
    return y_avg, x_avg, i_avg
    

def repeated_measures_oneway_anova(y, x, i, path):
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
    print('Computing repeated measures anova analysis...')
    
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
    
    # Call plot function
    anova_plot(y, x, i, df1, df2, F, path)
    
    # Return results
    return F, pval

def anova_plot(y, x, i, df1, df2, F, path):
    """Function to do a plot of the ANOVA results
    
    Parameters
        ----------
        y : numpy.ndarray
            1-dimensional numpy array with outcome measurements
        x : numpy.ndarray
            1-dimensional numpy array with group indentifiers
        i : numpy.ndarray
            1-dimensional numpy array with individual indentifiers
        df1: integer
            degrees of freedom of the numerator
        df2: integer
            degrees of freedom of the denominator
        F: float
            test statistic
        path: string
            path to write figure to disk
    """
    # ANOVA plot
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    # 1st plot: Assumptions
    axes[0].hist(y, bins = 'auto')
    axes[0].set_title('ANOVA assumptions:\nNormality and outliers')
    # 2nd plot: Boxplots
    yplot = []
    xplot = [] 
    for xi in np.unique(x):
        ysub = []
        for k in range(len(y)):
            if x[k] == xi:
                ysub.append(y[k])
        xplot.append(xi)
        yplot.append(ysub)
    
    axes[1].boxplot(yplot)
    axes[1].set_xticklabels(xplot)
    axes[1].boxplot(yplot)
    axes[1].set_title('ANOVA exploration:\nSeasonal boxplots')
    # 3th plot: Result
    # Derive pdf of the F distribution
    x_dist = np.linspace(f.ppf(0.01, df1, df2),
                         f.ppf(0.99, df1, df2), 100)
    rv = f(df1, df2)
    # Find critical value for distribution
    x_vals = rv.pdf(x_dist)
    crit = min(abs(x_vals-0.05))
    crit = x_dist[np.min(np.where(abs(x_vals-0.05)==crit))]
    # Plot
    axes[2].plot(x_dist, x_vals, 'k-', lw=2, label='Test F distribution')
    axes[2].axvline(x = F, label='Observed statistic', c = 'blue')
    axes[2].axvline(x = crit, label='Critical value', c = 'red')
    axes[2].set_title('ANOVA test results:\nStatistic and critical value')    
    
    plt.legend()
    fig.show()
    plt.savefig(path)

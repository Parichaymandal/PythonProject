import numpy as np
import matplotlib.pyplot as plt

def plot_timeseries(ids,timestamps,temps,file_path):

    array_timeseries=np.array([ids,timestamps,temps])
    unique_ids=list(np.unique(array_timeseries[0,]))
    max_temp=max(temps)
    min_temp=min(temps)
    average=np.average(temps)
    plt.figure(figsize=(14,8))
    for i in unique_ids:
        
        goose=array_timeseries[:,array_timeseries[0,:]==i]
        time=goose[1,]
        temp=goose[2,]
        label_text="Goose "+str(i)
        plt.plot(time,temp,c=np.random.rand(3,),label=label_text)
        plt.ylim(min_temp-20,max_temp+20)
    plot_title="Geese Temperature time series"
    plt.ylabel("Temperature (ºC)")
    plt.xlabel("Time")
    plt.title(plot_title,size=20)
    plt.axhline(y=max_temp, color='grey', linestyle='dashed',label="Max")
    plt.axhline(y=average, color='red', linestyle='dashed',label="Average")
    plt.axhline(y=min_temp, color='grey', linestyle='dashed',label="Min")
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1),
          ncol=3, fancybox=True, shadow=True)
    plt.savefig(file_path, bbox_inches='tight')
    plt.show()

    return(array_timeseries)

# Test data

bimonthly_days = np.arange(0, 60)
base_date = np.datetime64('2017-01-01 00:00:00')
timestamps = base_date + bimonthly_days

temps = np.random.rand(60,)*40-20
ids=np.repeat((1,2,3,4,5,6),10)

plot_timeseries(ids,timestamps,temps,'test_timeseries_geese.png')

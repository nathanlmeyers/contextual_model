from ops.db_utils import plot_db
import numpy as np
import pandas as pd
import pandas.plotting
from pandas.plotting import scatter_matrix
# import matplotlib
# import pylab as plt
import matplotlib
matplotlib.use('Agg') #comment/uncomment if running remotely
import matplotlib.pyplot as plt
import sys
table = sys.argv[1]

# Get the data from the db
cors = pd.DataFrame(np.array(plot_db(table))).loc[:,8:15].convert_objects(convert_numeric=True)
prams = pd.DataFrame(np.array(plot_db(table))).loc[:,2:7].convert_objects(convert_numeric=True)
means = cors.mean(axis=1)
mins = cors.min(axis=1)
import ipdb; ipdb.set_trace()
# Get the data from the manuscript
manu = pd.DataFrame(np.genfromtxt('manu_data.csv',delimiter=","))
manu_means = manu.loc[:,8:15].mean(axis=1)
manu_mins = manu.loc[:,8:15].min(axis=1)

plt_len = max(len(manu_means),len(means))

plt.figure()
plt.plot(manu_means, 'ro', markersize = 0.3)
plt.plot(means[:-1], 'ko', markersize = 0.5)
plt.plot((0,plt_len), (np.max(manu_means), np.max(manu_means)), 'r-')
plt.plot((0,plt_len), (np.max(means[:-1]), np.max(means[:-1])), 'k-')
plt.xlabel("Iteration")
plt.ylabel("Average Correlation")
plt.ylim((0.5,0.02+np.min([np.max([np.max(manu_means),np.max(means[:-1])])])))
plt.legend(['Manu Best Average','Bayes Best Average', 'Manu Iterations', 'Bayes Iterations'],loc=4)
plt.savefig('figures/perf_mean_'+table+'.png')

plt.figure()
plt_len = max(len(manu_mins),len(mins))
plt.plot(manu_mins, 'ro', markersize = 0.3)
plt.plot(mins[:-10], 'ko', markersize = 0.5)
plt.plot((0,plt_len), (np.max(manu_mins), np.max(manu_mins)), 'r-')
plt.plot((0,plt_len), (np.max(mins[:-10]), np.max(mins[:-10])), 'k-')
plt.xlabel("Iteration")
plt.ylabel("Min Correlation")
plt.ylim((-0.2,0.02+np.min([np.max([np.max(manu_mins),np.max(mins[:-1])])])))
plt.legend(['Manu Best Min','Bayes Best Min', 'Manu Iterations', 'Bayes Iterations'],loc=4)
plt.savefig('figures/perf_min_'+table+'.png')
plt.clf()

plt.figure()
prams.columns = ['alpha','beta','mu','nu','gamma','delta']
scatter_matrix(prams, alpha=0.1, figsize=(6, 6), diagonal='kde')
plt.savefig('figures/scatter_'+table+'.png')
plt.clf()

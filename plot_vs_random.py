from ops.db_utils import plot_db
import numpy as np
import pandas as pd
# import matplotlib
# import pylab as plt
import matplotlib
matplotlib.use('Agg') #comment/uncomment if running remotely
import matplotlib.pyplot as plt

# Get the data from the db
swag = plot_db('bayes_opt_all')
swag_df = pd.DataFrame(np.array(swag))
means = swag_df.loc[:,8:15].drop(12,axis = 1).mean(axis=1)
means = means.drop(647)
swag2 = plot_db('bayes_opt_min10')
swag2_df = pd.DataFrame(np.array(swag2))
mins = swag2_df.loc[:,8:15].drop(12,axis = 1).min(axis=1)

# Get the data from the manuscript
manu = pd.DataFrame(np.genfromtxt('manu_data.csv',delimiter=","))
manu_means = manu.loc[:,8:15].drop(12,axis = 1).mean(axis=1)
manu_mins = manu.loc[:,8:15].drop(12,axis = 1).min(axis=1)
### Uncomment for individual figure performance plots
# perf_f3a = swag_df[[8]]
# perf_f3b = swag_df[[9]]
# perf_f4 = swag_df[[10]]
# perf_f5 = swag_df[[11]]
# perf_tbp = swag_df[[13]]
# perf_tbtcso = swag_df[[14]]
# perf_bw = swag_df[[15]]
# plt.plot(perf_f3a)
# plt.plot(perf_f3b)
# plt.plot(perf_f4)
# plt.plot(perf_f5)
# plt.plot(perf_tbp)
# plt.plot(perf_tbtcso)
# plt.plot(perf_bw)
# plt.plot(means[:-1], linewidth=3, color='black')
# plt.xlabel("Iteration")
# plt.ylabel("Correlation")
# plt.ylim((0,1))
# plt.show()
#
# plt.clf()

### This plots
plt_len = max(len(manu_means),len(means))
plt.plot(manu_means, 'ro', markersize = 0.3)
plt.plot(means[:-1], 'ko', markersize = 0.5)
plt.plot((0,plt_len), (np.max(manu_means), np.max(manu_means)), 'r-')
plt.plot((0,plt_len), (np.max(means[:-1]), np.max(means[:-1])), 'k-')
plt.xlabel("Iteration")
plt.ylabel("Average Correlation")
plt.ylim((0.5,0.02+np.min([np.max([np.max(manu_means),np.max(means[:-1])])])))
plt.legend(['Manu Best Average','Bayes Best Average', 'Manu Iterations', 'Bayes Iterations'],loc=4)
plt.savefig('figures/perf_mean.png')
plt.clf()

plt_len = max(len(manu_mins),len(mins))
plt.plot(manu_mins, 'ro', markersize = 0.3)
plt.plot(mins[:-1], 'ko', markersize = 0.5)
plt.plot((0,plt_len), (np.max(manu_mins), np.max(manu_mins)), 'r-')
plt.plot((0,plt_len), (np.max(mins[:-1]), np.max(mins[:-1])), 'k-')
plt.xlabel("Iteration")
plt.ylabel("Average Correlation")
plt.ylim((-0.2,0.02+np.min([np.max([np.max(manu_mins),np.max(mins[:-1])])])))
plt.legend(['Manu Best Min','Bayes Best Min', 'Manu Iterations', 'Bayes Iterations'],loc=4)
plt.savefig('figures/perf_min.png')
plt.clf()

# swag_df[[2,3,4,5,6,7]].plot()
# plt.ylim((0,1))
# plt.savefig('vars.png')

# run_best_perf = sum(perf.values.tolist(), [])
# imps = [0] * len(run_best_perf)
# it = 0
# best_perf = run_best_perf[0]
# for p1 in run_best_perf:
#     if p1 < best_perf:
#         run_best_perf[it] = best_perf
#     else:
#         best_perf = p1
#         imps[it] = 1
#     it += 1
# plt.plot(run_best_perf)
# plt.plot(np.array(imps)*0.1+0.7)
# plt.xlabel("Iteration")
# plt.ylabel("Running Best Correlation")
# plt.show()
# plt.savefig('run_best.png')

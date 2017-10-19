from ops.db_utils import plot_db
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import pylab as plt

swag = plot_db()
swag_df = pd.DataFrame(np.array(swag))
perf = swag_df[[8]]
# plt.plot(perf)
# plt.xlabel("Iteration")
# plt.ylabel("Correlation")
# plt.show()
# plt.clf()
swag_df[[2,3,4,5,6,7]].plot()
plt.ylim((0,1))
plt.savefig('vars.png')


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
# import ipdb; ipdb.set_trace()
# plt.plot(run_best_perf)
# plt.plot(np.array(imps)*0.1+0.7)
# plt.xlabel("Iteration")
# plt.ylabel("Running Best Correlation")
# plt.show()
# plt.savefig('run_best.png')

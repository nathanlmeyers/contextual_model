from ops.db_utils import plot_db, add_row_to_db, open_db, close_db, gather_parameter_data
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
import scipy as sp
from ops.parameter_defaults import PaperDefaults
import GPyOpt
from timeit import default_timer as timer

# Get the data from the db
cors = pd.DataFrame(np.array(plot_db(table))).loc[21:,8:15].convert_objects(convert_numeric=True)
prams = pd.DataFrame(np.array(plot_db(table))).loc[21:,2:7].convert_objects(convert_numeric=True)
means = cors.mean(axis=1)[:-5]
means_it = int(np.argmax(means))
means_prams = prams.loc[means_it,:].tolist()
print "Best Mean Corr is at it " + str(means_it) + " and is corr = " + str(float(np.max(means)))
mins = cors.min(axis=1)[:-5]
mins_it = int(np.argmax(mins))
mins_prams = prams.loc[mins_it,:].tolist()
print "Best Min Corr is at it " + str(mins_it) + " and is corr = " + str(float(np.max(mins)))

epsilon = 0.001

# conn,cur = open_db()
# cur.execute("create table best_params (_id bigserial primary key, lesions varchar, alpha float, beta float, mu float, nu float, gamma float, delta float, f3a float, f3b float, f4 float, f5 float, f7 float, tbp float, tbtcso float, bw float, working boolean default False)")
# conn.commit()
# close_db(cur,conn)

opt_list = ['alpha', 'beta', 'mu', 'nu', 'gamma', 'delta']
means_grid = np.array([means_prams]*13)
mins_grid = np.array([mins_prams]*13)

for i in range(6):
    means_grid[i+1][i] = means_grid[i+1][i] + epsilon
    mins_grid[i+1][i] = mins_grid[i+1][i] + epsilon
    means_grid[i+5][i] = means_grid[i+5][i] - epsilon
    mins_grid[i+5][i] = mins_grid[i+5][i] - epsilon

id_var = len(np.array(gather_parameter_data('None',table_name='best_params')))

means_grid = means_grid.tolist()

for j in range(13):
    hp_set = dict(zip(opt_list,means_grid[j]))
    hp_set['_id'] = id_var
    add_row_to_db(hp_set,opt_list,'best_params')

    hp_set = dict(zip(opt_list,mins_grid[j]))
    hp_set['_id'] = id_var + 1
    add_row_to_db(hp_set,opt_list,'best_params')

    id_var = id_var + 2

import sys
import numpy as np
import tensorflow as tf
import model_utils
from timeit import default_timer as timer
import scipy as sp
sys.path.insert(0, '/media/storage_30/nathan/contextual_model/')
from ops.parameter_defaults import PaperDefaults
from ops.db_utils import add_row_to_db, gather_parameter_data, gather_perf_data
import GPyOpt

#Import default parameters
defaults = PaperDefaults()

#Import data from db and defaults to pass into optimization routine
hist = np.array(gather_parameter_data(defaults.lesions[0],table_name=defaults.table_name))
perf = np.array(gather_perf_data(defaults.lesions[0],table_name=defaults.table_name))
perf = np.array([[-x] for x in np.mean(perf,1)])
bds = defaults._DEFAULT_DOMAINS

#Generate the next sample
opt_me = GPyOpt.methods.BayesianOptimization(f = None, X = hist, Y = perf, domain = bds, evaluator_type = 'local_penalization')
next_samp = opt_me.suggested_sample[0].tolist()

#Update db and print status
opt_list = ['alpha', 'beta', 'mu', 'nu', 'gamma', 'delta']
hp_set = dict(zip(opt_list,next_samp))
hp_set['_id'] = len(hist)+1
add_row_to_db(hp_set,opt_list)
print 'Parameter combo #' + str(len(hist)+1) + ' inserted into db'

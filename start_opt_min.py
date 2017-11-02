import sys
import numpy as np
import scipy as sp
from ops.parameter_defaults import PaperDefaults
from ops.db_utils import add_row_to_db, gather_parameter_data, gather_perf_data
import GPyOpt
from timeit import default_timer as timer

opt_samp = int(sys.argv[2])
opt_type = sys.argv[3]
opt_max = sys.argv[4]

#Import default parameters
defaults = PaperDefaults()

def gpy_wrapper(X,Y,domain,samps):
    opt_me = GPyOpt.methods.BayesianOptimization(f = None, X = X, Y = Y, domain = domain, evaluator_type = 'local_penalization', batch_size = samps, num_cores = samps)
    next_samp = opt_me.suggested_sample
    return next_samp

# Collect history from DB
hist = np.array(gather_parameter_data(defaults.lesions[0],table_name=defaults.table_name))
perf = np.array(gather_perf_data(defaults.lesions[0],table_name=defaults.table_name))

if opt_max == 'min':
    perf = np.array([[x] for x in np.min(perf,1)])
else:
    perf = np.array([[-x] for x in np.min(perf,1)])

flat_perf = [item for sublist in perf for item in sublist]
if flat_perf[-1] <= np.min(flat_perf):
    print 'NEW BEST FOUND\nALERT\nNEW BEST FOUND'

#Generate the next sample
start = timer()
if opt_type == 'gpyopt':
    next_samp = gpy_wrapper(hist,perf,defaults._DEFAULT_DOMAINS,opt_samp)
else:
    print 'Not implemented yet'

#Update db and print status
opt_list = ['alpha', 'beta', 'mu', 'nu', 'gamma', 'delta']
samp_lists = [];
id_var = len(hist);
for i in range(opt_samp):
    hp_set = dict(zip(opt_list,next_samp[i].tolist()))
    id_var += 1
    hp_set['_id'] = id_var
    add_row_to_db(hp_set,opt_list)
end = timer()

print '\n\nParameter combo #' + str(len(hist)+1) + ' inserted into db. This took ' + str(np.around(end-start, 2)) +' seconds.\n\n'

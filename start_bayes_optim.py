from ops.db_utils import init_db, generate_combos, create_and_execute_daemons, prepare_settings
from ops.parameter_defaults import PaperDefaults
import sys

defaults = PaperDefaults()
print 'Initializing database'
init_db(sys.argv[2])
print 'Generating initial ' + sys.argv[1] + ' hyperparameter combos'
generate_combos(int(sys.argv[1]))

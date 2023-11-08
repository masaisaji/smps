from smps.read import StochasticModel
from time import time

sm = StochasticModel('./data/siplib/dcap342_300/dcap342_300')
# sm.plot_scenario_tree()  # useelss
model = sm.generate_deterministic_equivalent()
model.printStats()
t0 = time()
# model.optimize()
tf = time()
print('Time: ', tf-t0)

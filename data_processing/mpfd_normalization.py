'''
Normalizes mpfd data into count rates.
'''

import numpy as np

data = np.loadtxt('data')
nodeData = data[:,0]
relError = data[:,1]


# input normalization values
reactorPower = 250000 #W

# calculate normalization coefficient
normalization = (2.54 * reactorPower) / (200 * 1.60218e-13)

# normalize data
reactionRates = nodeData * normalization * 60 # counts per minute

# calculate error
absError = reactionRates * relError

# output results

for node, rate in enumerate(reactionRates):
    print('The reaction rate of node {} is {:6.2f} cpm +/-{:6.2f} cpm at {} kW'.format(node, rate, absError[node], reactorPower / 1000))

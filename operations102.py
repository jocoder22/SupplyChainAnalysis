from pulp import *
sp = '\n\n'

iron = ['A', 'B', 'C', 'D']
cost = [26, 30, 20, 8]
lbs = [1000, 1000, 1000, 1]
mag = [4.5, 5, 4, 1]
sil = [40, 10, 6, 0]

x = LpVariable.dicts('var_', iron, lowBound=0, cat='Continous')

price = dict(zip(iron, cost))
lbsdict = dict(zip(iron, lbs))
magdict = dict(zip(iron, mag))
sildict = dict(zip(iron, sil))

model = LpProblem('Max Profit', LpMinimize)
model += lpSum([price[i] * x[i] for i in iron])
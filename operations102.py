from pulp import *
sp = '\n\n'

iron = ['A', 'B', 'C', 'D']
cost = [26, 30, 20, 8.0]
lbs = [1000, 1000, 1000, 1.0]
mag = [4.5, 5.0, 4.0, 1.0]
sil = [40, 10, 6.0, 0]

x = LpVariable.dicts('var_', iron, lowBound=0, cat='Continous')

price = dict(zip(iron, cost))
lbsdict = dict(zip(iron, lbs))
magdict = dict(zip(iron, mag))
sildict = dict(zip(iron, sil))

model = LpProblem('Max Profit', LpMinimize)
model += lpSum([price[i] * x[i] for i in iron])

model += lpSum([lbsdict[i] * x[i] for i in iron]) == 1000
model += lpSum([magdict[i] * x[i] for i in iron]) >= 4.5
model += lpSum([sildict[i] * x[i] for i in iron]) >= 32.5
model += lpSum([sildict[i] * x[i] for i in iron]) <= 55.0

model.solve()
print(f'Status: {LpStatus[model.status]}')
for v in model.variables():
    print(f'{v.name} = {v.varValue}')

print(f'Objective = {value(model.objective)}')

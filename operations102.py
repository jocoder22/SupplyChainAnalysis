import pulp as plp
import pandas as pd 
sp = '\n\n'

iron = ['A', 'B', 'C', 'D']
cost = [26, 30, 20, 8.0]
lbs = [1000, 1000, 1000, 1.0]
mag = [4.5, 5.0, 4.0, 1.0]
sil = [40, 10, 6.0, 0]

x = plp.LpVariable.dicts('var_', iron, lowBound=0, cat='Continous')

price = dict(zip(iron, cost))
lbsdict = dict(zip(iron, lbs))
magdict = dict(zip(iron, mag))
sildict = dict(zip(iron, sil))

model = plp.LpProblem('Max Profit', plp.LpMinimize)
model += plp.lpSum([price[i] * x[i] for i in iron])


model += plp.lpSum([lbsdict[i] * x[i] for i in iron]) == 1000
model += plp.lpSum([magdict[i] * x[i] for i in iron]) >= 4.5
model += plp.lpSum([sildict[i] * x[i] for i in iron]) >= 32.5
model += plp.lpSum([sildict[i] * x[i] for i in iron]) <= 55.0

model.solve()
print(f'Status: {plp.LpStatus[model.status]}')
for v in model.variables():
    print(f'{v.name} = {v.varValue}')

print(f'Objective = {plp.value(model.objective)}')


# shadow price and slack
# if slack = 0, then the constraint is binding
# if slack > 0, then non-binding constraint
# changing binding constraint will change the result of the objective function and solution

o = [{'name': name, 'Shadow Price': c.pi, 'Slack': c.slack}
        for name, c in model.constraints.items()]

print(pd.DataFrame(o))



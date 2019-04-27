import pandas as pd 
from random import normalvariate as nmv
from pulp import *

sp = '\n\n'

house = ['A', 'B', 'C']
cost = [520, 490, 590]
space = [6, 8, 10]
mangt = [11, 18, 10]
gott = [1, 0, 0]

# Define decision variables
y = LpVariable.dicts('house_', house, lowBound=0, cat='Continous')
costdict = dict(zip(house, cost))
spacedict = dict(zip(house, space))
magdict = dict(zip(house, mangt))
gotdict = dict(zip(house, gott))

# Initialize the model
model1 = LpProblem('Max Profit', LpMaximize)

# Define the objective function
model1 += lpSum([costdict[i] * y[i] for i in house])

# Define the constraints
model1 += lpSum([spacedict[i] * y[i] for i in house]) <= 80
model1 += lpSum([magdict[i] * y[i] for i in house]) <= 120
model1 += lpSum([gotdict[i] * y[i] for i in house]) <= 16

# Solve the model
model1.solve()
print(f'Status: {LpStatus[model1.status]}')
for v in model1.variables():
    print(f'{v.name} = {v.varValue}')
print('Objective: ', value(model1.objective))

o = [{'name': name, 'Shadow Price': c.pi, 'Slack':c.slack} 
        for name, c in model1.constraints.items()]

print(pd.DataFrame(o))


# sensitivity analysis
def sensally():
    # Initialize the model
    model1 = LpProblem('Max Profit', LpMaximize)

    # Define the objective function and add random variable
    model += lpSum([(costdict[i] + nmv(0, 25)) * y[i] for i in house])

    # Define the constraints
    model += lpSum([spacedict[i] * y[i] for i in house]) <= 50
    model += lpSum([magdict[i] * y[i] for i in house]) <= 120
    model += lpSum([gotdict[i] * y[i] for i in house]) <= 16

    # Solve the model
    model.solve()

    oo = {f'{i}':y[i].varValue for i in house}
    oo['Objective'] = value(model.objective)

    return oo

output = []

for t in range(100):
    output.append(sensally())


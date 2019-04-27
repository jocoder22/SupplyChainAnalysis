import pandas as pd 
import matplotlib.pyplot as plt
from random import normalvariate as nmv
import pulp as plp
plt.style.use('ggplot')

sp = '\n\n'

house = ['A', 'B', 'C']
cost = [500, 450, 600]
space = [6, 5, 8]
mangt = [10.5, 20, 10]
gott = [1, 0, 0]

# Define decision variables
y = plp.LpVariable.dicts('house_', house, lowBound=0, cat='Continous')
costdict = dict(zip(house, cost))
spacedict = dict(zip(house, space))
magdict = dict(zip(house, mangt))
gotdict = dict(zip(house, gott))

# Initialize the model
model1 = plp.LpProblem('Max Profit', plp.LpMaximize)

# Define the objective function
model1 += plp.lpSum([costdict[i] * y[i] for i in house])

# Define the constraints
model1 += plp.lpSum([spacedict[i] * y[i] for i in house]) <= 50
model1 += plp.lpSum([magdict[i] * y[i] for i in house]) <= 120
model1 += plp.lpSum([gotdict[i] * y[i] for i in house]) <= 16

# Solve the model
model1.solve()
print(f'Status: {plp.LpStatus[model1.status]}')
for v in model1.variables():
    print(f'{v.name} = {v.varValue}')
print('Objective: ', plp.value(model1.objective))

o = [{'name': name, 'Shadow Price': c.pi, 'Slack':c.slack} 
        for name, c in model1.constraints.items()]

print(pd.DataFrame(o))


# sensitivity analysis
def sensally():
    # Initialize the model
    model = plp.LpProblem('Max Profit', plp.LpMaximize)

    # Define the objective function and add random variable
    model += plp.lpSum([(costdict[i] + nmv(0, 25)) * y[i] for i in house])

    # Define the constraints
    model += plp.lpSum([spacedict[i] * y[i] for i in house]) <= 50
    model += plp.lpSum([magdict[i] * y[i] for i in house]) <= 120
    model += plp.lpSum([gotdict[i] * y[i] for i in house]) <= 16

    # Solve the model
    model.solve()

    oo = {f'{i}':y[i].varValue for i in house}
    oo['Objective'] = plp.value(model.objective)

    return oo

output = []

for t in range(100):
    output.append(sensally())

df = pd.DataFrame(output)
print(df.head())
for item in house:
    print(" ", end=sp)
    print(df[item].value_counts(), sep=sp)


fig, axes = plt.subplots(1,3, sharex=True, sharey=True)

for item, (idx, ax) in zip(house, enumerate(axes.flatten())):
    ax.hist(df[item],  color=plt.cm.Paired(idx/6.))

plt.show()
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


# sensitivity analysis II
def sensally2():
    # Initialize the model
    model = plp.LpProblem('Max Profit', plp.LpMaximize)

    rdm = nmv(0.5, 0.5)
    # Define the objective function and add random variable
    model += plp.lpSum([costdict[i]  * y[i] for i in house])

    # Define the constraints
    model += plp.lpSum([(spacedict[i] + rdm) * y[i] for i in house]) <= 50
    model += plp.lpSum([(magdict[i] + rdm) * y[i] for i in house]) <= 120
    model += plp.lpSum([(gotdict[i] + rdm) * y[i] for i in house]) <= 16

    # Solve the model
    model.solve()

    oo = {f'{i}':y[i].varValue for i in house}
    oo['Objective'] = plp.value(model.objective)

    return oo

output = []

for t in range(100):
    output.append(sensally2())

df = pd.DataFrame(output)
print(df.head())

# for item in house:
#     print(" ", end=sp)
#     print(df[item].value_counts(), sep=sp)


# Plot the results
fig, axes = plt.subplots(1,4, sharey=True)

for item, (idx, ax) in zip(df.columns, enumerate(axes.flatten())):
    ax.hist(df[item],  color=plt.cm.Paired(idx/6.))
    ax.set_xlabel(item)
    if idx == 0:
        ax.set_ylabel('Number of Simulations')
    

plt.show()
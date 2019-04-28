import pandas as pd 
# from pulp import LpProblem, LpMaximize, LpVariable, LpStatus
import pulp as ch

sp = '\n\n'


model = ch.LpProblem('Maximium Profit', ch.LpMaximize)
A = ch.LpVariable("A", lowBound=0, cat="Integer")
B = ch.LpVariable("B", lowBound=0, cat="Integer")

model += 10*A + 20*B

model += 2.5*A + 2*B <= 280
model += 0.5*A + 1*B <= 110
model += 2*B <= 80

model.solve()
print(f'Status: {ch.LpStatus[model.status]}')
for v in model.variables():
    print(f'{v.name} = {v.varValue}')
print(f'Objective = {ch.value(model.objective)}', end=sp)


# Using LpVariable.dicts()
bread = ['A', 'B']
cost = dict(zip(bread, [10, 20]))
space = [0.5, 1]
demand = [1, 2.5]
discount = [1, 2]

var_dict = ch.LpVariable.dicts('Bread_', bread, lowBound=0, cat='Integer')

model2 = ch.LpProblem('Maximium Profit', ch.LpMaximize)
model2 += ch.lpSum(cost[i] * var_dict[i] for i in bread)

for i in space:
    model2 += ch.lpSum([i * var_dict[d] for d in bread]) <= 30
for i in demand:
    model2 += ch.lpSum([i * var_dict[d] for d in bread]) <= 60
for i in discount:
    model2 += ch.lpSum([i * var_dict[d] for d in bread]) <= 22

model2.solve()
print(f'Status: {ch.LpStatus[model2.status]}')
for v in model2.variables():
    print(f'{v.name} = {v.varValue}')

print(f'Objective = {ch.value(model2.objective)}', end=sp)





# Profit maximization problem
maxprofit = ch.LpProblem('Maximize Profit', ch.LpMaximize)
AA = ch.LpVariable("AA", lowBound=0, cat="Integer")
AB = ch.LpVariable("AB", lowBound=0, cat="Integer")
AC = ch.LpVariable("AC", lowBound=0, cat="Integer")

Beers = ["AA", "AB", "AC"]
Cost = [6, 8, 11]
costdict = dict(zip(Beers, Cost))
Beersdict = {"AA": AA, "AB": AB, "AC": AC}

maxprofit += ch.lpSum([Beersdict[i] + costdict[i] for i in Beers])

maxprofit += 1*AA + 2*AB + 1*AC <= 180
maxprofit += 0.5*AA + 1*AC <= 100
maxprofit += 1*AB  + 1*AC >= 50

maxprofit.solve()
print(f'Maxprofit Status: {ch.LpStatus[maxprofit.status]}')
for v in maxprofit.variables():
    print(f'{v.name} = {v.varValue}')





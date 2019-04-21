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



# Profit maximization problem
maxprofit = ch.LpProblem('Maximize Profit', ch.LpMaximize)
AA = ch.LpVariable("AA", lowBound=0, cat="Integer")
AB = ch.LpVariable("AB", lowBound=0, cat="Integer")


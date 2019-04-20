import pandas as pd 
from pulp import *

sp = '\n\n'


model = LpProblem('Maximium Profit', LpMaximize)
A = LpVariable("A", lowBound=0, cat="Integer")
B = LpVariable("B", lowBound=0, cat="Integer")

model += 30*A + 50*B

model += 4.5*A + 2*B <= 280
model += 0.5*A + 1*B <= 110
model += 2*B <= 80

model.solve()


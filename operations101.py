import pandas as pd 
import pulp as pul 

# Warehouse distribution problem

warehouse = ['NJ', 'NY', 'MD']
stores = ['pop', 'gog', 'lol', 'kol', 'mon']
demands = [3000, 1200, 7000, 4100, 5600]
cost = [300, 800, 100, 230, 90, 600, 240, 510, 892, 456, 125, 100, 840, 220, 234]

demansdict = dict(zip(stores, demands))
costdict = dict(zip([(x, y) for x in warehouse for y in stores], cost))

keys = [(w, s) for w in warehouse for s in stores]
vardict = pul.LpVariable.dicts('Storelist', keys, lowBound=0, cat='Integer')

# Define objective function
model = pul.lpSum([costdict[(w, s)] * vardict[(w, s)] 
                for s in stores for w in warehouse])

for s in stores:
    model += pul.lpSum([vardict[(w, s)] for w in warehouse]) == demands[s]

model.solve()
print('Status', pul.LpStatus[model.status])
for v in model.variables():
    print(f'{v.name} = {v.varValue}')
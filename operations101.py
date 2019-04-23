import pandas as pd 
import pulp as pul 

# Warehouse distribution problem

warehouse = ['NJ', 'NY', 'MD', 'IL']
stores = ['pop', 'gog', 'lol', 'kol', 'mon']
demands = [3000, 1200, 7000, 4100, 5600]
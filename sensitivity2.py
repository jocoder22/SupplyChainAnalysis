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
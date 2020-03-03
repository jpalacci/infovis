# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import csv

plt.rcdefaults()
fig, ax = plt.subplots()

with open('Week9MM.csv') as f:
    data = list(csv.DictReader(f, delimiter=','))

# Example data
grades = [x['Grade'] for x in data]
y_pos = np.arange(len(grades))
sleep_averaged = np.array([float(x['Hours Averaged']) for x in data])
sleep_needed = np.array([float(x['Hours Needed']) for x in data])

ax.barh(y_pos, sleep_averaged, edgecolor='black', align='center')
ax.barh(y_pos, sleep_needed, left=sleep_averaged, color='red', edgecolor='black',  align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(grades)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Hours')
ax.set_title('How much kids sleep?')

plt.show()

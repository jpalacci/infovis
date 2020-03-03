# libraries
import csv

import matplotlib.pyplot as plt
import numpy as np

with open('Week9MM.csv') as f:
    data = list(csv.DictReader(f, delimiter=','))

grades = [x['Grade'] for x in data]
y_pos = np.arange(len(grades))
sleep_averaged = np.array([float(x['Hours Averaged']) for x in data])
sleep_needed = np.array([float(x['Hours Needed']) for x in data])

plt.hlines(y=grades, xmin=sleep_averaged, xmax=sleep_needed, color='red',
           alpha=0.4)
plt.scatter(sleep_averaged, grades, color='skyblue', alpha=1, label='value1')
plt.scatter(sleep_needed, grades, color='green', alpha=0.4, label='value2')
ax.patch.set_facecolor('#ababab')

# Add title and axis names
plt.xlabel('Hours of sleep')
plt.show()

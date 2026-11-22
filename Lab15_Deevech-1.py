"""
Program Name: Plot a Math Formula (Sine Wave)
Author: Boston Deevech
Purpose: Use matplotlib and the math library to calculate points on the
         sine wave y = sin(x), plot them with a title and axis labels,
         and save the finished plot to an image file (sine_wave.png).
Starter Code: No starter code was used. The approach follows the
              circle example in the Lab 15 assignment description
              (looping through degrees and converting with math.radians()).
Date: 11/22/2026
"""

import math

import matplotlib.pyplot as plt

# Build the x and y lists using the formula y = sin(x).
# Loop from 0 to 1800 degrees, which is 5 full periods of the wave.
x_values = []
y_values = []
for degree in range(0, 1801):
    radians = math.radians(degree)
    x_values.append(radians)
    y_values.append(math.sin(radians))

# Plot the data with a title and axis labels.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=2)
ax.set_title("Sine Wave: y = sin(x)", fontsize=18)
ax.set_xlabel("x (radians)", fontsize=12)
ax.set_ylabel("sin(x)", fontsize=12)

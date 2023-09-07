import numpy as np
import matplotlib.pyplot as plt

# generate data using numpy
# create 500 data between 0 and 1 then multiply by 100
x_data = np.random.random(500) * 100
y_data = np.random.random(500) * 100

# print x_data on terminal
print(x_data)

# create a scatter plot
# c is for color, marker is for shape of the scatter, alpha is for transparency
plt.scatter(x_data, y_data, c="#00f", marker="*", alpha=0.3, s=150)

# show the graph
plt.show()


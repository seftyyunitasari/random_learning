import matplotlib.pyplot as plt

# generate data using a python function
years = [2006 + x for x in range(16)]
weights = [44, 45, 46, 48, 47, 45, 44, 43, 42, 45, 46, 47, 48, 46, 45, 44]

# create a line plot
# plt.plot(years, weights, "r--", lw=3)
plt.plot(years, weights, c="r", lw=3, linestyle="--")
plt.show()

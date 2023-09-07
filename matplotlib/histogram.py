import numpy as np
import matplotlib.pyplot as plt

# generate data using a normal distribution
# 1000 data with a mean of 20 years old and standard deviation of 1.5 years
ages = np.random.normal(20, 1.5, 1000)

# plot a histogram
# we can specify the number of bin ex: bins=10
# we can also plot cumulative plot ex cumulative=True
plt.hist(ages,
         bins=[ages.min(), 18, 21, ages.max()])
plt.show()



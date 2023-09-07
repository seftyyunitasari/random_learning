import numpy as np
import matplotlib.pyplot as plt

stock_a = [98, 102, 100, 99, 98, 100, 103]
stock_b = [100, 99, 101, 102, 104, 102, 102]
stock_c = [99, 101, 103, 100, 104, 103, 105]

plt.plot(stock_a, label="Company1")
plt.plot(stock_b, label="Company2")
plt.plot(stock_c, label="Company3")
plt.legend(loc="lower right")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

years = [2015 + x for x in range(8)]
income = [70,  73, 75, 74, 77, 79, 82, 85]

income_ticks = list(range(68, 87, 2))

plt.plot(years, income)
plt.title("Income of John in USD", fontsize=20, fontname="Times New Roman")
plt.xlabel("Years")
plt.ylabel("Income")
plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])
plt.show()

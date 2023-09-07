import matplotlib.pyplot as plt

x = ["Java", "C#", "Go", "Phyton", "C++", "JavaScript"]
y = [40, 35, 15, 70, 60, 50]

# generate a bar plot
plt.bar(x, y, color="g", width=0.5, align="edge", edgecolor="r", lw=3)
plt.show()

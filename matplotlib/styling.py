import matplotlib.pyplot as plt
from matplotlib import style

# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
style.use("ggplot")

votes = [10, 17, 19, 39, 21]
people = ["A", "B", "C", "D","E"]

plt.pie(votes, labels=None)
plt.legend(labels=people)
plt.show()

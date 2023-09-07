import matplotlib.pyplot as plt

langs = ["Python", "C++", "Java", "C#", "Go"]
votes = [51, 19, 19, 28, 7]
explodes = [0.3, 0, 0, 0, 0]

plt.pie(votes, labels=langs, explode=explodes,
        autopct="%.2f%%", pctdistance=1.5, startangle=90)
plt.show()

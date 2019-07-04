import seaborn as sns
from matplotlib import pyplot as plt
sns.set(style="whitegrid")
iris = sns.load_dataset("iris")
ax = sns.violinplot(x="species", y="sepal_length", data=iris)
plt.show()
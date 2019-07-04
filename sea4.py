import seaborn as sns
from matplotlib import pyplot as plt
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
ax = sns.violinplot(x="sex", y="total_bill", data=tips)
plt.show()
import seaborn as sns
from matplotlib import pyplot as plt
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
ax = sns.swarmplot(x=tips["total_bill"],y=tips["size"],data=tips)
plt.show()
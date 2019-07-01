import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('titanic')
print(df.head())
sb.jointplot(x='age', y='fare', data=df)
plt.show()
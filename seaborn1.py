import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('titanic')
print(df.head())
sb.barplot(x='sex',y='survived',data=df)
plt.show()
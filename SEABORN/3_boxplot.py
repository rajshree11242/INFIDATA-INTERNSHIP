import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')


sns.boxplot(x='species',y='sepal_width',data=df,palette='set2')#creating a boxplot
plt.show()
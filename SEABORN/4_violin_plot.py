import seaborn as sns
import matplotlib.pyplot as plt

#violin plot
#loading dataset

df = sns.load_dataset('iris')
#creating


sns.violinplot(x='species',y='sepal_width',data=df)
plt.show()
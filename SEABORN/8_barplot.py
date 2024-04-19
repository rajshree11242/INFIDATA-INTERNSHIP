import seaborn as sns
import matplotlib.pyplot as plt
#loading dataset
df = sns.load_dataset('iris')
#creating

sns.barplot(x='species',y='sepal_width',color='red',data=df)
plt.show()
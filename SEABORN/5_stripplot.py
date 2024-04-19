import seaborn as sns
import matplotlib.pyplot as plt
#loading dataset

df = sns.load_dataset('iris')
#creating
sns.stripplot(x='species',y='sepal_width',color='blue',data=df)
plt.show()
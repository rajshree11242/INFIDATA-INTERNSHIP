import seaborn as sns
import matplotlib.pyplot as plt


#loading dataset

df = sns.load_dataset('iris')
#creating
sns.histplot(x='species',y='sepal_width',data=data)
#displaying
plt.show()
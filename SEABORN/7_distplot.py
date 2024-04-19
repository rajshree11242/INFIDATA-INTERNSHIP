#displot is used basically plot distribution of continous data
#distribution lot
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df = sns.load_dataset('iris')
#creating

sns.displot(df['sepal_width'],color='b')
plt.show()
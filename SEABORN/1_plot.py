import seaborn as sns#advanced visualisation
import matplotlib.pyplot as plt #basic visualisation

#loading dataset
df = sns.load_dataset("iris")#loading the dataset
print(df)#displaying the dataset

#draw lineplot

sns.lineplot(x="sepal_length",y="sepal_width",data=df)
#selling the title using matplotlib
plt.title('Lineplot on IRIS dataset')
plt.show()#displaying the plot
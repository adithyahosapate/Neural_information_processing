import pandas
import matplotlib.pyplot as plt

df =pandas.read_csv('result1.csv')
df.head()


plt.scatter(range(1024),df.prob[1022:2046])
plt.show()


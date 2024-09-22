import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv(r"C:\\Users\\mevas\\Desktop\\Projects\\Python\\Day91-91 Drug Classification\\pyspark\\day9192DrugClass.csv")
data

data.head(5)
df = pd.DataFrame(data)

drug = df['Drug']
age = df['Age']

fig = plt.figure(figsize =(10, 7))

plt.bar(drug[0:10], age[0:10])

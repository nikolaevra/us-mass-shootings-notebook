import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mass Shootings Dataset.csv')

import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

m_illness = dataset.iloc[:, 7].values

# categorize data to make comparisons faster
le = LabelEncoder()
m_illness = le.fit_transform(m_illness)

# 4 categories that are present in the dataset
# Yes
cat_yes = 0
# No
cat_no = 0
# Unknown
cat_unknown = 0
# Unclear
cat_unclear = 0

for item in m_illness:
    if item == 0:
        cat_no += 1
    elif item == 2:
        cat_unknown += 1
    elif item == 3:
        cat_yes += 1
    elif item == 1:
        cat_unclear += 1

# create labels and colors
labels = 'Yes', 'No', 'Unknown', 'Unclear'
x = [cat_yes, cat_no, cat_unknown, cat_unclear]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'red']

# plot the results
# plt.pie(x, labels=labels, colors=colors)
# plt.show()

dead = dataset.iloc[:, 4].values
injured = dataset.iloc[:, 5].values

import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
area = np.pi * (15 * np.random.rand(N))**2

plt.scatter(dead[1:], injured[1:], s=area, c='blue', alpha=0.2)
plt.show()



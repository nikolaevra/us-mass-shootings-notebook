import pandas as pd

# Importing the dataset
dataset = pd.read_csv('datasets/Mass Shootings Dataset.csv')

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
area = np.pi * (15 * np.random.rand(N)) ** 2

# plt.scatter(dead[1:], injured[1:], s=area, c='blue', alpha=0.2)
# plt.show()

dates = dataset.iloc[:, 3].values

# plt.figure(figsize=(20, 5))
# plt.plot_date(x=dates, y=dead, fmt="r-")
plt.title("US Mass Shooting Deaths Timeline")
plt.ylabel("Deaths")
plt.xlabel("Dates")

# plt.grid(True)
# plt.show()

# categorize data to make comparisons faster
race = dataset.iloc[:, 8].values

# create a dictionary to count for each category
race_dict = dict()

for item in race:
    if item not in race_dict:
        race_dict[item] = 1
    else:
        race_dict[item] += 1

races = list(race_dict.keys())
num_races = list(race_dict.values())
elem_count = np.arange(len(races))

# plt.barh(y_pos, num_races, align='center', alpha=0.5)
# plt.yticks(y_pos, races)
# plt.ylabel("Races")
# plt.xlabel("# of shootings involved in")
# plt.title('# of shootings involvement by race')
# plt.show()

# create a dictionary to count for each category
fatal_dict = dict()

for item in dead:
    if item not in fatal_dict:
        fatal_dict[item] = 1
    else:
        fatal_dict[item] += 1

deaths = list(race_dict.keys())
num_deaths = list(race_dict.values())
elem_count = np.arange(len(deaths))



#plt.yticks(elem_count, deaths)
#plt.ylabel("Races")
#plt.xlabel("# of shootings involved in")
#plt.title('# of shootings involvement by race')

#plt.show()

from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)

wordcloud = WordCloud(
    background_color='white',
    stopwords=stopwords,
    max_words=200,
    max_font_size=40,
    random_state=42
).generate(str(dataset['Summary']))

plt.figure(figsize=(12,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

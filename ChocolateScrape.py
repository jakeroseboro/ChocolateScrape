import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')

soup = BeautifulSoup(webpage.content, 'html.parser')

ratings = soup.find_all(attrs = {'class' : 'Rating'})

rating = []

for i in ratings[1:]:
  rating.append(float(i.get_text()))

plt.show(plt.hist(rating))

companyNames = soup.select('.Company')

companyName = []

for i in companyNames[1:]:
  companyName.append(i.get_text())

cocoa_percent_tags = soup.select(".CocoaPercent")

cocoa_percents = []

for i in cocoa_percent_tags[1:]:
  percent = float(i.get_text().strip('%'))
  cocoa_percents.append(int(percent))

d = {'Company' : companyName, 'Ratings' : rating, 'CocoaPercent' : cocoa_percents}

data = pd.DataFrame.from_dict(d)

average = data.groupby('Company').Ratings.mean()

topTen  = average.nlargest(10)

print(topTen)

plt.scatter(data.CocoaPercent, data.Ratings)

z = np.polyfit(data.CocoaPercent, data.Ratings, 1)

line_function = np.poly1d(z)

plt.plot(data.CocoaPercent, line_function(data.CocoaPercent), "r--")

plt.show()
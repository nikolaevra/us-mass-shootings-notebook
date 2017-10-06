# Get this figure: fig = py.get_figure("https://plot.ly/~nikolaevra/2/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~nikolaevra/2/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Plot 2", fileopt="extend")

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mass Shootings Dataset.csv')
dead = dataset.iloc[:, 4].values
lat = dataset.iloc[:, 10].values
lon = dataset.iloc[:, 11].values

import plotly.plotly as py
from plotly.graph_objs import *

for col in dataset.columns:
    dataset[col] = dataset[col].astype(str)

title = dataset['Title'] + '<br>' + \
                  'Date: ' + dataset['Date'] + ' Fatalities: ' + \
                  dataset['Fatalities'] + '<br>'

py.sign_in('nikolaevra', '#####')
trace1 = {
    "lat": lat,
    "lon": lon,
    "marker": {
        "cauto": True,
        "cmax": 58,
        "cmin": 0,
        "color": dead,
        "colorscale": [
            [0, "rgb(220,220,220)"], [0.2, "rgb(245,195,157)"],
            [0.4, "rgb(245,160,105)"], [1, "rgb(178,10,28)"]],
        "size": dead,
        "sizemode": "area",
        "sizeref": 0.01125,
        "sizesrc": "nikolaevra:5:f192d9",
    },
    "name": "Longitude",
    "text": title,
    "textsrc": "nikolaevra:0:8ca055",
    "type": "scattermapbox",
    "uid": "ccba03"
}
data = Data([trace1])
layout = {
    "geo": {
        "lakecolor": "rgb(255, 255, 255)",
        "projection": {"type": "mercator"},
        "scope": "usa",
        "showlakes": True
    },
    "mapbox": {
        "bearing": 0,
        "center": {
            "lat": 36.1844184699,
            "lon": -96.7380895968
        },
        "pitch": 0,
        "zoom": 2.89886008608
    },
    "title": "US Mass Shootings Geographical Heatmap<br>(Hover for "
             "breakdown)"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

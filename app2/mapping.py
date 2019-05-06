import pandas as pd
import json
# mapping library
import folium

data = pd.read_csv("volcanoes_usa.txt")

# access the data columns
lat = list(data["LAT"])
long = list(data["LON"])
elevation = list(data["ELEV"])
name = list(data["NAME"])

"""
    Creating a new map with its centre at the location list
    its tile layers as Stamen and its zoom control
"""
map = folium.Map(
    location=[35.0902, -95.7129],
    tiles='Stamen Toner',
    zoom_start=3,
)

"""
        the function accepts elevation parameter
        and will categorized it and return a color
"""


def categorized_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1001 <= elevation < 2000:
        return 'orange'
    elif 2001 <= elevation < 3000:
        return 'pink'
    else:
        return 'red'


# Creating a new feature group
fg_Markers = folium.FeatureGroup(name="Volcanoes")

"""
        Creating new markers
        We use zip function to match the objects together to a list
    """
# for lt, ln, nm, el, in zip(lat, long, name, elevation):
#     fg_Markers.add_child(
#         folium.Marker(
#             location=[lt, ln],
#             popup="<b>Name: </b>" + nm + '\n' +
#             "<b>Height: </b>" + str(el) + 'm',
#             icon=folium.Icon(color=categorized_color(el))
#         )
#     )

# create new circle Markers
fg_CircleMarkers = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el, in zip(lat, long, name, elevation):
    fg_CircleMarkers.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=5,
            fill=True,
            fill_color=categorized_color(el),
            popup="<b>Name: </b>" + nm + '\n' +
            "<b>Height: </b>" + str(el) + 'm', color=categorized_color(el))
    )

"""
    Categorized country layer color depending on the population
    Using lambda function and if else statement
    """
fg_Poly = folium.FeatureGroup(name = "World Population")
fg_Poly.add_child(
    folium.GeoJson(
        data=open("world.json", 'r',
                  encoding='utf-8-sig').read(),
        style_function=lambda z:
        {'fillColor': 'yellow'
         if z['properties']['POP2005'] < 10000000
         else 'orange' if 10000000 <= z['properties']['POP2005'] < 20000000
         else 'red'}))


map.add_child(fg_Markers)
map.add_child(fg_CircleMarkers)
map.add_child(fg_Poly)

# layer control
# this is added after adding feature groups to the map
map.add_child(folium.LayerControl())

map.save('map.html')

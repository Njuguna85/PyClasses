import pandas as pd

# mapping library
import folium

data = pd.read_csv("volcanoes_usa.txt")

# access the data columns
lat = list(data["LAT"])
long = list(data["LON"])
elevation = list(data["ELEV"])
name = list(data["NAME"])

map = folium.Map(
    location=[35.0902, -95.7129],
    tiles='Stamen Toner',
    zoom_control=3,
)


def categorized_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1001 <= elevation < 2000:
        return 'orange'
    elif 2001 <= elevation < 3000:
        return 'pink'
    else:
        return 'red'


feature_Group = folium.FeatureGroup(name="My Map")

for lt, ln, nm, el, in zip(lat, long, name, elevation):
    feature_Group.add_child(
        folium.Marker(
            location=[lt, ln],
            popup="<b>Name: </b>" + nm + '\n' +
            "<b>Height: </b>" + str(el) + 'm',
            icon=folium.Icon(color=categorized_color(el))
        )
    )

map.add_child(feature_Group)

map.save('map.html')

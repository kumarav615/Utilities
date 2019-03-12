# python library to show maps depending on coordinates
import folium as fo
import pandas as pd

# Load the data from a file
data = pd.read_csv('volcanoes_usa.txt')

# get latitude longitude elevation from data
latitude = data['LAT']
longitude = data['LON']
elevation = data['ELEV']


def elevate_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# call Map method of folium libaray and hold in a variable
out_map = fo.Map(location=[37.296933, -121.9574983], zoom_start=5, tiles="Mapbox bright")

# Add Marker, then add to out_map
for latitude, longitude, elevation in zip(latitude, longitude, elevation):
    fo.Marker(location=[latitude, longitude], popup=str(elevation) + "m", icon=fo.Icon(color=elevate_color(elevation))).add_to(out_map)

# save the map to the current working directory
out_map.save("elevationbycolor.html")




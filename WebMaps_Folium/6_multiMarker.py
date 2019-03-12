# python library to show maps depending on coordinates
import folium as fo

# call Map method of folium libaray and hold in a variable
out_map = fo.Map(location=[37.296933, -121.9574983], zoom_start=8, tiles="Mapbox bright")

# Add Marker, then add to out_map
for coordinate in [[37.4074687,-122.086669],[37.8199286,-122.4804438]]:
    fo.Marker(location=coordinate, icon=fo.Icon(color='green')).add_to(out_map)

# save the map to the current working directory
out_map.save("multiMarker.html")




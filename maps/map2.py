import folium
map = folium.Map(location = [53.55, -113.49], zoom_start = 6, tiles = "Stamen Terrain")
map.add_child(folium.Marker(location=[53.54, -113.40], popup = "Hi There I'm the Marker", icon = folium.Icon(color = 'red')))
map.save("Map1.html")

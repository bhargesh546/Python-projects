# pip install folium 
# for folium everything spins around a map object
# for location we use latitude which ranges from (-90 to 90) and longitude which ranges from (-180 to 180)

import folium

m = folium.Map(location=[79, -100.6], zoom_start=6, tiles="Stamen Terrain", attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors")
m.save("Map1.html")
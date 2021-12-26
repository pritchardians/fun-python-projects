import pandas
import folium
import random
import time
import webbrowser
from funs import add_marker
from resources.art import ascii_art
from funs import clue

where_on_earth_data = pandas.read_csv('event_locations.csv')
latitudes = list(where_on_earth_data['latitude'])
longtitudes = list(where_on_earth_data['longtitude'])
titles = list(where_on_earth_data['title'])
descriptions = list(where_on_earth_data['description'])
clue1 = list(where_on_earth_data['location_clue_01'])
clue2 = list(where_on_earth_data['location_clue_02'])
clue3 = list(where_on_earth_data['location_clue_03'])
findme_index = random.randint(0, len(latitudes) - 1)
findme_lat = latitudes[findme_index]
findme_long = longtitudes[findme_index]
findme_title = titles[findme_index]
findme_description = descriptions[findme_index]
findme_clue = []
findme_clue.append(clue1[findme_index])
findme_clue.append(clue2[findme_index])
findme_clue.append(clue3[findme_index])

where_on_earth_map = folium.Map(location=[findme_lat, findme_long], zoom_start=2
                                , tiles='Stamen Terrain')

fg_base = folium.FeatureGroup(name='Where On Earth?')
fg_borders = folium.FeatureGroup(name='Borders')

fg_base.add_child(
    folium.Marker(location=[findme_lat, findme_long], popup='<strong>You found me!</strong> <br> <br>' + findme_title,
                  icon=folium.Icon(color='cadetblue')))

for _ in range(0, 3):
    decoy_index = random.randint(0, len(latitudes) - 1)
    while decoy_index == findme_index:
        decoy_index = random.randint(0, len(latitudes) - 1)
    add_marker.add_decoy(fg_base, latitudes[decoy_index], longtitudes[decoy_index])

fg_borders.add_child(folium.GeoJson(data=open('./resources/world.json', 'r', encoding='utf-8-sig').read()))

ascii_art.print_earth()
ascii_art.print_where_on_earth_text()

print('When a map appears in your browser, choose the marker that I am about to describe.')
time.sleep(.5)
print(findme_description)
time.sleep(.5)

where_on_earth_map.add_child(fg_base)
where_on_earth_map.add_child(fg_borders)
where_on_earth_map.add_child(folium.LayerControl())
web_page_name = 'where_on_earth.html'
where_on_earth_map.save(web_page_name)
_ = input('Press <ENTER> to see the map')
webbrowser.open(web_page_name, new=2)

for num in range(0, 3):
    clue.give_clue(num, findme_clue)

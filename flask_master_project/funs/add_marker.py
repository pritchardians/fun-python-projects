import folium

def add_decoy(feature_group, long, lat):
    feature_group.add_child(folium.Marker(location=[long, lat], popup='<strong>Not here!</strong> <br> <br> Get a clue.',
                               icon=folium.Icon(color='cadetblue')))


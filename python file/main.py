import folium
import pandas

data = pandas.read_csv("118 Volcanoes.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["NAME"])
elv = list(data["ELEV"])

def color(elvation):
    if elvation<1000:
        return 'green'
    elif 1000<=elvation < 3000:
        return 'orange'
    else:
        return 'red'       

map = folium.Map(location=[38.58,-99.09],tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Valcnos")


for lt,ln,nn,el in zip(lat,lon,name,elv):
    fgv.add_child(folium.Marker(location=[lt,ln],popup=nn,icon=folium.Icon(color=color(el))))

fgp = folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x["properties"]["POP2005"] < 10000000 else 'orange' if 10000000<=x["properties"]['POP2005']<20000000 else 'red'}))    


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
 
map.save("Map1.html")
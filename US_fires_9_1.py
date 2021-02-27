import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open("US_fires_9_1.json", "r")

fire_data = json.load(infile)

# Create empty list to hold the list of brightness, longitude and latitude
brightness, longs, lats = [], [], []
for fires in fire_data:
    bright = fires["brightness"]
    long = fires["longitude"]
    lat = fires["latitude"]

    # Check only fires with brightness factor above 450
    if bright > 450:
        # Append to the empty list
        brightness.append(bright)
    longs.append(long)
    lats.append(lat)

# Map Data and Format
map_data = [
    {
        "type": "scattergeo",
        "lon": longs,
        "lat": lats,
        "marker": {
            "size": [0.03 * bright for bright in brightness],
            "color": brightness,
            "colorscale": "Solar",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

map_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")
figure = {"data": map_data, "layout": map_layout}

# Show the map
offline.plot(figure, filename="US_fires_9_1.html")
print("The program ran successfully!")
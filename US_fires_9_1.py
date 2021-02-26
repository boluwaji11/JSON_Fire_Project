import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fires_9_1.json", "w")

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)
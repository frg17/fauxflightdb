"""
Aðal script fyrir db generator
"""
from ffdbessentials import Airport, Flight

departure_times = None

with open("departuretimes.txt", "r") as f:
    times = f.read()
    times = times.split(";")
    times = list(filter(lambda s: s != "", times))
    departure_times = times

airports = [
    Airport("Akureyri", 605, 194),
    Airport("Reykjavík", 262, 513),
    Airport("Ísafjörður", 174, 96),
    Airport("Egilsstaðir", 935, 262)
]


print(departure_times)
print(airports)
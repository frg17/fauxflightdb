"""
Aðal script fyrir db generator
"""
from ffdbessentials import Airport, Flight
import random
import codecs

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

def get_random_departure_time():
    """
    Skilar random farartíma
    """
    return departure_times[random.randint(0, len(departure_times) - 1)]

def get_random_airports(): 
    """
    Skilar 2 mismunandi flugvöllum
    """
    ap1 = random.randint(0, len(airports) -1)
    ap2 = random.randint(0, len(airports) -1)
    while ap2 == ap1:
        ap2 = random.randint(0, len(airports) -1)

    return (airports[ap1], airports[ap2])



with codecs.open("flights.txt", "w", "utf-8-sig") as f:
    for i in range(0, 100):
        dep_time = get_random_departure_time()
        airp = get_random_airports()
        flight = Flight(airp[0], airp[1], dep_time)
        flightinfo = "{} to {} at {}. Estimated travel time: {} minutes.\n".format(
            flight.origin.name, flight.destination.name, flight.departure_time, flight.travel_time
        )
        f.write(flightinfo)


"""
Aðal script fyrir db generator
"""
from ffdbessentials import Airport, Flight, Dates
import random
import codecs

# Les inn mögulega departure times og geymi í lista.
departure_times = None
with open("./files/departuretimes.txt", "r") as f:
    times = f.read()
    times = times.split(";")
    times = list(filter(lambda s: s != "", times))
    departure_times = times

# Bý til flugvelli sem hægt er að nota
airports = [
    Airport("Akureyri", 605, 194),
    Airport("Reykjavík", 262, 513),
    Airport("Ísafjörður", 174, 96),
    Airport("Egilsstaðir", 935, 262)
]

# Bý til random föll.
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


# Bý til random flugferðir
with codecs.open("./files/flights.txt", "w", "utf-8-sig") as f:
    n = 100
    dates = Dates.get_n_random_future_dates(n, 200)
    for i in range(0, n):
        dep_time = get_random_departure_time()
        airp = get_random_airports()    
        flight = Flight(airp[0], airp[1], dates[i], dep_time)
        flightinfo = "{} to {} on {}.{}.{} at {}. Estimated travel time: {} minutes.\n".format(
            flight.origin.name, flight.destination.name,
            flight.date.day, flight.date.month, flight.date.year,
            flight.time, flight.travel_time
        )
        f.write(flightinfo)


"""
Aðal script fyrir db generator
"""
from ffdbessentials import Airport, Flight, Dates, FFDB
import random
import codecs
from getpass import getpass

departure_times = None
airports = None

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

def generate_random_flights(n):
    """
    Býr til n marga Flight hluti.
    """
    flights = []
    dates = Dates.get_n_random_future_dates(n, 365)

    for i in range(0, n):
        dep_time = get_random_departure_time()
        airp = get_random_airports()    
        flights.append(Flight(airp[0], airp[1], dates[i], dep_time))
    
    return flights


def make_and_seed_database():
    """
    Býr til gagnagrunn, býr til n flug og 
    setur þau inn í nýja gagnagrunninn
    """
    usern = input("Postgres user: ")
    passw = getpass()
    try:
        FFDB.init_db(usern, passw)
        conn = FFDB.connect(usern, passw)
        cur = conn.cursor()

        flights = generate_random_flights(100)
        for f in flights:
            cur.execute("""
                INSERT INTO flights (dateof, timeof, origin, destination, traveltime) 
                VALUES (%s, %s, %s, %s, %s)
                """, (f.date, f.time, f.origin.name, f.destination.name, f.travel_time,))
            
        conn.commit()
        cur.close()
        conn.close()
    except Exception as err:
        print(err)



if __name__ == "__main__":
    # Les in mögulega farartíma
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

    make_and_seed_database()


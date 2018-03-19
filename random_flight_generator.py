"""
Aðal script fyrir db generator
"""
from ffdbessentials import Airport, Flight, Dates, FFDB, Seats
import random
from getpass import getpass

departure_times = None
airports = None

# Bý til random föll.
def get_random_flno(airp):
    """
    Býr til semi handahófskennt flugnumer
    """
    #airp inniheldur 2 strengi
    flno = "{}{}{}".format(airp[0].name[:2], airp[1].name[:2], random.randint(100, 999))
    return flno

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


def get_total_seats(airp):
    """
    Býr til fjölda sæta í flugvél
    """
    if (airp[0].name is not 'Reykjavík') and (airp[1].name is not 'Akureyri'):
        ran = random.random()
        if(ran < 0.8):
            seats = 32
        else:
            seats = 72
    else:
        seats = 72
    return seats


def generate_random_flights(n):
    """
    Býr til n marga Flight hluti.
    """
    flights = []
    dates = Dates.get_n_random_future_dates(n, 93)

    for i in range(0, n):
        dep_time = get_random_departure_time()
        airp = get_random_airports()    
        flno = get_random_flno(airp)
        seats = Seats.make_seats(get_total_seats(airp))
        flights.append(Flight(flno, airp[0], airp[1], dates[i], dep_time, seats))
    
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
        FFDB.save_airports(usern, passw, airports)
        conn = FFDB.connect(usern, passw)
        cur = conn.cursor()

        flights = generate_random_flights(100)
        for f in flights:
            cur.execute("""
                INSERT INTO flights (flno, dateof, timeof, origin, destination, traveltime) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
                """, (f.flno, f.date, f.time, f.origin.name, f.destination.name, f.travel_time,))
            flid = cur.fetchone()[0]
            for seat in f.seats:            
                cur.execute("INSERT INTO seats (flightid, seatid, booked) VALUES (%s, %s, %s);",
            (flid, seat[0], seat[1]))

        conn.commit()
        cur.close()
        conn.close()
    except Exception as err:
        print("rfg; make_and_seed_database: {}: ".format(err))



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
        Airport("Egilsstaðir", 935, 262),
        Airport("Keflavík", 190, 540)
    ]

    make_and_seed_database()


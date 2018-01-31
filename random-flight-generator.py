import random

# Note þennan klasa til að búa til flug.
# Þurfum að bæta við öllum properties sem
# við notum. (arrival date og stuff)
class Flight:
    def __init__(self, departure, arrival):
        self.departure = departure
        self.arrival = arrival



f1 = Flight(random.randint(0, 100), random.randint(0, 100))

print('{};{}'.format(f1.departure, f1.arrival))


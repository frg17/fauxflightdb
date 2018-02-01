"""
Heldur utan um klasana sem við ætlum að nota.
"""
import math

class Flight:
    """
    Note þennan klasa til að búa til flug.
    Þurfum að bæta við öllum properties sem
    við notum. (arrival date og stuff)
    """
    def __init__(self, departure, arrival):
        self.departure = departure
        self.arrival = arrival

class Airport:
    """
    Klasi til að halda utan um flugvöll,
    staðsetningu hans ofl o.s.frv.
    """
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distanceTo(self, destination):
        scale = 95
        kmperunit = 50
        length = math.sqrt((self.x - destination.x)**2 + (self.y - destination.y)**2)
        return round((length / scale) * kmperunit, 0)

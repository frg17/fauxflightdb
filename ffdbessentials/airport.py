"""
Airport class module
"""
import math
import psycopg2

class Airport:
    """
    Klasi til að halda utan um flugvöll,
    staðsetningu hans ofl o.s.frv.
    """
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return "{} ({}, {})".format(self.name, self.x, self.y)

    def distance_to(self, destination):
        """
        Reiknar fjarlægð milli self og destination
        sem er Airport hlutur
        """
        scale = 95
        kmperunit = 50
        length = math.sqrt((self.x - destination.x)**2 + (self.y - destination.y)**2)
        return round((length / scale) * kmperunit, 0)
    
    def set_id(self, id):
        self.id = id
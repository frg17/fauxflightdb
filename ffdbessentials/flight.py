"""
Module containing Flight class
"""
import math

class Flight:
    """
    Heldur utan um eitt flug
    """
    _offset_constant = 1/20
    speed = 295

    def __init__(self, origin, destination, departure_date, departure_time):
        self.origin = origin
        self.destination = destination
        self.date = departure_date
        self.time = departure_time
        self.travel_time = self.calculate_travel_time()

    
    def calculate_travel_time(self):
        """
        Reiknar flugtíma. Nota _offset_constant til þess að
        stytta flugtíma smátt og smátt fyrir lengri flug.
        """
        dist = self.origin.distance_to(self.destination)
        # offset til að hafa flugtima ekki jafn línulegan.
        offset =  (dist - 250) * Flight._offset_constant
        return math.floor(dist / Flight.speed * 60 - offset)
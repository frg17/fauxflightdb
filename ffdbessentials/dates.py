"""
Module sér um allt sem tengist dates.
"""
from datetime import date as Date
import random


def get_n_random_future_dates(n, days_forward):
    """
    Skilar n random dates í framtíðinni.
    """
    dates = []

    today_ordinal = Date.today().toordinal()

    for i in range (0, n):
        random_ordinal = today_ordinal + random.randint(0, days_forward)
        dates.append(Date.fromordinal(random_ordinal))
        
    return dates


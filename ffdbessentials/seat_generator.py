import random

letters = ['A', 'B', 'C', 'D']

def make_seats(n):
    """
    Býr til n mörg sæti, 4 í röð. og setur í lista.
    25% líkur á að það sé "pantað"
    """
    seats = []
    i = 1
    while len(seats) < n:
        for k in letters:
            occupado = True if random.random() > 0.75 else False
            seats.append(('{}{}'.format(i, k), occupado))

        i += 1
    
    return seats

    
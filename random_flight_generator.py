"""
Aðal script fyrir db generator
"""
from ffdbessentials import Airport

ap1 = Airport("Akureyri", 605, 194)
ap2 = Airport("Reykjavík", 262, 513)
ap3 = Airport("Ísafjörður", 174, 96)
ap4 = Airport("Egilsstaðir", 935, 262)

print("{} til {} - {}km".format(ap1.name, ap2.name, ap1.distance_to(ap2)))
print("{} til {} - {}km".format(ap2.name, ap3.name, ap2.distance_to(ap3)))
print("{} til {} - {}km".format(ap4.name, ap1.name, ap4.distance_to(ap1)))
print("{} til {} - {}km".format(ap4.name, ap2.name, ap4.distance_to(ap2)))
print("{} til {} - {}km".format(ap1.name, ap3.name, ap1.distance_to(ap3)))

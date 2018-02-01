"""
Aðal script fyrir db generator
"""

import random
from ffdbessentials import Airport

ap1 = Airport("Akureyri", 605, 194)
ap2 = Airport("Reykjavík", 262, 513)
ap3 = Airport("Ísafjörður", 174, 96)
ap4 = Airport("Egilsstaðir", 935, 262)

print("{} til {} - {}km".format(ap1.name, ap2.name, ap1.distanceTo(ap2)))
print("{} til {} - {}km".format(ap2.name, ap3.name, ap2.distanceTo(ap3)))
print("{} til {} - {}km".format(ap4.name, ap1.name, ap4.distanceTo(ap1)))
print("{} til {} - {}km".format(ap4.name, ap2.name, ap4.distanceTo(ap2)))
print("{} til {} - {}km".format(ap1.name, ap3.name, ap1.distanceTo(ap3)))

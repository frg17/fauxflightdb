"""
Aðal script fyrir db generator
"""

import random
from ffdbessentials import Airport

ap1 = Airport("Akureyri", 605, 194)
ap2 = Airport("Reykjavík", 262, 513)
ap3 = Airport("Ísafjörður", 174, 96)
ap4 = Airport("Egilsstaðir", 935, 262)

print(str(ap1.distanceTo(ap2)))
print(str(ap2.distanceTo(ap3)))
print(str(ap1.distanceTo(ap4)))
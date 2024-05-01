
# Import works in pythons.

# import pandas
# pandas.read_csv()

import math
print(math.floor(4.2343))
print(math.sqrt(9))

from math import sqrt,pi  # only import sqrt and pi
print(sqrt(9)*pi)

from math import *  # this * importing everything
result=sqrt(16)*pi
print(result)


# 'as' keyword
from math import sqrt as s
result=s(25)
print(result)


import math as m
result=m.sqrt(5)*m.pi
print(result)


# dir functions:
import math
print(dir(math))

print(math.nan,type(math.nan))


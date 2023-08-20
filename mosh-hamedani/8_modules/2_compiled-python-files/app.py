"""
. Talked about pycache file stores by python to enhance compilation
. Copy pasted the entire code from previous lecture to see pycache in action
"""

# First Way of importing a module:

from sales import calc_shipping, calc_tax

#Avoid importing the entire modules by - from sales import *
#Import only those modules which you require

calc_shipping()
calc_tax()

# Second Wayof importing a module:

import sales

sales.cal_shipping()
calc_tax()

#Both of the methods are good. Choos anyone











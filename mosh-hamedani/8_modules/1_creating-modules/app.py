"""
. As our program grows, we should split our codes accross multiples files
. We refer to each file as module. So, a module is a file that contains some python code
. A module should contain highly related objects. These objects can be functions, classes, objects and so on..
.  
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











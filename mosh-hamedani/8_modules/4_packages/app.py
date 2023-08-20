"""
We might end up with a lot of python files 
in the same directory.
In order to avoid that we should make sub-directories.
So, over here in this folder we will create another sub-directory
called 'e-commerce' and create a file by the name '__init__.py'
After creating this file, we can call the function easily
"""

import ecommerce.sales

ecommerce.sales.calc_tax


# when we add the file '__init__.py'. Python will treat the
# ecommerce folder as a package

from ecommerce import sales


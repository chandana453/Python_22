#10.program to use specific imports from a module to other modules.

from calc import add
print(add(10,7))

from calc import *
print(sub(9,5))


from math import pi
print("The value of pi is", pi)

import math
print("The value of pi is", math.pi)


# While importing a module, Python looks at several places. Interpreter first looks for a built-in module. Then(if built-in module not found), Python looks into a list of directories defined in sys.path. The search is in this order.

# The current directory.
# PYTHONPATH (an environment variable with a list of directories).
# The installation-dependent default directory.

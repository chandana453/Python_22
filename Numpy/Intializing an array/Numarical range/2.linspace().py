# This is the one more method to initialise the values to the array in the arange function.
# we have to use the function is called linspace(),in this we have to pass the parameters
# (start,stop,step="here step consider as the no of values return b?w the start and step,not the diff value")
# and few more optional parameter are,the end point(it is nothing but to return the end point,defaulit the endpoint is True,if we dont want that,then
# we have write endpoint=False,the point deleted and the value before end value prints)
# anyway if we want to know the diff value,then we have to use the keyword is called retstep=True,then we can get the diff value finally



import numpy as np

a=np.linspace(10,100,10,endpoint=False,retstep=True)
print(a)

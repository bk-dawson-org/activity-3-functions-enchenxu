import math
def volumeCylinder (r,h):
    v= math.pi*(r**2)*h
    return v
    
height=float(input("what is the height of the cake?"))
radius=float(input("what is the radius of the cake?"))

c=round(volumeCylinder(radius,height),3)
print ("volume of the cake is", c )


import math
def getNumberOfSlices(radius,hight,volumeOfSlice):
    v=volumeCylinder(radius,hight)
    n=v/volumeOfSlice
    return n

n=int(input('what is the number of slices that you want?'))


print('the number of slices to be cut is', int(getNumberOfSlices(radius,height,n)) )
print('enjoy!')

#this is a function about calculating volume obviously. 
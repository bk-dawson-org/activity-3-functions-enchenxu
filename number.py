import math
def getNumberOfSlices(radius,hight,volumeOfSlice):
    v=(radius**2)*hight*math.pi
    n=v/volumeOfSlice
    return n

r=float(input('what is the radius of the cake?'))
h=float(input('what is the hight of the cake?'))
n=int(input('what is the number of slices that you want?'))


print('the number of slices to be cut is', int(getNumberOfSlices(r,h,n)) )
print('enjoy!')
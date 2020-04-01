import numpy as np
import matplotlib.pyplot as plt
list1 = [0.254,0.305,0.356,0.406,0.457]
array1=np.array(list1)
def period(array):
#This function takes an array of lengths as a parameter. It finds the theoretical period times based on the given lengths,
#and returns the estimated period value(s).
    n = len(array1)
    for i in range(n):
      T = (2* np.pi) * np.sqrt(array[i]/9.81)
      array[i] = T
    return array 
print(period(array1))
#This graphs the theoretical periods versus length so the relationship between them can be found.
x = list1
y = array1
plt.scatter(x, y,)
plt.title('Estimated Period of Pendulum')
plt.xlabel('Length (m)')
plt.ylabel('Period (s)')
plt.show()
#This assumes that the pedulum will behave under ideal conditions: 
#the rope is massless, there is no air resistance or friction and that the center 
#of mass is in the middle of the bob (bob behaves like a mass point). However,
#In the real world, air resistance and friction are factors that can greatly 
#affect the pedulum as well as the fact that since we are not using a rope, the 
#mass of Legos is not negligigle and factors in to where the center of mass is.
#All these factors, therefore affect the periods calculated.  
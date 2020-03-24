#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:17:11 2020

@author: gackermannlogan
"""
import os
import numpy as np 
import matplotlib.pyplot as plt
path = "/Users/gackermannlogan/mu_code/data_capture/"
os.chdir(path)
print(os.getcwd())
fin = open("10inch-Trial.csv", "r")

array = (np.genfromtxt(fin, delimiter = ","))
x = np.array(array[960:1087,0])
y = np.array(array[960:1087,1])
z = np.array(array[960:1087,2])
time = np.array(array[960:1087,3])

plt.plot(time, x)
plt.plot(time, y)
plt.plot(time, z)
plt.legend("x" "y" "z")
plt.title("Acceleration v. Time")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:40:09 2022
BEST FIT LINE ALGORITHIM
@author: Chase Fashing
"""
import random
import math
import matplotlib.pyplot as plt

demo_or_try = input("Would you like to demo or try new points? ('demo'/'try')")

def get_input_points():
    points = list()
    number_of_points = int(input("How many points would you like to give"))
    for i in range(number_of_points):
        given_x = int(input(f"Point {i} x coordinate: "))
        given_y = int(input(f"Point {i} y coordinate: "))
        points.append((given_x,given_y))
    return points
points = sorted([(1,1.5),(2,3),(3,4.5),(4,7),(4,5)]) if demo_or_try == 'demo' else sorted(get_input_points())


test_signs = [(1,1),(1,-1),(-1,1),(-1,-1)]

def find_error(params):
    B0 = params[0]
    B1 = params[1]
    total_error=0
    for x,y in [point for point in points]:
        total_error+= abs((B0 + B1 * x)  - y)
    return total_error

SPEED = .001

B0 = random.randint(-5,5)
print("B0:",B0)
B1 = random.randint(-5,5)
print("B1:",B1)

#while slope > small number 
    #Variables are B0 and B1
    #Get random B0 and B1
GRADE = 1
while(GRADE > 0.0001):
    print("\n")
    print("B0:",B0)
    print("B1:",B1)
    #TEST SECTION
    #FIND ERROR
    total_error = 0
    for x,y in [point for point in points]:
        total_error += abs((B0 + B1 * x ) - y)
    print("Total Error:",total_error)
    
    #4 Test points
    test_points = []
    for sign_0,sign_1 in [signs for signs in test_signs]:
        test_points.append((B0+GRADE*sign_0,B1+GRADE*sign_1))
    test_errors = []
    for test_point in test_points:
        test_errors.append(find_error(test_point))
    least_index = (test_errors.index(min(test_errors)))
    #direction_signs = test_signs[least_index]
    B0_new= test_points[least_index][0]
    B1_new= test_points[least_index][1]
    #set to slope
    GRADE= SPEED*(abs(find_error((B0,B1))/len(points)-find_error((B0_new,B1_new))/len(points)) / (math.sqrt((B0-B0_new)**2 + (B1-B1_new)**2)))
    print("GRADE:",GRADE)
    B0=B0_new
    B1=B1_new

print("\n")
print("B0:",B0)
print("B1:",B1)

x_points = [point[0] for point in points]
y_points = [point[1] for point in points]
plt.plot(x_points,y_points,'ro')
plt.plot([x_points[0],x_points[-1]],[B0+x_points[0]*B1,B0+x_points[-1]*B1])
plt.show()
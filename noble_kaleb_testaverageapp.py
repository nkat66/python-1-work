#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:51:25 2019

 Kaleb Noble
 2/27/2019
 Python 1 - DAT-119 - Spring 2019
 Grade Average Assignment
 This program takes an input of three test scores from the user, then
   calculates and presents the average.

@author: katnob8
"""

#Introduces the app.
print("Welcome to the Test Average App.")

#Accepts a user-entered first grade, and converts it to a float.
test1 = float(input("Please enter the first test score: "))

#Accepts a user-entered second grade, and converts it to a float.
test2 = float(input("Please enter the second test score: "))

#Accepts a user-entered third grade, and converts it to a float.
test3 = float(input("Please enter the third test score: "))

#Calculates the average of all three tests by adding up the scores,
#then dividing by the total number of scores given (3, in this case).
average = (test1 + test2 + test3) / 3

#Presents the average to the user, formatted to two decimal points.
print("Okay, the average of all these grades is", format(average, ".2f"))
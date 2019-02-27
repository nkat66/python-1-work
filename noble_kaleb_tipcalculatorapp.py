#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:00:12 2019

 Kaleb Noble
 2/27/2019
 Python 1 - DAT-119 - Spring 2019
 Tip Calculator Assignment
 This program takes an input of a meal bill, then calculates and presents the
   user with the 10%, 15%, and 20% tip values.

@author: katnob8
"""
#Set all three tip values for clarity when calculating.

tip10 = float(.10)
tip15 = float(.15)
tip20 = float(.20)

#Introduces the app.
print("Hi there! Welcome to the Tip Calculator App 1.0!")

#Requests that the user inputs the meal bill.
meal_bill = float(input("To start, please provide me with your total bill: "))

#Calculate the 10%, 15%, and 20% tip.
tip_value_10 = meal_bill * tip10

tip_value_15 = meal_bill * tip15

tip_value_20 = meal_bill * tip20

#Presents the total $ of the tip.

print("Okay! Here's what the tip values are: ")

print("10%: ", format(tip_value_10, ".2f"))
print("15%: ", format(tip_value_15, ".2f"))
print("20%: ", format(tip_value_20, ".2f"))





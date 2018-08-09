# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:15:19 2016

@author: cindylee
"""

import math

side_one = float (input ("Please enter the first side: "))
side_two = float (input ("Please enter the second side: "))
side_three = float (input ("Please enter the third side: "))
right_tri = False

if (round ((math.sqrt (side_one**2 + side_two**2)), 5) == side_three):
    right_tri = True
if (round ((math.sqrt (side_two**2 + side_three**2)), 5) == side_one):
    right_tri = True
if (round ((math.sqrt (side_one**2 + side_three**2)), 5) == side_two):
    right_tri = True
    
if (right_tri == True):
    print (str(side_one) + ", " + str(side_two) + ", and ", str (side_three) + " form a right triangle")
else: 
    print ("Not a valid right triangle")
    
month = int (input ("Please enter an integer between 1 and 12: "))

if (month == 1):
    print ("The entered month is January and the number of days is 31.")
elif (month == 2):
    print ("The entered month is February and the number of days is 28.")
elif (month == 3):
    print ("The entered month is March and the number of days is 31.")
elif (month == 5):
    print ("The entered month is May and the number of days is 31.")
elif (month == 7):
    print ("The entered month is July and the number of days is 31.")
elif (month == 8):
    print ("The entered month is August and the number of days is 31.")
elif (month == 10):
    print ("The entered month is October and the number of days is 31.")
elif (month == 12):
    print ("The entered month is December and the number of days is 31.")
elif (month == 4):
    print ("The entered month is April and the number of days is 30.")
elif (month == 6):
    print ("The entered month is June and the number of days is 30.")
elif (month == 9):
    print ("The entered month is Sepetember and the number of days is 30.")
else:
    print ("The entered month is November and the number of days is 30.")
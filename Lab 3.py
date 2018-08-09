# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:02:38 2016

@author: cindylee
"""

import math 
language = input ("Enter a language: ")

if (language == "es"):
    print ("¡Hola mundo!")
elif (language == "cn"):
    print ("你好世界!")
elif (language == "fr"):
    print ("Bonjour monde!")
else:
    print ("Hello world!")

num = int(input ("Enter a number: "))

if (num%2 == 0):
    print ("Even")
else:
    print ("Odd")
    
num_less = int (input ("Enter a number less than 100: "))
roman = ""
if (num_less//50 >= 1):
    roman += "L"
    num_less-=50
if (num_less//10 >= 1):
    repeat = num_less//10
    if (repeat == 4):
        roman += "XXXX"
        num_less -=40
    elif (repeat == 3):
        roman += "XXX"
        num_less-=30
    elif (repeat ==2):
        roman += "XX"
        num_less-=20
    else:
        roman += "X"
        num_less-=10
if (num_less//5 >=1):
    roman += "V"
    num_less-=5
if (num_less > 0):
    if (num_less == 4):
        roman += "IIII"
    elif (num_less ==3):
        roman += "III"
    elif (num_less == 2):
        roman += "II"
    else:
        roman += ("I")

print (num_less, "in roman numeral is:", roman)

name = input ("Please enter your name: ")
grad = int (input ("Please enter your graduation year: "))
year = int (input ("Please enter your current year: "))
if (grad - year == 0):
    print (name, "has already graduated.")
elif (grad - year == 1):
    print (name, "is a senior.")
elif (grad -year == 2):
    print (name, "is a junior.")
elif (grad - year == 3):
    print (name, "is a sophomore.")
elif (grad - year == 4):
    print (name, "is a freshman.")
else:
    print (name, "is not in college yet.")

time_hour = int (input("Please enter a time in 24hour format: "))
hour = time_hour//100
minute = time_hour%100
hour_twelve = 0
if (hour > 12):
    hour_twelve= hour-12
    """
    if (hour == 13):
        hour_twelve = 1
    elif (hour == 14):
        hour_twelve = 2
    elif (hour == 15):
        hour_twelve = 3
    elif (hour == 16):
        hour_twelve = 4
    elif (hour == 17):
        hour_twelve = 5
    elif (hour == 18):
        hour_twelve = 6
    elif (hour == 19):
        hour_twelve = 7
    elif (hour == 20):
        hour_twelve = 8
    elif (hour == 21):
        hour_twelve = 9
    elif (hour==22):
        hour_twelve = 10
    elif (hour == 23):
        hour_twelve = 11
    else:
        hour_twelve = 12
        """
else:
    print (hour, ":", minute, "in 12 hour format: ", hour, ":", minute, "A.M.")

#print (hour, ":", minute, "in 12hr format: ", hour_twelve, ":", minute)
hour_time_str = str(hour) + ":" + str (minute) + " in 12 hour format: " + str(hour_twelve) + ":" + str(minute) + " P.M."
print (hour_time_str)

leg_one = float (input("Please enter the first leg: "))
leg_two = float (input("Please enter the second leg: "))
hypotenuse = float (input ("Please enter a hypotenuse: "))

if (round (math.sqrt(leg_one**2 + leg_two**2),5) == hypotenuse):
    print (leg_one, ",", leg_two, ", and", hypotenuse, "form a right triangle")
else:
    print ("Not a valid right triangle.")
            
val_a = int (input ("Please enter a value for a: "))
val_b = int (input ("Please enter a value for b: "))
answer = 0
if (val_a==0):
    if (val_b==0):
        print ("infinite soluton")
    else:
        print ("no solution")
else:
    answer = val_b * -1 / val_a
    print ("The equation has a single solution and x =", answer)



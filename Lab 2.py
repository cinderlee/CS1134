# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:02:54 2016

@author: cindylee
"""

import math 
import turtle

kilo = int (input ("Please enter an integer for kilogram amount: "))
ounce = kilo * 2.2046 * 16
pound = ounce // 16
ounce = ounce % 16


print (kilo, "kilograms is", round (pound, 2), "pounds and", round (ounce,4) , "ounces")

day_num = int (input("Please enter a number of days: "))
week = day_num //7
day = day_num % 7

print (day_num, "days is equal to", week, "weeks and", day, "days")

rad = int (input("Please enter a radius: "))
circum = 2*rad*math.pi
area = rad**2 * math.pi

print("Circumference is: ", round (circum,4))
print ("Area is: ", round (area, 4))
"""
turtle.forward (100)
turtle.left (60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left (60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)

turtle.done ()
"""
"""
bday = input("Please enter a birth date: ")
today= input ("Please enter today's date: ")
year_born = bday [ 0: 4]
year_born_int = int(year_born)
year_today = today [0:4]
year_today_int = int (year_today)
month_born = bday [4:6]
month_born_int = int (month_born)
month_today = today [4:6]
month_today_int = int(month_today)
day_born = bday [6:8]
day_born_int = int(day_born)
day_today = today [6:8]
day_today_int = int(day_today)
days_born = (365 * year_born_int) + (30 * month_born_int) + day_born_int
days_today = (365 * year_today_int) + (30 * month_today_int) + day_today_int
days_old = days_today-days_born
year_total = days_old // 365
months_total = (days_old%365)//30
day_total = (days_old % 365) % 30
print ("You are", year_total, "years,", months_total, "months, and", day_total, "days old.")
"""

bday = int (input ("Please enter a birth date:"))
today = int (input ("Please enter today's date: "))
year_born = bday // 10000
year_today= today//10000
month_born = bday % 10000 // 100
month_today= today % 10000 // 100
day_born = bday % 100
day_today = today % 100
total_day_born = 365 * year_born + 30 * month_born + day_born
total_day_today = 365 * year_today + 30 * month_today + day_today
total_day = total_day_today - total_day_born
years = total_day // 365
months = total_day % 365 // 30
days = total_day % 365 % 30
print ("You are", years, "years,", months, "months, and", days, "days old.")

first_feet = int (input ("Please enter the first length's feet: "))
first_yard = int (input ("Please enter the first length's yard: "))
second_feet = int (input ("Please enter the second length's feet: "))
second_yard = int (input ("Please enter the second length's yard: "))

total_feet = first_feet + first_yard * 3 + second_feet + second_yard * 3
total_yard = total_feet // 3
new_feet = total_yard % 3
print ("Their sum is:", total_yard, "yards and", new_feet, "feet.")

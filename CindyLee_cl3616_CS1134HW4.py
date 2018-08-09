# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:57:46 2017

@author: cindylee
"""

"""
Name: Cindy Lee
Net ID: cl3616
N12335562
Homework 4
"""

#Question 1
def insomewhere(X,s):
    for index in range (len (X)):
        if X[index] == s:
            return True
        if isinstance (X[index], list):
            return insomewhere (X [index], s) or insomewhere (X[index + 1], s) 
    return False
            
A=[[1,2],[3,[[[4],5]],6],7,8]
print(insomewhere(A,6)) #True
print(insomewhere(A,4))
print(insomewhere(A,66)) #False
print(insomewhere ([], 6))

#Question 2
def unnest (lst, i = 0):
    if i == len (lst):
        return []
    if isinstance (lst [i], list):
        return unnest (lst[i], 0) + unnest (lst, i + 1)
    return [lst[i]] + unnest (lst, i + 1)
    

A=[[1,2],[3,[[[4],5]],6],7,8]
print(unnest(A))
print(A) 


#Question 3
def print2d (lst):
    print ("[")
    for i in lst:
        print (" " + str (i))
    print ("]")        
    
print2d([[i]*5 for i in range(5)])



#Question 4
def triangle (n):
    lst = []
    z = n - 1
    while z >= 0:
        lst.append ([i for i in range (n, z , -1)])
        z -= 1
    return lst

print2d(triangle(5))
print2d(triangle(10))



#Question 5
def table(f,xrange,yrange):
    lst = []
    for y in yrange:
        lst2 = []
        for x in xrange:
            lst2.append (f (x, y))
        lst.append (lst2)
    return lst
    
print2d(table(pow,[1,2,10],range(10,15)))



#Question 6
def nest (x, n):
    if n == 0:
        return x
    y = []
    y.append (nest (x, n-1))
    return y

print(nest ("nest",2))
print (nest (5, 0))
print (nest (5, 1))
print(nest (53,10))
print(unnest(nest(53,10)))
print(unnest (nest ("nest",2)))
print(unnest (nest (5, 1)))

#Question 7
A = [[1],[1]] * 5
print(A)
A[3][0]=5
print(A)
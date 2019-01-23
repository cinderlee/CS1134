# -*- coding: utf-8 -*-


"""
Name: Cindy Lee
Net ID: cl3616
N12335562
Homework 2
Note: Please refer to document for explanations of runtime.
"""

#Write a short recursive Python function that finds the minimum and maximum 
#values in a sequence without using any loops.

def minandmax (lst, minimum = None, maximum = None, copy = False):
    if len (lst) == 0:
        return minimum, maximum    
    if copy == False:
        copy = True
        lst = lst [:]
        minimum = lst [0]
        maximum = lst [0]
    last = lst.pop()
    if last > maximum:
        maximum = last
    elif last < minimum:
        minimum = last
    return minandmax (lst, minimum, maximum, copy)

#runtime is O(n)
    
print (minandmax ([4, 8, 12, 74, -1, 1041, 3 ,1, 54]))
print (minandmax ([1]))
print (minandmax ([]))



#Describe a recursive algorithm to compute the integer part of the base-two
#logarithm of n using only addition and integer division.

def intlog (number, start = 0):
    if number <= 0:
        return None
    if number // 2 == 0:
        return start
    return intlog (number//2, start + 1)
    
#runtime is log (n)
    
print (intlog (16))
print (intlog (500))



#Describe an efficient recursive function for solving the element uniqueness
#problem, which runs in time that is at most O(n^2) in the worst case
#without using sorting.

def unique (lst, start = 0, end = None):
    if end == None:
        end = start + 1
    if start == len (lst): 
        return True 
    elif end == len (lst):
        start = start + 1
        end = start + 1
        return unique (lst, start, end)
    if lst [start] == lst [end]:
        return False
    else:
        return unique (lst, start, end + 1) 
    
#runtime is O(n^2)
    
print (unique ([1, 2, 3 ,4 ,5]))
print (unique ([34, 7457, 1, 3, 53, 5, 1, 8]))
    
    
    
    
#Write a recursive function that will output all the subsets of a set of n
#elements (without repeating any subsets).


def subset (lst, start = 0):
    if start == len (lst):
        return [[]]
    sublist = subset (lst, start + 1)
    return sublist + [[lst[start]] + subby for subby in sublist]
    
#runtime is O(n^3)
    
print (subset ([1, 2, 3, 4, 5]))
print (subset ([1, 2, 3]))
print (subset ([1,2,3,4]))




#Write a short recursive Python function that determines if a string s is a
#palindrome, that is, it is equal to its reverse. For example, racecar and
#gohangasalamiimalasagnahog are palindrome.

def palindrome (string, start = 0):
    if string [start] != string [len(string) - start - 1]:
        return False
    if start > len (string) - start - 1:
        return True
    return palindrome (string, start + 1)
    
#runtime is O(n)
    
print (palindrome ("gohangasalamiimalasagnahog"))
print (palindrome ("racecar"))
print (palindrome ("ifjioweg"))



#Given an unsorted sequence, S, of integers and an integer k, describe a
#recursive algorithm for rearranging the elements in S so that all elements
#less than or equal to k come before any elements larger than k. What is
#the running time of your algorithm on a sequence of n values?

def rearrange (S, k, start = 0, end = None):
    if end == None:
        end = len (S) - 1
    if start == end:
        return S
    if S [start] > k:
        store = S [end]
        S [end] = S [start]
        S [start] = store
        return rearrange (S, k, start, end - 1)
    else:
        return rearrange (S, k, start + 1, end)

#runtime is O(n)
    
print (rearrange ([ 325, 8, 32, 59, 100, 20, 90], 80))
print (rearrange ([325, 80, 80, 3, 225, 1, 3 ,8, 63], 80))
    
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 21:32:44 2018

@author: sevgi
"""
#it takes k sorted arrays, each with n elements, and combines them into a single sorted array that has k x n elements. 

#I used merge sort algorithm for this problem
#This algorithm will divide the list into two parts ,until the best case occur.
#Then will merge the list element two by two.
#For instance ;we have 4 sorted arrays with this form : list[[],[],[],[]].This method will take list[0] and
#list[1] and will merge them ; it will merge list[3] and list[4] in the meantime.Then it will merge the result of previos merges. 
def mergesort(list,size):
    #best case:if list has only  one element return list.
    if len(list) < 2:
        return list 
    middle = len(list)//2
    #divide the list into two parts
    left = mergesort(list[:middle],size) 
    right = mergesort(list[middle:],size)
    if(not(middle==size//2)):# make list the result of merge if method does not reach the end.
        return [merge(left[0], right[0])]#we send the first element of the left and right into the merge because the form
                                       #of right and left are [[]] so we need to remove first brackets.Then we take the output of merge and add brackets back.
    return  merge(left[0], right[0])#if method reachs the end return the result of merge.

#the function merge is not change.
def merge(left, right):
    result = []
    i, j = 0, 0
    while ((i<len(left) ) and (j < len(right))):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
    while i < len(left):
        result.append(left[i])
        i=i+1
    while j < len(right):
        result.append(right[j])
        j+= 1
    return result
 
    
#standard form for input list.    
list =[[2,7,9,11,15],[1,3,5,8,10],[1,3,5,6,10],[1,3,5,7,10],[31,44,55,60,85],[11,18,19,20,20]] 
print("Given array is")
print(list); 
print("Sorted array is")
print(mergesort(list,len(list)))
print("\n")
list =[[2,7,9,11,15],[1,3,5,8,10],[1,3,5,6,10],[1,3,5,7,10],[31,44,55,60,85]] 
print("Given array is")
print(list);
print("Sorted array is")
print(mergesort(list,len(list)))
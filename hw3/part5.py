# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:40:01 2018

@author: sevgi
"""
#takes as input constraints B over variable A and decides 
#whether the constraints can be satisfied
def isSatisfiable(A,B):
    #check each consraints in B
    for i in range(len(B)):
        #second index holds '!' or '=',thus make comparison
        #according to the content of the secon element of the B[i]
        if(B[i][2]=='='):#check equality constraints
            if(A[int(B[i][1])]!=A[int(B[i][4])]):
                return False
        else:#check inequality constraints
            if(A[int(B[i][1])]==A[int(B[i][5])]):
                return False
    return True
    
input1=[2,5,2,3]#standard form for variables
input2=[("x0=x2"),("x1!=x3")]#standard form for constraints
print("variables :"+str(input1))
print("constraints :"+str(input2))
print("output:"+str(isSatisfiable(input1,input2)))
print("\n")

input2=[("x1=x2"),("x2!=x3")]
print("variables :"+str(input1))
print("constraints :"+str(input2))
print("output:"+str(isSatisfiable(input1,input2)))
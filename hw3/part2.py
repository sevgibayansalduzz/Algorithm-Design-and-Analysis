# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:48:04 2018

@author: sevgi
"""

def optimalCost(n,M,NY,SF):

    cost=[]
    cost.append(NY[0])#When we start from NY, we will keep the cost in C [0].
    cost.append(SF[0])#When we start from SF, we will keep the cost in C [1].
    
    flagN=True## if flagN true it means we are in NY
    
    #first iteration calculates the cost which denotes when we start from NY,and 
    #second first iteration calculates the cost which denotes when we start from SF
    for i in range(2):
        for j in range (1 ,n):
            if(flagN):#if we are in NY
                cost[i]=cost[i]+min(NY[j],SF[j]+M)#compares the NY cost with the sum of the M and SF costs.
                if(SF[j]+M<NY[j]):#if the costs of SF is less than NY,we will be in  the SF.
                    flagN=False
            else:##if we are in SF
                cost[i]=cost[i]+min(SF[j],NY[j]+M)#compares the SF cost with the sum of the M and NY costs.
                if(NY[j]+M<SF[j]):#if the costs of NY is less than SF,we will be in  the SF.
                    flagN=True
        flagN=False
    return min(cost[0],cost[1])#Choose the minumum cost
    
#samples
n=5
M=20
NY=[1,3,6,1,7]
SF=[20,10,5,8,1]
print("n: "+str(n)+" M: "+str(M)+" NY: "+ str(NY)+" SF: "+ str(SF))
print("Cost:"+str(optimalCost(n,M,NY,SF)))


n=4
M=10
NY=[1,3,20,30]
SF=[50,20,2,4]
print("n: "+str(n)+" M: "+str(M)+" NY: "+ str(NY)+" SF: "+ str(SF))
print("Cost:"+str(optimalCost(n,M,NY,SF)))
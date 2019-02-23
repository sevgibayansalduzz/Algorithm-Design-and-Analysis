# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:48:04 2018

@author: sevgi
"""

def OptimalPlan(NY,SF,M):
    StartNY,temp,StartSF= NY[0],NY[0],SF[0]
    for i in range(1,len(NY)):
        StartNY = NY[i] + min(temp,M+StartSF)
        StartSF = SF[i] + min(StartSF,M+temp)
        temp = StartNY
    return min(StartNY,StartSF)

#samples
M=20
NY=[1,3,6,1,7]
SF=[20,10,5,8,1]
print(" M: "+str(M)+" NY: "+ str(NY)+" SF: "+ str(SF))
print("Cost:"+str(optimalCost(M,NY,SF)))

M=10
NY=[1,3,20,30]
SF=[50,20,2,4]
print(" M: "+str(M)+" NY: "+ str(NY)+" SF: "+ str(SF))
print("Cost:"+str(optimalCost(M,NY,SF)))
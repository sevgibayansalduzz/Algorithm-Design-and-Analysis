# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:29:42 2018

@author: sevgi
"""
def calculateOptimalRoute(hotelList):
    path = [-1]*(len(hotelList))
    penalty = [0]*(len(hotelList))
    
    for i in range (len(hotelList)):
        penalty[i] = (200 - hotelList[i])**2#Calculate the penalty of each stop (200 — ai)^2
        path[i] = -1
        for j in range(i):
            temp = penalty[j] +((200 - (hotelList[i] - hotelList[j]))**2);#Calculate total penalty
            if (temp < penalty[i]):#choose the minimum penalty
                penalty[i] = temp; 
                path[i] = j#save the path into the array path
    output=[]
    for i in range (len(path)):#Take the hotels distance according to elements of path and add distances into the output
        if (path[i]>=0 and not(hotelList[path[i]] in output)):
            output.append(hotelList[path[i]])
    output.append(hotelList[len(hotelList)-1])        
    return output;

print("Optimum path:"+str(calculateOptimalRoute([20, 40, 60, 940, 1500])))
print("Optimum path:"+str(calculateOptimalRoute([190, 420, 550, 660, 670])))
print("Optimum path:"+str(calculateOptimalRoute( [190, 220, 410, 580, 640, 770, 950, 1100, 1350] )))

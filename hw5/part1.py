# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:46:06 2018

@author: sevgi
"""
#I used selection sort algorithm to choose scheduling problem.
#This method sorts jobs increasing order according to their weight,and calculate the weighted sum of the completion times in 
#the meantime.After calculating is over ,this method returns the minimize weighted sum.
def schedulingTheJobs(jobs):
    Csum=0#Create finishing time
    Wsum=0#Create weighted completion time
    for j in range(len(jobs)):#selection sort step
        max=j#take j as maximum
        for i in range(j+1,len(jobs)):#selection sort step
            if(jobs[i][1]>jobs[max][1]):#sorts jobs increasing order according to weight
                max=i
        Csum=Csum+jobs[max][0]#Calculate the completion time
        Wsum=Wsum+Csum*jobs[max][1]#Calculate the weighted completion time
        if(max!=j):
            jobs[max],jobs[j]=jobs[j],jobs[max]##swap the jobs 
    return Wsum       


#standard form jobs=[(ti,wi),(tj,wj).....]
jobs=[[3,2],[1,10]]
print("Given jobs=> "+str(jobs))
print("minimum weighted sum:"+str(schedulingTheJobs(jobs)))
print("Order of jobs=> "+str(jobs))

print("\n")
jobs=[[2,3],[1,10],[3,5]]
print("Given jobs=> "+str(jobs))
print("minimum weighted sum:"+str(schedulingTheJobs(jobs)))
print("Order of jobs=> "+str(jobs)) 

print("\n")
jobs=[[2,3],[1,10],[3,5],[2,11],[1,15]]
print("Given jobs=> "+str(jobs))
print("minimum weighted sum:"+str(schedulingTheJobs(jobs)))
print("Order of jobs=> "+str(jobs)) 
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 09:43:08 2018

@author: sevgi
"""
# takes as input the list of n people and the list of pairs who know each other, and outputs the best choice of party invitees.
def partyInvitees(people,pairs):
    output=[]
    known=[]
    #take a person and calculate that how many people he/she knows. 
    for i in range (len(people)):
        count=0#reset count
        for j in range(len(pairs)):#search this person in pairs
            if(people[i] in pairs[j]):#if this person is in  pair[j] ,increase count by 1
                count=count+1
        known.append(count)#append 'count' into the array known.(this person is in the ith index and known[i] represents the number of people whohe/she knows)
    for i in range(len(people)):#Take a person and make a decision to invite this person to the party or not
        #if this person should have at least five other people whom they know 
        #and five other people whom they don't know,add this person into the array output .
        if(known[i]>=5 and (len(people)+1 -known[i]) >=5):
            output.append(people[i])#this array includes people who will ne inviteed to the party.
    return output

#Standard form for people
people=["Jane","Bill","Susan","Tom","Jim","Mary","Will","Mick","Rory","Lindsay",
        "Kate","Karen","Joe","Martha","Arthur","Taylor","Connor"]

#standard form for pairs
pairs=[("Jane","Bill"),("Jane","Susan"),("Jane","Tom"),("Jane","Jim"),("Jane","Will"),("Jane","Connor"),
      ("Bill","Kate"),("Bill","Susan"),("Bill","Martha"),("Bill","Arthur"),("Bill","Karen"),
      ("Susan","Will"),("Susan","Tom"),("Susan","Jim"),("Susan","Taylor"),
      ("Tom","Will"),("Tom","Rory"),("Tom","Kate"),
      ("Jim","Joe"),
      ("Mary","Rory"),("Mary","Kate"),("Mary","Lindsay"),
      ("Will","Kate"),("Will","Rory"),
      ("Mick","Rory"),("Mick","Kate"),("Mick","Connor"),("Mick","Arthur"),("Mick","Martha"),
      ("Rory","Kate"),
      ("Lindsay","Kate"),
      ("Karen","Martha"),("Karen","Arthur"),
      ("Joe","Martha"),("Joe","Taylor"),("Joe","Connor"),("Joe","Arthur"),
      ("Arthur","Connor")
      ]

print(partyInvitees(people,pairs))

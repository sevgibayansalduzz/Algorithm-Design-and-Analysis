# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:16:07 2018

@author: sevgi
"""

dictionary={"it","was","the","best","of","times","you","can",
            "add","new","words","here","are"} 

def isValid(string):
    #if length is 0 return false
    if(len(string)==0):
        return False;
    s2="";
    for i in range(len(string)+1):
          #s2 is a word ,delete s2 and add the next letter into it
        if(s2 in dictionary):
            if(i!=len(string)):
                s2=string[i].lower()
            else:
                s2=""#if the func reach the end of string ,add nothing
        else:#s2 is not  a word, concatanete s2  with the next letter
            if(i!=len(string)):
                s2=s2+string[i].lower()
    if(s2==""):
        return True
    else:
        return False

#given string
print(isValid("itwasthebestoftimes"))
print(isValid("youarethebest"))
print(isValid("besttimesks"))
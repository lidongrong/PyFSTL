# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:08:05 2022

@author: lidon
"""
import random
from vectorADT import*



# swap i and j
def swap(i,j):
    i=i+j
    j=i-j
    i=i-j
    return i,j

# copy function
def copy(self):
    new_arr=self.elements.copy()
    u=vector(new_arr)
    return u
# bind copy to vector
vector.copy=copy

# implement unsort()
# unsort elements in [low, high)
# use Knuth shuffling
def unsort(self,low=None,high=None):
    if low==None and high==None:
        low=0
        high=self.length
    for k in range(low,high):
        index=random.randint(k,high-1)
        self[k],self[index]=swap(self[k],self[index])
# bind unsort to vector
vector.unsort=unsort

#implement size()
def size(self):
    return self.length
#bind size() to vector
vector.size=size

#implement find()
# find e from [low,high)
# find the smallest index that equals to e
# if fail to find e, return -1
def find(self,e,low=None,high=None):
    if low==None and high==None:
        low=0
        high=self.length
    for k in range(low,high):
        if self[k]==e:
            return k
    return -1
# bind find to vector
vector.find=find

# insert e into position r
# return r after executing
def insert(self,r,e):
    self.elements.append(0)
    i=self.length
    # don't use add, since traversing backward have time complexity O(n-r)
    while i!=r:
        self.elements[i]=self.elements[i-1]
        i=i-1
    self.elements[i]=e
    self.length=self.length+1
    return r
#bind insert to vector
vector.insert=insert

# implement remove_index
# return number of elements deleted
# time complexity O(lengh-high), independent of high-low
def remove_index(self,low,high):
    if low==high:
        return 0
    while high<self.length:
        self.elements[low]=self.elements[high]
        low+=1
        high+=1
    self.length=low
    self.elements=self.elements[0:self.length]
    return high-low
#bind remove_index to vector
vector.remove_index=remove_index
    
# implement remove
# return element deleted
def remove(self,r):
    elem=self[r]
    self.remove_index(r,r+1)
    return elem
# bind to vector
vector.remove=remove

# implement deduplicate
# return old size - new size
def deduplicate(self):
    old_size=self.length
    # in case only 1 element
    if self.length==1:
        return 0
    r=1
    while r<self.length:
        if self.find(self.elements[r],0,r)<0:
            r=r+1
        else:
            self.remove(r)
    new_size=self.length
    return old_size-new_size
# bind to vector
vector.deduplicate=deduplicate

# implement traverse
# notice can't change elements in v
def traverse(self,func):
    for i in range(0,self.size()):
        func(self.elements[i])
# bind to vector
vector.traverse=traverse
    
#implement disordered
def disordered(self):
    n=0
    if self.length==1:
        return n
    for i in range(0,self.length-1):
        if self.elements[i]>self.elements[i+1]:
            n+=1
    return n
# bind to vector
vector.disordered=disordered

# implement uniquify
# assume v sorted
# Time complexity: O(n)
def uniquify(self):
    if self.length==1:
        return 0
    i=0
    j=1
    while j<self.length:
        if self.elements[i]!=self.elements[j]:
            self.elements[i+1]=self.elements[j]
            i=i+1
        j=j+1
    self.elements=self.elements[0:i+1]
    self.length=len(self.elements)
    return 1
# bind to vector
vector.uniquify=uniquify

#implement bin_search
# use binary search
# only applicable for ordered vector
# if search fails, return -1
def bin_search(self,e,low=None,high=None):
    if low==None and high==None:
        low=0
        high=self.length
    while low<high:
        mid=int((low+high)/2)
        if e<self.elements[mid]:
            high=mid
        elif e> self.elements[mid]:
            low=mid
        else:
            return mid
    # search failed
    return -1
# bind to vector
vector.bin_search=bin_search

    


#test code
v=vector([1,2,3,4,5])
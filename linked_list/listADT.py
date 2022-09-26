# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:33:02 2022

@author: lidon
"""

class list_node:
    def __init__(self,data=None,pred=None,succ=None):
        self.data=data
        self.pred=pred
        self.succ=succ
    def insert_as_pred(self,data):
        pass
    def insert_as_succ(self,data):
        pass
    
class linked_list:
    def __init__(self):
        header=list_node()
        trailer=list_node()
        header.succ=trailer
        header.pred=None
        trailer.pred=header
        trailer.succ=None
        self.size=0
        
    def __getitem__(self,key):
        pass
    
    # remove all nodes
    def clear(self):
        pass
    
    # copy n nodes starting from node
    def copy_nodes(self,node,n):
        pass
    
    # return size
    def size(self):
        pass
    
    # if it is empty (True if empty)
    def empty(self):
        return self.size<=0
    
    # return first node
    def first(self):
        return self.header.succ
    
    # return last node
    def last(self):
        return self.trailer.pred
    
    # return if node is valid (can be exposed to user)
    def valid(self,node):
        return node and (node!=self.header) and (node!=self.trailer)
    
    # return if ordered
    def disordered(self):
        pass
    
    # find data from linked list
    # assume disordered
    def find(self,data):
        pass
    
    # search data from linked list
    # assume ordered
    # if n and node are none, search from the whole list
    def search(self,data,n=None,node=None):
        pass
    
    # find the largest among node and its n-1 successors
    # if node and n None, search from whole list
    def select_max(self,node=None,n=None):
        pass
    
    def insert_as_first(self,data):
        pass
    
    def insert_as_last(self,data):
        pass
    
    # insert e as the successor of node
    def insert_succ(self,node,data):
        pass
    
    # insert e as the pred of node
    def insert_pred(self,node,data):
        pass
    
    # remove a node
    def remove(self,node):
        pass
    
    #sort
    def sort(self,node=None,n=None):
        pass
    
    #deduplicate
    def deduplicate(self):
        pass
    
    # uniquify
    def uniquify(self):
        pass
    
    # reverse
    def reverse(self):
        pass
    
    # traverse
    def traverse(self,func):
        pass
    
    
    
    
    
    
    
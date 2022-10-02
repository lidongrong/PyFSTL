# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:22:25 2022

@author: lidon
"""

from bin_node import*

class bin_tree:
    # size: tree size
    # root: tree root
    def __init__(self,size=0,root=None):
        self.size=size
        self.root=root
        
    # update the height of node x
    # return the updated height
    def update_height(self,x):
        x.height=1+max(stature(x.lc),stature(x.rc))
        return x.height
    
    # update height of x and its ancestors
    def update_height_above(self,x):
        while x:
            self.update_height(x)
            x=x.par
    
    # return size of the tree
    def size(self):
        return self.size
    
    # empty or not
    def empty(self):
        return not self.root
    
    # return root
    def root(self):
        return self.root
    
    # insert as root with data e
    # return root
    # WARNING: this will remove the full tree if there exists any!
    def insert_as_root(self,e):
        self.size=1
        self.root=bin_node(data=e)
        return self.root
    
    # insert e as the lc of node x
    def insert_as_lc(self,x,e):
        self.size=self.size+1
        x.insert_as_lc(e)
        self.update_height_above(x)
        return x.lc
    
    def insert_as_rc(self,x,e):
        self.size=self.size+1
        x.insert_as_rc(e)
        self.update_height_above(x)
        return x.rc
    
    # attach tree as left subtree of x
    # return position of x
    # WARNING: the original left subtree of x will be removed (if any)!
    def attach_as_lc(self,x,tree):
        x.lc=tree.root
        tree.root.par=x
        self.size=self.size+tree.size
        self.update_height_above(x)
        tree.root=None
        tree.size=0
        return x
    
    def attach_as_rc(self,x,tree):
        x.rc=tree.root
        tree.root.par=x
        self.size=self.size+tree.size
        self.update_height_above(x)
        tree.root=None
        tree.size=0
        return x
    
    # remove subtree with x as its root
    def remove(self,x):
        # if x is the root of the tree
        if isroot(x):
            self.size=0
            self.root=None
        else:
            if is_lc(x):
                x.par.lc=None
            else:
                x.par.rc=None
            self.update_height_above(x.par)
            x.par=None
                    
            
    
    # remove subtree with x as its root and transform it into an independent subtree
    def secede(self,x):
        # if x is the root, just return the tree itself
        if isroot(x):
            return self
        else:
            # cutoff pointer from the parents
            if is_lc(x):
                x.par.lc=None
            else:
                x.par.rc=None
            # renew heights
            self.update_height_above(x.par)
            # construct a new tree starting from x
            new_tree=bin_tree(size=x.size(),root=x)
            x.par=None
            
            # renew size of the old tree
            self.size=self.size-new_tree.size
            return new_tree
    
    def trav_level(self,func):
        pass
    
    def trav_pre(self,func):
        pass
    
    def trav_in(self,func):
        pass
    
    def trav_post(self,func):
        pass
    
    # reload <=
    def __le__(self,other):
        return self.root and  other.root and self.root<=other.root
    
    # reload ==
    def __eq__(self,other):
        return self.root and other.root and self.root==other.root
    
    
    
    
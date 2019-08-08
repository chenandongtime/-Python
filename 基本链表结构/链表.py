# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:37:11 2019

@author: Antime
"""

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedBag(object):
    """A linkbased bag implemention."""
    #constructor 
    def __init__(self,sourceCollection = None):
        """sets the initial state of self,which includes the contents 
        of sourceCollection"""
        self._items = None
        self._size = 0
        if sourceCollection :
            for item in sourceCollection:
                self.add(item)
        
    #Accessor methods
    def isEmpty(self):
        """Returns True if len(self)==0,or False otherwise."""
        return len(self)==0
    
    def __len__(self):
        """Returns the number of items in self"""
        return self._size
    def __str__(self):
        """Returns the string representation of self"""
        return "{"+",".join(map(str,self))+"}"
    
    def __iter__(self):
        """Supports iteration over a view of self"""
        cursor = self._items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next
        
    def __add__(self,other):
        """Returns a new bag containing the contents of 
        self and other"""
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result
        
    def __eq__(self,other):
        """Returns true if self equals other
        ,otherwise False"""
        if self is other :return True
        if type(self) != type(other) or \
            len(self) != len(other):
                return False
        for item in other:
            if not item in self:
                return False
        return True
            
            
    #mutator
    def clear(self):
        """Makes self become empty"""
        self._size = 0
        self._items = None
        
    def add(self,item):
        """Adds item to self"""
        self._items = Node(item,self._items)
        self._size +=1
        
    def remove(self,item):
        """Precondition:item is in self
        Raise:KeyError if item is not in self
        PostCondition:item is removed  from self."""
        probe = self._items
        trailer = None
        for items in self:
            if item == items:
                break
            trailer = probe
            probe = probe.next
            
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        #Decrment logical size
        self._size -=1

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("Expect 3:", len(b1))
    print("Expect the bag's string:", b1)
    print("Expect True:", 2013 in b1)
    print("Expect False:", 2012 in b1)
    print("Expect the items on separate lines:")
    for item in b1:
        print(item)
    b1.clear()
    print("Expect {}:", b1)
    b1.add(25)
    b1.remove(25)
    print("Expect {}:", b1)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Expect True:", b1 == b2)
    print("Expect False:", b1 is b2)
    print("Expect two of each item:", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Expect {}:", b1)
    print("Expect crash with KeyError:")
    b2.remove(61)

#test(ArrayBag)
test(LinkedBag)
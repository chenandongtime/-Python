# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:35:14 2019

@author: Antime
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, *fillValues):
        """Capacity is the static size of the array.
        fillValue is placed at each position.
        if there is more place need to fill use None"""
        self._items = list()
        for value in fillValues:
            self._items.append(int(value))
        for count in range(len(self._items)-1,capacity-1):
            self._items.append(None)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem

class ArrayBag(object):
    """An array based bag implentation"""
    #class variable
    DEFAULT_CAPACITY = 10
    
    #Constructor
    def __init__(self,sourceCollection = None):
        """Sets the initial state of self,which includes the 
        contens of sourceCollection,if it is presents."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection :
            for item in sourceCollection:
                self.add(item)
    
    #Accessor methods
    def isEmpty(self):
        """Returns true if len(self)==0,
        or False othersize"""
        return len(self==0)
    
    def __len__(self):
        """returns the numbers of items in self"""
        return self._size
    
    def __str__(self):
        """Returns the string representation of self"""
        return "{"+",".join(map(str,self))+"}"
    
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor +=1
    
    def __add__(self,other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self,other):
        """Returns True if self equals other,
        or False othersize."""
        if self is other:return True
        if type(self) != type(other) or \
            len(self) != len(other):
                return False
        for item in self:
            if item not in other:
                return False
        return True
    
    #Mutator methor    
    def clear(self):
        """Makes self becomes empty"""
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        
    def add(self,item):
        """Adds item to self."""
        #check array memmory here and increase it if necessary
        #Exercise
        self._items[len(self)] = item
        self._size +=1
        
    def remove(self,item):
        """Precondition:item is in self.
        Raise:keyError if item in not in self.
        Postcondition:item is removed from self"""
        if item not in self:
            raise KeyError(str(item)+"not in bag")
            #search for the index of the target item
            targetIndex = 0
            for targetItem in self:
                if targetItem == item:
                    break
                targetIndex +=1
            #shift items to the left of the target up by one position
            for i in range(targetIndex,len(self)-1):
                self._items[i] = self._items[i+1]
            #Decrement logical size
            self._size -=1
            #check array menmory here and decrease if if necessary

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

test(ArrayBag)
#test(LinkedBag)
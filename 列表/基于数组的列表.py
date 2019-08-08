# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:50:46 2019

@author: Antime
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

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

class AbstractCollection(object):
    """An abstract collection implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
    
class AbstractList(AbstractCollection):
    """Represent an abstract list"""
    def __init__(self,sourceCollection):
        """Maintain a count of modfications to the list."""
        self._modCount = 0
        AbstractCollection.__init__(self,sourceCollection)
    
    def getModCount(self):
        """Returns the count of modifications to the list"""
        return self._modCount
    
    def incModCount(self):
        """Increment the count of modifications to the list"""
        self._modCount +=1
        
    def index(self,item):
        """Precondition:item is in the list.
        Returns the position of item
        Raise: ValueError if the item is not in te list"""
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position +=1
        if position == len(self):
            raise ValueError(str(item)+" not in the list")
            
    def remove(self,item):
        """Precondition:item is in self.
        Raise:ValueError if item in not in self.
        Postcondition:item is removed from self"""
        position = self.index(item)
        self.pop(position)
        
    def add(self,item):
        """Adds the item to the end of the list"""
        self.insert(len(self),item)
        
    def append(self,item):
        """Adds the item to the end of the list"""
        self.add(item)

class ArrayList(AbstractList):
    """An array-based list implemention"""
    DEFAULT_CAPACITY = 10
    
    def __init__(self,sourceCollection = None):
        """Sets the initial state of self ,which
        includes the contents of sourceCollection,
        if it's present."""
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
        AbstractList.__init__(self,sourceCollection)
        
    def _resize(self,array,logicalSize):
        """if the array needs resizeing,resizes and returns the
        new array.Otherwise,returns the old array"""
        temp = None
        #if array is full
        if len(array) == logicalSize:
            temp = Array(2*len(array))
        #if array is wasting space
        elif logicalSize <= .25 * len(array) and \
             len(array) >= ArrayList.DEFAULT_CAPACITY:
                 temp = Array(round(.5 * len(array)))
        else:
            return array
        for i in range(logicalSize):
            temp[i] = array[i]
        return temp
    
    #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self"""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor +=1
        
    def __getitem__(self,i):
        """Precondition:0 < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List in dex out of range")
        return self._items[i]
    
    #Mutator methods
    def clear(self):
        """Makes self become empty"""
        self._size = 0
        self._items = Array(ArrayList.DEFAULT_CAPACITY)
    
    def __setitem__(self,i,item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises:IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("list out of range")
        self._items[i] = item
        
    def insert(self,i,item):
        """Insert the item at position i."""
        self._items = self._resize(self._items,len(self))
        if i < 0 or i >= len(self):
            raise IndexError("list out of range")
        elif i == -1 : i = len(self)
        elif i >= 0 and i <= len(self):
            for j in range(len(self),i,-1):
                self._items[j] = self._items[j-1]
        self._items[i] = item
        self._size +=1
        self.incModCount()
        
    def pop(self,i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self)-1
        if i < 0 or i >= len(self):
            raise IndexError("list index out of range")
        item = self._items[i]
        for j in range(i,len(self)-1):
            self._items[j] = self._items[j+1]
        self._size -=1
        self.incModCount()
        self._items = self._resize(self._items,len(self))
        return item
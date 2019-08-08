# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:47:15 2019

@author: Antime
"""
class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class TwoWayNode(Node):
    """Represents a doubly linked node."""

    def __init__(self, data = None, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous

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
        
class LinkedList(AbstractList):
    """A linked-based list implementation"""
    def __init__(self,sourceCollection = None):
        """Sets the inital state of self,which includes the
        contents of sourceCollection, if it's present"""
        #Uses a circular linked structure with a dummy header node
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        AbstractList.__init__(self,sourceCollection)
        
    #Helper method returns node at position i 
    def _getNode(self,i):
        """Helper method:returns a pointer to the node at position i ."""
        if i == len(self):
            return self._head
        elif i == len(self)-1:
            return self._head.previous
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -=1
        return probe
    
    def _checkIndex(self,i):
        """check wether i is out of  list range"""
        if i < 0 or i >= len(self):
            raise IndexError("list index out of range")
    
        #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield cursor.data
            cursor = cursor.next
        


    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        self._checkIndex()
        return self._getNode(i).data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head

        
    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError."""
        self._checkIndex()
        self._getNode(i).data = item
        

    def insert(self, i, item):
        """Inserts the item at position i."""
        if i < 0 : i = 0
        elif i > len(self): i = len(self)
        self._checkIndex()
        theNode = self._getNode(i)
        newNode = TwoWayNode(item,theNode.previous,theNode)
        theNode.previous.next = newNode
        theNode.previous =newNode
        self._size +=1
        self.incModCount()
        
    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        self._checkIndex()
        theNode = self._getNode(i)
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self._size -=1
        self.incModCount()
        return item

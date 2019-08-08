# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:43:35 2019

@author: Antime
"""
class Node(object):
    """Nodes for singly linked structures."""

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

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
    def __len__(self):
        """-> The number of items in self."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __add__(self, other):
        """Returns a new collection consisting of the
        items in self and other."""
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
    
class LinkedQueue(AbstractCollection):
    """An linked queue implemention"""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = None #存储队列头结构节点信息
        self._rear = None # 存储队列尾结构节点信息
        AbstractCollection.__init__(self,sourceCollection)

    # Accessor methods

    def __iter__(self):
        """Supports iteration over a view of self."""
        self._iter = self._front
        cursor = 0 
        while cursor < len(self):
            yield self._iter.data
            self._iter = self._iter.next
            cursor += 1

    def peek(self):
        """Returns the item at the top of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("the queue is empty")
        return self._front.data

    # Mutator methods
    def clear(self):
        """"clear the queue"""
        self._front = self._rear = None
        self._size = 0
        return print("the queue is cleared")
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        if self.isEmpty():
            self._front = self._rear = Node(item,None)
        else:
            self._rear.next = Node(item,None)
            self._rear = self._rear.next
        self._size +=1

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the top item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("the queue is empty")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -=1
        return oldItem
    
def test(queueType):
    # Test any implementation with same code
    q = queueType()
    print("Length:", len(q))
    print("Empty:", q.isEmpty())
    print("Add 1-10")
    for i in range(10):
        q.add(i + 1)
    print("Peeking:", q.peek())
    print("Items (front to rear):",  q)
    print("Length:", len(q))
    print("Empty:", q.isEmpty())
    theClone = queueType(q)
    print("Items in clone (front to rear):",  theClone)
    theClone.clear()
    print("Length of clone after clear:",  len(theClone))
    print("Pop 3 items:", end = " ")
    for count in range(3): print(q.pop(), end = " ")
    print("\nQueue: ", q)
    print("Adding 11 and 12:")
    for item in range(11, 13): q.add(item)
    print("Queue: ", q)    
    print("Popping items (front to rear): ", end="")
    while not q.isEmpty(): print(q.pop(), end=" ")
    print("\nLength:", len(q))
    print("Empty:", q.isEmpty())
    print("Create with 11 items:")
    q = queueType(range(1, 12))
    print("Items (front to rear):",  q)
    q = queueType(range(1, 11))
    print("Items (front to rear):",  q)
    print("Popping two items: ", q.pop(), q.pop(), q)
    print("Adding five items: ", end = "")
    for count in range(5):
        q.add(count)
    print(q)

#test(ArrayQueue)

test(LinkedQueue)
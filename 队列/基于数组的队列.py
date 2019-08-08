# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:39:58 2019

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

class ArrayQueue(AbstractCollection):
    """An Array queue implemention
    使用循环数组的方法实现，要点在于判断队头队尾的位置"""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        CAPACITY = 10 #队列基本容量
        self._items = Array(CAPACITY)
        self._front = 0 #出队列索引
        self._rear = 0 #进队列索引
        AbstractCollection.__init__(self,sourceCollection)

    # Accessor methods

    def __iter__(self):
        """Supports iteration over a view of self.
        如果出队列的索引指针大于进队列的索引，说明数组已经循环一周了，
        索引时需要先索引出队列索引到数组末尾，然后从数组开头继续索引
        到进队列位置；否则正常从出队列索引到进队列位置。"""
        if self._rear < self._front:
            for i in range(self._front,len(self._items)):
                yield self._items[i]
            for i in range(0,self._rear):
                yield self._items[i]  
        if self._rear > self._front:
            for i in range(self._front,self._rear):
                yield self._items[i]
        else:
            raise KeyError("the queue is empty")
            

    def peek(self):
        """Returns the item at the top of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise KeyError("the queue is empty")
        return self._items[self._front]

    # Mutator methods
    def clear(self):
        """"clear the queue"""
        self._front = self._rear = 0
        self._size = 0
        self._items = None
        return print("the queue is cleared")
    
    def add(self, item):
        """Inserts item at rear of the queue.
        首先判断队列是否要溢出，可能溢出则增加队列长度；
        否则判断进入指针是否到达队列末尾"""
        if len(self) > (len(self._items)-2):
            """如果队列即将满，则先拓展队列长度"""
            temp = Array(2*len(self._items))
            lenth = len(self)
            for i in range(0,lenth):
                temp[i] = self.pop()
            #恢复数据
            self._items = temp
            self._front = 0
            self._rear = lenth
            self._size = lenth
            
        if self._rear == (len(self._items)-1):
            """如果进入指针刚好在数组末尾，则需要将新的指针放到数组开头"""
            self._items[self._rear] = item
            self._rear = 0
            self._size +=1
            return None
        
        self._items[self._rear] = item
        self._rear +=1
        self._size +=1
        return None
            
    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the top item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("the queue is empty")
            
        tep = self._front #当前指针位置
        if self._front == (len(self._items)-1):
            """如果出指针在末尾则需要将指针下一个数值指向数组开头"""
            self._front = 0
        elif self._front < (len(self._items)-1):
            self._front +=1
        else:
            raise KeyError("it is out of the queue")
        self._size -=1
        return self._items[tep]
    
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

test(ArrayQueue)
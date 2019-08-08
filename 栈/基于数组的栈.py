# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:32:21 2019

@author: Antime
"""
class Abstractcollection():
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
        """-Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str, self)) + "]"


    def __add__(self, other):
        """Returns a new instance of the type of self
        containing the contents of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        #栈应该要求元素顺序也相同
        otherIter = iter(other)
        for item in self:
            #Return the next item from the iterator
            #Help on built-in function next in module builtins:
            if item != next(otherIter):
                return False
        return True
        
class AbstractStack(Abstractcollection):
    """An abstract stack implementation"""
    def __init__(self,sourceCollection=None):
        """sets the initial state of self,which includes the contents
        of sourcecollection, if it is present"""
        Abstractcollection.__init__(self,sourceCollection)
    
    def add(self,item):
        """"Adds item to self"""
        self.push(item)

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
        
class ArrayStack(AbstractStack):
    """An array stack implmention"""
    def __init__(self,sourceCollection=None):
        """初始化一个大小为10的数组作为栈的底层结构"""
        DEFAULT_CAPACITY = 10 #数组初始大小
        self._items = Array(DEFAULT_CAPACITY)
        AbstractStack.__init__(self,sourceCollection)
        
    def __iter__(self):
        """不可以使用数组的iter方法，因为数组大小不等于栈大小"""
        cursor = 0
        while cursor <= len(self)-1:
            yield self._items[cursor]
            cursor +=1
            
    def peek(self):
        """returns the item at the top o the stack.
        Precondition:the stack is not emoty.
        Raises:keyError if the stack is empty"""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        return self._items[len(self)-1]
    
    def clear(self):
        """clear the stack"""
        self._items = None
        self._size = 0 
        
    def push(self,item):
        """push a data to the stack.
        precondition:the stack is not empty.
        Raise:keyError.
        check if the data number is more than half of the capacity,
        expand the capacity double"""
        if self._items.__len__() == len(self):#判断栈是否满了
            raise KeyError
        
        #数组空间占用一半时，将数组空间扩大一倍
        #print("debug 1: " + str(self._items.__len__()))
        
        if len(self) > (self._items.__len__()*0.8):
            items_temp = Array(2*len(self))#数据中转站
            current_data_number = len(self)
            while len(self) > 0:
                #print("debug 2: "+str(len(self)))
                items_temp.__setitem__(len(self)-1,self.pop())
            self._items = Array(2*current_data_number)#容量加倍
            #print("debug 5 : "+ str(self._items.__len__()))
            #print(self._items)
            #self._size = 0 #回到初始态无data
            #数据回倒
            for i in range(0,current_data_number):
                #print('debug 4 '+str(items_temp[i]))
                self.push(items_temp[i])
        #常规流程push data
        #print("debug 3 "+str(len(self)))
        self._items[len(self)] = item
        self._size +=1
        """看一下数组添加data的方式是否正确"""
    
    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        # Resize the array here if necessary
        return oldItem
    
def test(stackType):
    # Test any implementation with same code
    s = stackType()
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    print("Push 1-15")
    for i in range(25):
        s.push((i + 1))
    print("Peeking:", s.peek())
    print("Items (bottom to top):",  s)
    print("Length:", len(s))
    print("Empty:", s.isEmpty())
    theClone = stackType(s)
    print("Items in clone (bottom to top):",  theClone)
    theClone.clear()

    print("Length of clone after clear:",  len(theClone))

    print("Push 26")
    s.push(26)
    print("Popping items (top to bottom): ", end="")
    while not s.isEmpty(): print(s.pop(), end=" ")
    print("\nLength:", len(s))
    print("Empty:", s.isEmpty())

test(ArrayStack)
#test(LinkedStack)
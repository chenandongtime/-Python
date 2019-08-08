# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:28:37 2019

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
    
class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedStack(AbstractStack):
    """A link-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = None
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        
        def visitNodes(node):
            """Adds items to tempList from tail to head."""
            if not node is None:
                visitNodes(node.next)
                tempList.append(node.data)
                
        tempList = list()                
        visitNodes(self._items)
        return iter(tempList)

    def peek(self):
        """
        Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        return self._items.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None

    def push(self, item):
        """Adds item to the top of the stack."""
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        """
        Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        data = self._items.data
        self._items = self._items.next
        self._size -= 1
        return data

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

#test(ArrayStack)
test(LinkedStack)
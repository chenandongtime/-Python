# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:25:05 2019

@author: Antime
"""

class BinHeap():
    def __init__(self):
        """给列表一个初始值0，
        使列表能够满足平衡二叉树左子节点
        为父节点的二倍的位置关系"""
        self._heapList = [0]
        self._currentSize = 0
    
    def perUp(self,i):
        """当插入的节点比父节点小时，
        节点位置和父节点互换"""
        while i // 2 > 0:
            if self._heapList[i] < self._heapList[i // 2]:
                tmp = self._heapList[i // 2 ]
                self._heapList[i // 2] = self._heapList[i]
                self._heapList[i] = tmp
            i = i // 2
    
    def insert(self,k):
        """插入新数据时，在列表末尾添加数据，
        在调用insert 方法"""
        self._heapList.append(k)
        self._currentSize = self._currentSize +1
        self.perUp(self._currentSize)
    
    def minChild(self,i):
        """确定当前节点的子节点的位置，左还是右"""
        if i*2 + 1 > self._currentSize:
            return i * 2
        else:
            if self._heapList[i*2] < self._heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    
    def percDown(self,i):
        """将父节点和子节点互换，
        通过minChild()函数确定子节点位置是2i还是2i+1
        """
        while (i * 2) <= self._currentSize:
            mc = self.minChild(i)
            if self._heapList[i] > self._heapList[mc]:
                tmp = self._heapList[i]
                self._heapList[i] = self._heapList[mc]
                self._heapList[mc] = tmp
            i = mc
            
    def delMin(self):
        """删除顶点后要回复堆的特点
        第一步把最后一个数放到堆顶
        第二步使用percDown()调整堆顶数据的位置"""
        retval = self._heapList[1]
        self._heapList[1] = self._heapList[self._currentSize]
        self._heapList.pop()
        self._currentSize -= 1
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist):
        """建立一个二叉堆"""
        i = len(alist) // 2
        self._currentSize = len(alist)
        self._heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -=1
bh = BinHeap()
bh.buildHeap([9,5,6,2,3])
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:22:06 2019

@author: Antime
"""
class TreeNode:
    """一个带有父节点信息的树结构类型"""
    def __init__(self,key,val,left=None,right=None,parent=None):
        """初始化信息，以字典的形式存储信息。
        self._key和self._payload分别作为Key值和Value
        key值可以用来排序"""
        self._key = key
        self._payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    
    def hasLeftChild(self):
        """返回左节点，无就返回None"""
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self):
        return not self.parent
    
    def isleaf(self):
        return not (self.rightChild or self.leftChild)
    
    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    
    def hasBothChildren(self):
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self,key,value,lc,rc):
        """更换一个节点的数据"""
        self._key = key
        self._payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    
    def __iter__(self):
        """迭代函数"""
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class BinarySearchTree:
    """基于字典存储类型的二叉搜索树"""
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def put(self,key,val):
        """在二叉树中插入一个数据，调用self._put辅助方法"""
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size +=1
        
    def _put(self,key,val,currentNode):
        """循环找到最小的位置"""
        if key < currentNode._key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
    
    def __setitem__(self,k,v):
        """字典形式的重载发符
        Dic[k]=v"""
        self.put(k,v)
    
    def get(self,key):
        """通过键值得到Value,调用辅助方法_get()"""
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res._payload
            else:
                return None
        else:
            return None
        
    def _get(self,key,currentNode):
        """利用循环的思想搜索，前序遍历方法"""
        if not currentNode:
            return None
        elif currentNode._key == key:
            return currentNode
        elif key < currentNode._key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
        
    def __getitem__(self,key):
        """重载操作符a=Dic[key]"""
        return self.get(key)
    
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
    
    def delete(self,key):
        """删除某个节点，并且移动其他位置节点到这个位置"""
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
            else:
                raise KeyError('Error , key not in tree')
        elif self.size ==1 and self.root.key == key:
            self.root = None
            self.size -=1
        else:
            raise KeyError('Error,key not in tree')
            
    def __delitem__(self,key):
        self.delete(key)
     
    def remove(self,currentNode):
        """移除一个节点，根据节点所在位置分类讨论如何操作"""
        self.size -=1 #只要发生remove操作，结构单元数量减一
        if currentNode.isleaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren:
            #当前节点有两个节点如何处理
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            #当前节点只有一个子节点
            if currentNode.hasLeftChild():
                #如果当前节点有左子节点
                if currentNode.isLeftChild():
                    #如果当前节点是左子节点
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    #如果当前节点是右子节点
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    #当前节点没有父节点
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                #如果当前节点只有右子节点
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)
    
    def findSuccessor(self):
        """找到当前节点最合适的继任者"""
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.finMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    #左子节点的最合适的继任者就是其父节点
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    def findMin(self):
        """找到当前分支的最小值，一直在左子树查找即可"""
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
print(mytree[6])
print(mytree[4])
mytree.delete(6)
print(mytree[6])
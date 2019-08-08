# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:57:05 2019

@author: Antime
"""

class Vertex:
    """建立一个节点类
    构造函数初始化id
    addNeighbor()用于添加一个顶点
    getConnections方法返回邻接表中的所有顶点
    getWeight()方法返回参数传递的边的权重
    """
    def __init__(self,key):
        """初始化id
        添加一个字典变量
        """
        self.id = key
        self.connectedTo = {}
        
    def addNeighbor(self,nbr,weight=0):
        """添加一个顶点及其边权重,nbr是一个Vertex对象"""
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        """返回字本节点id以及与其相连的节点id和权重"""
        return str(self.id)+' connectedTo ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        """返回所有与当前顶点相连的节点"""
        return self.connectedTo.keys()
    
    def getId(self):
        """"""
        return self.id
    
    def getWight(self,nbr):
        """返回当前两节点之间的权重"""
        return self.connectedTo[nbr]
    
class Graph():
    def __init__(self):
        """初始化一个空列表用来保存顶点，
        一个变量用来存储顶点数"""
        self.verlist = {} #顶点线性列表
        self.numVertices = 0 #记录当前定点数
    
    def addVertex(self,key):
        """再列表中增加一个新的顶点"""
        self.numVertices +=1
        newVertex = Vertex(key)
        self.verlist[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        """返回第n个顶点"""
        if n in self.verlist:
            return self.verList[n]
        else:
            raise KeyError("No elements of n" + str(n))
    
    def __contains__(self,n):
        """"""
        return n in self.verlist[n]
    
    def addEdge(self,f,t,cost=0):
        """添加两个顶点之间的连接，如果顶点不存在则先将顶点加入到顶点列表中"""
        if f not in self.verlist:
            self.addVertex(f)
        if t not in self.verlist:
            self.addVertex(t)
        self.verlist[f].addNeighbor(self.verlist[t],cost)
    
    def getVertices(self):
        """"""
        return self.verlist.keys()
    
    def __iter__(self):
        """写一个Graph类的迭代函数"""
        return iter(self.verlist.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
    
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
    for w in v.getConnections():
        print("(%s, %s,%s)" % (v.getId(),w.getId(),v.getWight(w)))
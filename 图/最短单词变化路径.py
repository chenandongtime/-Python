# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:58:06 2019

@author: Antime
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:20:04 2019

@author: Antime
"""
from linkedqueue import LinkedQueue

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
        设一个到顶点的距离distance
        一个前导变量
        一个颜色变量
        """
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.predecessor = None 
        self.color = 'white'
        
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
    
    def setDistance(self,Distance):
        self.distance = Distance
    
    def getDistance(self):
        return self.distance
    
    def setColor(self,color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def setPred(self,Vertex):
        self.predecessor = Vertex
    
    def getPred(self):
        return self.predecessor
    
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
            return self.verlist[n]
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

def buildGraph(wordFile):
    """通过桶方法来确定文本中所有单词之间的联系"""
    d = {} #桶字典
    g = Graph()
    wfile = open(wordFile,'r')
    #create buckets of words that differ by one letter
    for line in wfile:
        print("this is line :"+line)
        word = line[:-1]
        print()
        print("this is word :"+word)
        for i in range(len(word)):
            bucket = word[:i]+'_'+word[i+1:]
            print("this is bucket:"+bucket)
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    #add verties and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = LinkedQueue()
    vertQueue.add(start)
    while not vertQueue.isEmpty():
        currentVert = vertQueue.pop()
        for nbr in currentVert.getConnections():
            if (nbr.getColor()) == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.add(nbr)
        currentVert.setColor('black')
        
def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())
    
g = buildGraph('wordfile.txt')
print(g.getVertices())
bfs(g,g.getVertex('foul'))
traverse(g.getVertex('pope'))




    
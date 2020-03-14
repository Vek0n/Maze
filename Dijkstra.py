import numpy as np
from numpy import asarray
from PIL import Image
from MazeToGraph import MazeToGraph
import random
from Maze import Maze

class Dijkstra:
    def __init__(self, mazeObj, start, target):
        self.maze = mazeObj.getMaze()
        self.maze = np.asarray(self.maze)
        self.mazeSize = len(self.maze)
        self.m2g = MazeToGraph(mazeObj)
        self.graph = self.m2g.generateGraph()
        self.graphSize = len(self.graph)
        self.start = start
        self.target = target
        
    def minDist(self, dist, prev):
        minValue = np.inf
        for i in range(self.graphSize):
            if dist[i]<minValue and prev[i]==False:
                minValue = dist[i]
                minIndex = i
        return minIndex

    def findPath(self):
        dist = np.full(self.graphSize ,np.inf)
        prev = np.full(self.graphSize ,np.nan)
        visited = np.full(self.graphSize , False)
        dist[self.start] = 0

        for _ in range(self.graphSize):
            u = self.minDist(dist, visited)
            if u == self.target: return prev
            visited[u] = True
            for v in range(self.graphSize):
                if self.graph[u][v] > 0 and visited[v] == False and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    prev[v] = u
        return prev

    def getPath(self):
        prev = self.findPath()
        S = []
        u = self.target
        while np.isfinite(u):
            S.append(int(u))
            u = prev[int(u)]
        S.reverse()
        return S  
    
    def drawPath(self):
        dictOfNodes = self.m2g.getDictOfNodes()
        mazeMatrix = self.maze
        path = self.getPath()
        
        for p in path:
            tup = list(dictOfNodes.keys())[list(dictOfNodes.values()).index(p)]
            mazeMatrix[tup[0]][tup[1]] = 2
        
        emptyArray = np.zeros([self.mazeSize, self.mazeSize, 3], dtype=np.uint8)
        mazeArray = np.expand_dims(self.maze, axis=2)
        mazeArray = mazeArray + emptyArray
        
        for x in range(self.mazeSize):
            for y in range(self.mazeSize):
                if mazeMatrix[x][y] == 2:
                    mazeArray[x][y][0] = 0
                    
        img = Image.fromarray((mazeArray * 255).astype(np.uint8))
        img.save('path.png')
        
    
def main():
    m = Maze(50,50)
    start = 0
    finish = m.getNumOfNodes() - 1
    d = Dijkstra(m, start, finish)
    d.drawPath()
main()
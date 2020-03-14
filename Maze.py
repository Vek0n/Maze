import numpy as np
import random
from PIL import Image

class Maze:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.mazeMatrix = self.generateMaze()
    
    def getMaze(self):
        return self.mazeMatrix
    
    def getNodes(self):
        numOfNodes = 0
        dictOfNodes ={}
        for x in range(len(self.mazeMatrix)):
            for y in range(len(self.mazeMatrix)):
                if self.mazeMatrix[x][y] == 1:
                    dictOfNodes[x,y] = numOfNodes
                    numOfNodes += 1
                    
        return numOfNodes, dictOfNodes
    
    def getNumOfNodes(self):
        numOfNodes, dictOfNodes = self.getNodes()
        return numOfNodes
    
    def isInsideMaze(self, x, y):
        return x >= 0 and y >= 0 and x < self.h and y < self.w        
    
    def generateMaze(self):
        x = random.randint(0, self.w - 1)
        y = random.randint(0, self.h - 1)
        maze = np.zeros((self.w, self.h))
        maze[x][y] = 1
        path = [(x,y,0)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while(len(path) > 0):
            listOfPossibleMoves = []
            (x, y, d) = path[-1]
            for i in range(4):
                if self.isInsideMaze(x + dx[i], y + dy[i]):
                    if maze[x + dx[i]][y + dy[i]] == 0:
                        numOfFreePaths = 0
                        for j in range(4):
                            if self.isInsideMaze(x + dx[i] + dx[j], y + dy[i] + dy[j]):
                                if maze[x + dx[i] + dx[j]][y + dy[i] + dy[j]] == 1: numOfFreePaths += 1
                        if numOfFreePaths == 1:
                            listOfPossibleMoves.append(i)
                            
            lenOfList = len(listOfPossibleMoves)
            if lenOfList > 0:
                nextMove = listOfPossibleMoves[random.randint(0, lenOfList - 1)]
                x += dx[nextMove]
                y += dy[nextMove]
                maze[x][y] = 1
                path.append((x,y, nextMove))
            else:
                path.pop()

        return maze.astype(int)
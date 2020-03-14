from Maze import Maze
import numpy as np


class MazeToGraph:
    def __init__(self, mazeObj):
        self.maze = mazeObj.getMaze()
        self.numOfNodes, self.dictOfNodes = mazeObj.getNodes()
        
    def getDictOfNodes(self):
        return self.dictOfNodes
        
    def generateGraph(self):
        adjacencyMatrix = np.zeros((self.numOfNodes, self.numOfNodes))
        sizeOfMaze = len(self.maze)
        for x in range(sizeOfMaze):
            for y in range(sizeOfMaze):
                if self.maze[x][y] == 1:
                    if x == 0 and y == 0:
                        if self.maze[x+1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x+1,y]] = 1
                        if self.maze[x][y+1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y+1]] = 1
                    elif x == 0 and y == sizeOfMaze - 1:
                        if self.maze[x+1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x+1,y]] = 1
                        if self.maze[x][y-1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y-1]] = 1
                    elif x == sizeOfMaze-1 and y == sizeOfMaze-1:
                        if self.maze[x-1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x-1,y]] = 1
                        if self.maze[x][y-1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y-1]] = 1
                    elif x == sizeOfMaze-1 and y == 0:
                        if self.maze[x-1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x-1,y]] = 1
                        if self.maze[x][y+1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y+1]] = 1
                    elif x == 0:
                        if self.maze[x][y+1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y+1]] = 1
                        if self.maze[x][y-1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y-1]] = 1
                        if self.maze[x+1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x+1,y]] = 1
                    elif y == 0:
                        if self.maze[x+1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x+1,y]] = 1
                        if self.maze[x-1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x-1,y]] = 1
                        if self.maze[x][y+1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y+1]] = 1
                    elif x == sizeOfMaze - 1:
                        if self.maze[x][y+1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y+1]] = 1
                        if self.maze[x][y-1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y-1]] = 1
                        if self.maze[x-1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x-1,y]] = 1
                    elif y == sizeOfMaze - 1:
                        if self.maze[x+1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x+1,y]] = 1
                        if self.maze[x-1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x-1,y]] = 1
                        if self.maze[x][y-1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y-1]] = 1
                    else:
                        if self.maze[x+1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x+1,y]] = 1
                        if self.maze[x-1][y] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x-1,y]] = 1
                        if self.maze[x][y+1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y+1]] = 1
                        if self.maze[x][y-1] == 1:
                            adjacencyMatrix[self.dictOfNodes[x,y]][self.dictOfNodes[x,y-1]] = 1
                        
                                                
        return adjacencyMatrix
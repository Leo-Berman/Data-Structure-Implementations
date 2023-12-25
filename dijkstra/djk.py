# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:42:49 2023

@author: leo
"""

class node:
    
    # default constructor for nodes
    # holds node name and its connectios to other nodes
    def __init__(self,inname):
        self.name = inname
        self.connections = []
        
    # print node contents
    def printself(self):
        print(self.name)
        print(self.connections)
        
    # add connection to other node
    def addconnection(self,connection,dist):
        self.connections.append((connection,int(dist)))
    
    # getter for connections
    def retdist(self):
        return self.connections
        
class graph:
    
    # default constructor
    # this holds edges and vertices
    # it also makes sure that the nodes
    # are in order for dijkstra's algorithm
    def __init__(self,nodes):
        self.C = {}
        self.V = []
        for x in nodes:
            self.C[x.name] = x
            self.V.append(x.name)
        self.V.sort()
        
    # print graph contents
    def printself(self):
        for x in self.V:
            self.C[x].printself()
    
    # dijkstras implementation
    def djk(self,start,end):
        
        # create list for names and their distances to other nodes
        names = []
        dist = []
        
        # list of nodes that have already been checked
        checked = []
        
        # add all vertices to the unchecked nodes and
        # set their distances to infinitiy
        for x in self.V:
            names.append(x)
            if x == start:
                dist.append(0)
            else:
                dist.append(float('inf'))
                
        # set the start node
        index = dist.index(min(dist))
        
        # add the start node to the checked list
        checked.append(names[index])
        
        # set the work node to the start node
        work = self.C[names[index]]
        
        while True:
            # loop through all the current nodes connections
            for x in work.retdist():
                # if connections aren't checked, check them
                if x[0] not in checked:
                    if x[1]+dist[names.index(work.name)] < dist[names.index(x[0])]:
                        dist[names.index(x[0])] = x[1]+dist[names.index(work.name)]
            comp = float('inf')
            # check for minimum distances and set that node to the current work node
            for i in range(len(dist)):
                if dist[i] < comp:
                    if names[i] not in checked:
                        work = self.C[names[i]]
                        comp = dist[i]
            checked.append(work.name)
            
            # if all nodes are checked break out of the while loop
            if len(checked) == len(self.V):
                break
            
        # print the distance from start to end
        print(dist[names.index(end)])
        
        

def main():
    # open file
    with open("data.txt") as f:
        lines = f.readlines()
    
    lines = [x.replace("\n","").split(",") for x in lines]
    # load nodes in 
    nodes = []
    for i in range(len(lines)):
        nodes.append(node(lines[i][0]))
        z = [y.split() for y in lines[i][1::]]
        for x in z:
            nodes[i].addconnection(x[0],x[1])
    
    # create graph with nodes
    mygraph = graph(nodes)
    mygraph.djk("A","P")
        
main()
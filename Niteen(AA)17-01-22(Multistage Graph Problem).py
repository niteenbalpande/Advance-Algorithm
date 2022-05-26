# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:40:27 2021

@author: Niteens
"""
import sys 
def Source_to_Sink(MG):
#list for storing shortest distance from particular node to N-1 node  
    Distance=[0]*n
    for x in range(n-2, -1, -1): 
        Distance[x]=IN   
        for y in range(n):   
            if MG[x][y]==IN: 
                continue
            Distance[x]=min(MG[x][y]+Distance[y],Distance[x]) 
    return Distance[0] 
  
n=9
IN=sys.maxsize
  
#Adjacency matrix of graph
MG=[[IN, 9, 25, IN, IN, IN, IN, IN, IN],  
    [IN, IN, IN, 3, IN, 5, IN, IN, IN],  
    [IN, IN, IN, 2, 9, 3,IN, IN, IN],  
    [IN, IN, IN, IN, IN, IN, 7, 2, IN],  
    [IN, IN, IN, IN, IN, IN, 10, 2, IN], 
    [IN, IN, IN, IN, IN, IN, 5, 7, IN],  
    [IN, IN, IN, IN, IN, IN, IN, IN, 12],
    [IN, IN, IN, IN, IN, IN, IN, IN, 11]]  
D=Source_to_Sink(MG)  
print("Using Multistage graph, shortest distance is: ",D)

#O(n square)
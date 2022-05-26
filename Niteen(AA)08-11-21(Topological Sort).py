from collections import defaultdict
 
# Class to represent a graph
 
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)      # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order
 
 
# Driver Code
graph = Graph(7)
graph.addEdge(5,2);
graph.addEdge(5,6);
graph.addEdge(4,6);
graph.addEdge(4,1);
graph.addEdge(1,2);
graph.addEdge(3,4);

print("The Topological Sort Of The Graph Is:  ")
 
# Function Call
graph.topologicalSort()
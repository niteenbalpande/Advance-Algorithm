graph = {
  '1' : ['5','2','3'],
  '2' : ['1', '3','5','4','6'],
  '3' : ['1','2','4'],
  '4' : ['2','3'],
  '5' : ['1','2'],
  '6' : ['1']
}
visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
print("BFS")
bfs(visited, graph, '1') 
#o(v+e)
#Adjecency list- o(n squere)

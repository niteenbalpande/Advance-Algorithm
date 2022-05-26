graph = {
  '1' : ['5','2','3'],
  '2' : ['1', '3','5','4','6'],
  '3' : ['1','2','4'],
  '4' : ['2','3'],
  '5' : ['1','2'],
  '6' : ['1']
} 
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("DFS")
dfs(visited, graph, '6')
#o(v+e)
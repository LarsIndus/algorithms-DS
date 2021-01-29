# This is an implementation of DFS in graphs.
# Pass a graph as a dictionary, where the keys are nodes and the
# values are lists of neighbors (only the neighbors 'below' are needed).
# Note that this is not really a search, but merely a traversal through the whole graph
# in order to visualize the algorithm.
# The search itself can be added easily by checking whether the current node is the target.

def DFS(graph, start):
    # Two versions, using a dictionary and a list (same in complexity?)
    #visited = {node : False for node in graph.keys()}
    visited = set()
    DFS_helper(graph, start, visited)
        
def DFS_helper(graph, node, visited):
    #if visited[node]: return
    if node in visited: return
    print(node) # print out the order of traversal
    #visited[node] = True
    visited.add(node)
    for neighbor in graph[node]:
        DFS_helper(graph, neighbor, visited)
        
# Alternative in one function using a default value (bad practice?) -------------------------------------

def DFS_alternative(graph, node, visited = None):
    if visited is None: visited = set()
    if node in visited: return
    print(node) # print out the order of traversal
    visited.add(node)
    for neighbor in graph[node]:
        DFS_alternative(graph, neighbor, visited)
        
if __name__ == '__main__':       
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }
    
    print('First version:')
    DFS(graph, 'A')
    
    print('\n')
    
    print('Second version:')
    DFS_alternative(graph, 'A')
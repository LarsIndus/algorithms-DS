# This is an implementation of BFS in graphs.
# Pass a graph as a dictionary, where the keys are nodes and the
# values are lists of neighbors (only the neighbors 'below' are needed).
# Note that this is not really a search, but merely a traversal through the whole graph
# in order to visualize the algorithm.
# The search itself can be added easily by checking whether the current node is the target.

def BFS(graph, start):
    queue = [start]
    # Here, we could also use a dictionary instead of a set, see DFS script.
    # Using a list is not recommended, as checking the occurrence of an element is an O(n) operation
    # as opposed to O(1) for sets (and dictionaries?).
    visited = {start}
    print(start)
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(neighbor)
        
if __name__ == '__main__':       
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F'],
        'F' : []
    }
    
    BFS(graph, 'A')
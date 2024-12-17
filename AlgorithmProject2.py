import heapq

def prim(graph, start_vertex):
    
    visited = set()
    mst = []  
    min_heap = []
    
    
    heapq.heappush(min_heap, (0, start_vertex))
    
    while min_heap:
        
        weight, vertex = heapq.heappop(min_heap)
        
        if vertex in visited:
            continue
        
        
        visited.add(vertex)
        
        
        if weight != 0:
            mst.append((weight, vertex))
        
        
        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
    
    return mst


graph = {
    0: [(1, 1), (2, 4)],
    1: [(0, 1), (2, 2), (3, 5)],
    2: [(0, 4), (1, 2), (3, 1)],
    3: [(1, 5), (2, 1)]
}


mst = prim(graph, 0)


print("Edges in the Minimum Spanning Tree (MST):")
for edge in mst:
    print(edge)

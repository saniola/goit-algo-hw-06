# Implementation of the BFS algorithm to find paths
def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph[vertex]:
            if next_node not in path:
                if next_node == end:
                    paths.append(path + [next_node])
                else:
                    queue.append((next_node, path + [next_node]))
    return paths

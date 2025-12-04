from tree import create_the_tree
#BFS - Breadth First search
root = create_the_tree()
bfs_visited = set()
q = [root]
print("BFS VISITED:")
while q:
    node = q.pop(0)
    if node not in bfs_visited:
        bfs_visited.add(node.value)
        print(node.value)
        for child in node.children:
            if child not in bfs_visited:
               q.append(child)

#DFS - Depth First Search
print("\nDFS VISITED:")
stack = [root]
dfs_visited = set()
while stack:
    node = stack.pop()
    if node not in dfs_visited:
        dfs_visited.add(node.value)
        print(node.value)
        for child in node.children:
            if child not in dfs_visited:
                stack.append(child)
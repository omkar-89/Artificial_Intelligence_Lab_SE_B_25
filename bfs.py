# bfs program

from collections import deque 
def bfs(maze, start, end): 
# Directions: up, right, down, left 
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
queue = deque([start]) 
visited = set([start]) parent = {start: None} 
while queue: 
current = queue.popleft() 
if current == end: 
path = [] 
while current is not None: 
path.append(current) 
current = parent[current] 
path.reverse() 
return path 
for direction in directions: 
next_cell = (current[0] + direction[0], current[1] + direction[1]) 
if (0 <= next_cell[0] < len(maze) and 
0 <= next_cell[1] < len(maze[0]) and 
maze[next_cell[0]][next_cell[1]] != '#' and 
next_cell not in visited): 
queue.append(next_cell) 
visited.add(next_cell) 
parent[next_cell] = current 
return None 
# Example maze 
maze = [ 
['S', '.', '.', '#', '.', '.', '.'], 
['.', '#', '.', '#', '.', '#', '.'], 
['.', '#', '.', '.', '.', '.', '.'], 
['.', '.', '#', '#', '#', '.', '.'], 
['.', '#', '.', '.', '.', '#', '.'], 
['.', '#', '#', '#', '.', '#', '.'], 
['.', '.', '.', '.', '.', '.', 'E'], 
] 
start = (0, 0) # Starting position 
end = (6, 6) # Ending position (exit)
# Run BFS to find the path 
path = bfs(maze, start, end) 
if path: 
print("Path found:", path) 
else: 
print("No path exists.") 

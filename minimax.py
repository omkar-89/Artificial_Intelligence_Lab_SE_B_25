def minimax(depth, index, maximizingPlayer, values):
    # Base case: if depth is 0 or we reached beyond leaf nodes
    if depth == 0 or index >= len(values):
        return values[index]

    if maximizingPlayer:
        best = float('-inf')
        # Left and Right child (binary tree assumption)
        best = max(best, minimax(depth-1, index*2, False, values))
        best = max(best, minimax(depth-1, index*2 + 1, False, values))
        return best
    else:
        best = float('inf')
        best = min(best, minimax(depth-1, index*2, True, values))
        best = min(best, minimax(depth-1, index*2 + 1, True, values))
        return best


# Example values at the leaf nodes
values = [3, 5, 6, 9, 1, 2, 0, -1]  
depth = 3   # tree height
result = minimax(depth, 0, True, values)

print("Optimal value (using Minimax):", result)

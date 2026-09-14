class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        next_dir = {"right": "down", "down": "left", "left": "up", "up": "right"}
        vectors = {"right": (0, 1), "left": (0, -1),
                   "down": (1, 0), "up": (-1, 0)}

        rows = len(matrix)
        cols = len(matrix[0])

        spiral = []
        visited = []
        row, col = 0, 0
        direction = "right"
        for i in range(rows * cols):
            spiral.append(matrix[row][col])
            visited.append((row, col))

            if i == rows * cols - 1:
                break

            next_row = row + vectors[direction][0]
            next_col = col + vectors[direction][1]

            while (not (0 <= next_row < rows and 0 <= next_col < cols) or
                    (next_row, next_col) in visited):
                direction = next_dir[direction]
                next_row = row + vectors[direction][0]
                next_col = col + vectors[direction][1]

            row, col = next_row, next_col

        return spiral
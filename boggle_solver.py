"""
NAME: SAMIR ACHARYA
SID: @03058028
"""

class Boggle:
    def __init__(self, grid, dictionary):
        """Constructor to initialize the grid and dictionary."""
        self.grid = grid
        self.dictionary = set(dictionary)  # Convert the dictionary to a set for fast lookup
        self.rows = len(grid)              # Number of rows in the grid
        self.cols = len(grid[0]) if grid else 0  # Number of columns in the grid
        self.result = set()                # Set to store found words

    def setGrid(self, grid):
        """Setter method to update the grid."""
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

    def setDictionary(self, dictionary):
        """Setter method to update the dictionary."""
        self.dictionary = set(dictionary)

    def is_valid(self, x, y, visited):
        """Check if the cell (x, y) is valid and not visited."""
        return 0 <= x < self.rows and 0 <= y < self.cols and not visited[x][y]

    def dfs(self, x, y, path, visited):
        """Perform depth-first search from the cell (x, y) to find valid words."""
        if path in self.dictionary:
            self.result.add(path)  # Add to result if the path forms a valid word

        # If the dictionary is empty, avoid calling max() to prevent errors
        if self.dictionary and len(path) > max(map(len, self.dictionary)):
            return

        # Define all 8 possible directions (including diagonals)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Mark the current cell as visited
        visited[x][y] = True

        # Explore all 8 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny, visited):
                # Recurse to explore the next cell
                self.dfs(nx, ny, path + self.grid[nx][ny], visited)

        # Unmark the current cell to allow other paths to use it
        visited[x][y] = False

    def getSolution(self):
        """Return the list of all valid words found in the grid."""
        # Handle edge case: if dictionary is empty, return an empty list
        if not self.dictionary:
            return []

        # Initialize the visited matrix
        visited = [[False] * self.cols for _ in range(self.rows)]

        # Start DFS from every cell in the grid
        for x in range(self.rows):
            for y in range(self.cols):
                self.dfs(x, y, self.grid[x][y], visited)

        # Return the list of all found words
        return list(self.result)

def main():
    """Main function to create a Boggle game and print the solution."""
    grid = [['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'], 
            ['I', 'J', 'K', 'L'], 
            ['A', 'B', 'C', 'D']]

    dictionary = ['ABEF', 'AFJIEB', 'DGKD', 'DGKA']

    # Create an instance of Boggle
    mygame = Boggle(grid, dictionary)

    # Print the solution (valid words found in the grid)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()

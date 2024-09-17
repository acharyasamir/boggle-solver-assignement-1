'''
      NAME : SAMIR ACHARYA
      SID : @03058028
'''

class Boggle:
  def __init__(self, grid, dictionary):
    # Setup the boggle board and dictionary
    self.grid = grid
    self.dictionary = set(dictionary)  # Store the dictionary in a set for quicker lookup
    self.rows = len(grid)              # Get the number of rows in the grid
    self.cols = len(grid[0])           # Get the number of columns in the grid
    self.result = set()                # Set to store discovered words

  def is_valid(self, x, y, visited):
    # Ensure that the position (x, y) is within bounds and not visited yet
    return 0 <= x < self.rows and 0 <= y < self.cols and not visited[x][y]

  def dfs(self, x, y, path, visited):
    # Depth-first search to explore all potential words starting from (x, y)
    if path in self.dictionary:
      self.result.add(path)  # Add to result if the word is found in the dictionary

    # Terminate early if the current path is longer than the longest word in the dictionary
    if len(path) > max(map(len, self.dictionary)):
      return

    # Define all 8 possible moves (left, right, diagonal, etc.)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    # Mark the current cell as visited
    visited[x][y] = True

    # Explore all neighboring cells
    for dx, dy in directions:
      nx, ny = x + dx, y + dy  # Calculate new coordinates
      if self.is_valid(nx, ny, visited):
        # Continue the search from the neighboring cell and append the new character to the path
        self.dfs(nx, ny, path + self.grid[nx][ny], visited)
    
    # Unmark the current cell so it can be used in other paths
    visited[x][y] = False

  def solution(self):
    # Create a visited matrix to track which cells have been explored
    visited = [[False] * self.cols for _ in range(self.rows)]

    # Start a DFS search from every cell in the grid
    for x in range(self.rows):
      for y in range(self.cols):
        # Begin the search from the cell at (x, y)
        self.dfs(x, y, self.grid[x][y], visited)

    # Return the list of all valid words found in the grid
    return list(self.result)

def main():
  # Define the boggle board and the list of valid words
  grid = [['A', 'B', 'C', 'D'],
          ['E', 'F', 'G', 'H'], 
          ['I', 'J', 'K', 'L'], 
          ['A', 'B', 'C', 'D']]

  dictionary = ['ABEF', 'AFJIEB', 'DGKD', 'DGKA']

  # Create an instance of the Boggle game and find all valid words in the grid
  mygame = Boggle(grid, dictionary)
  
  # Display the list of words that were found
  print(mygame.solution())

# Ensure the main function runs only when the script is executed directly
if __name__ == "__main__":
  main()

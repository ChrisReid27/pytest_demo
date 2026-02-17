# Christopher Reid SID: 003122717

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = None
        self.dictionary = None
        self.words = set()
        self.prefixes = set()
        self.solutions = set()

        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        if not grid or not isinstance(grid, list):
            self.grid = None
            return

        rows = len(grid)
        # Use the length of the first row to define the expected width
        cols = len(grid[0]) if rows > 0 and isinstance(grid[0], list) else 0

        normalized_grid = []
        for row in grid:
            # Check if every row matches the width of the first row
            if not isinstance(row, list) or len(row) != cols:
                self.grid = None
                return

            new_row = []
            for cell in row:
                if not isinstance(cell, str):
                    self.grid = None
                    return
                new_row.append(cell.lower())
            normalized_grid.append(new_row)

        self.grid = normalized_grid

    def setDictionary(self, dictionary):
        if not dictionary or not isinstance(dictionary, list):
            self.dictionary = None
            return

        self.dictionary = []
        self.words = set()
        self.prefixes = set()

        for word in dictionary:
            if isinstance(word, str) and len(word) >= 3:
                clean_word = word.lower()
                self.dictionary.append(clean_word)
                self.words.add(clean_word)

                # Correctly populate prefixes for the search tree
                for i in range(1, len(clean_word) + 1):
                    self.prefixes.add(clean_word[:i])

    def getSolution(self):
        if not self.grid or not self.dictionary:
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])
        self.solutions = set()
        
        # Create a visited matrix that matches the rectangular dimensions
        visited = [[False] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, visited, "")

        return sorted(list(self.solutions))
    
    def _dfs(self, r, c, visited, current):
        rows = len(self.grid)
        cols = len(self.grid[0])

        # 1. Correct boundary check for rectangular grids
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        
        if visited[r][c]:
            return

        new_word = current + self.grid[r][c]

        # 2. Prefix pruning
        if new_word not in self.prefixes:
            return

        visited[r][c] = True
        
        # 3. Success check
        if new_word in self.words:
            self.solutions.add(new_word)

        # 4. Explore all 8 neighbors
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:
                    self._dfs(r + dr, c + dc, visited, new_word)

        # Backtrack
        visited[r][c] = False


def main():
    grid = [
      ["T", "W", "Y", "R"], 
      ["E", "N", "P", "H"],
      ["G", "St", "Qu", "R"],
      ["O", "N", "T", "A"]
      ]
    
    dictionary = [
      "art", "ego", "gent", "get", 
      "net", "new", "newt", "prat", 
      "pry", "qua", "quart", "rat", 
      "tar", "tarp", "ten", "went", 
      "wet", "stont", "not", "quar", 
      "nest", "west", "test", "gest",  
      ]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())



if __name__ == "__main__":
    main()
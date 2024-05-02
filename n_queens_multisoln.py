class NQueensBranchBound:
    def __init__(self, n=8):
        self.n = n  # Board size (n x n)
        self.board = [-1] * n  # Initialize board where board[col] = row of queen in column col
        self.row_used = [False] * n  # Track if row is already occupied
        self.diagonal1_used = [False] * (2 * n - 1)  # Track main diagonals (/)
        self.diagonal2_used = [False] * (2 * n - 1)  # Track anti-diagonals (\)
        self.solutions = []  # List to store all solutions

    def is_safe(self, row, col):
        """ Check if placing a queen at (row, col) is safe """
        return not self.row_used[row] and not self.diagonal1_used[row + col] and not self.diagonal2_used[row - col + self.n - 1]

    def place_queen(self, col):
        """ Place a queen in the specified column using backtracking """
        if col == self.n:
            # Found a valid solution
            self.solutions.append(self.board[:])
            return True
        
        for row in range(self.n):
            if self.is_safe(row, col):
                # Place the queen
                self.board[col] = row
                self.row_used[row] = True
                self.diagonal1_used[row + col] = True
                self.diagonal2_used[row - col + self.n - 1] = True
                
                # Recursively place queens in next columns
                self.place_queen(col + 1)
                
                # Backtrack
                self.board[col] = -1
                self.row_used[row] = False
                self.diagonal1_used[row + col] = False
                self.diagonal2_used[row - col + self.n - 1] = False

    def solve(self):
        """ Solve the N-Queens problem using branch and bound """
        self.place_queen(0)
        return self.solutions

    def print_solution(self, solution):
        """ Print the N-Queens solution """
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if solution[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()

# Main function to solve and print N-Queens solutions
def main():
    n_queens = NQueensBranchBound(8)
    solutions = n_queens.solve()

    print(f"Total solutions for {n_queens.n}-Queens on an {n_queens.n}x{n_queens.n} board: {len(solutions)}\n")

    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        n_queens.print_solution(solution)

if __name__ == "__main__":
    main()

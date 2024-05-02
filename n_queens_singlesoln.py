class NQueensBranchBound:
    def __init__(self, n=8):
        self.n = n  # Board size (n x n)
        self.board = [-1] * n  # Initialize board where board[col] = row of queen in column col
        self.row_used = [False] * n  # Track if row is already occupied
        self.diagonal1_used = [False] * (2 * n - 1)  # Track main diagonals (/)
        self.diagonal2_used = [False] * (2 * n - 1)  # Track anti-diagonals (\)
        self.solution = None  # Store the final solution

    def is_safe(self, row, col):
        """ Check if placing a queen at (row, col) is safe """
        return not self.row_used[row] and not self.diagonal1_used[row + col] and not self.diagonal2_used[row - col + self.n - 1]

    def place_queen(self, col):
        """ Place a queen in the specified column using backtracking """
        if col == self.n:
            # All queens placed successfully, store the solution
            self.solution = self.board[:]
            return True
        
        for row in range(self.n):
            if self.is_safe(row, col):
                # Place the queen
                self.board[col] = row
                self.row_used[row] = True
                self.diagonal1_used[row + col] = True
                self.diagonal2_used[row - col + self.n - 1] = True
                
                # Recursively place queens in next columns
                if self.place_queen(col + 1):
                    return True
                
                # Backtrack
                self.board[col] = -1
                self.row_used[row] = False
                self.diagonal1_used[row + col] = False
                self.diagonal2_used[row - col + self.n - 1] = False
        
        return False

    def solve(self):
        """ Solve the N-Queens problem using branch and bound """
        self.place_queen(0)
        return self.solution

    def print_solution(self):
        """ Print the final N-Queens solution """
        if self.solution is None:
            print(f"No solution found for {self.n}-Queens problem.")
        else:
            for row in range(self.n):
                line = ""
                for col in range(self.n):
                    if self.solution[col] == row:
                        line += "Q "
                    else:
                        line += ". "
                print(line)
            print()

# Main function to solve and print the final N-Queens solution
def main():
    n_queens = NQueensBranchBound(8)
    final_solution = n_queens.solve()

    print(f"Final solution for {n_queens.n}-Queens on an {n_queens.n}x{n_queens.n} board:\n")
    n_queens.print_solution()

if __name__ == "__main__":
    main()

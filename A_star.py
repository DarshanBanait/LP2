import heapq

class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None, depth=0):
        self.puzzle = puzzle  # Current state of the puzzle (2D list representing the puzzle configuration)
        self.parent = parent  # Parent state (previous puzzle state)
        self.move = move      # Move that led to this state from the parent state
        self.depth = depth    # Depth of this state in the search tree

        # Calculate the cost (f-score) for A* based on current state and heuristic
        self.cost = self.depth + self.calculate_heuristic()

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        # Convert the puzzle state to a hashable representation (tuple of tuples)
        return hash(tuple(map(tuple, self.puzzle)))

    def find_blank(self):
        # Find the position of the blank (zero) tile in the puzzle
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

    def move_blank(self, direction):
        # Move the blank tile in the specified direction (up, down, left, right)
        blank_row, blank_col = self.find_blank()
        new_row, new_col = blank_row, blank_col

        if direction == 'up':
            new_row -= 1
        elif direction == 'down':
            new_row += 1
        elif direction == 'left':
            new_col -= 1
        elif direction == 'right':
            new_col += 1

        # Perform the move if it's within bounds
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_puzzle = [row[:] for row in self.puzzle]
            new_puzzle[blank_row][blank_col], new_puzzle[new_row][new_col] = \
                new_puzzle[new_row][new_col], new_puzzle[blank_row][blank_col]
            return new_puzzle
        else:
            return None

    def get_possible_moves(self):
        # Return all valid moves from the current state
        possible_moves = []
        for direction in ['up', 'down', 'left', 'right']:
            new_puzzle = self.move_blank(direction)
            if new_puzzle:
                possible_moves.append((new_puzzle, direction))
        return possible_moves

    def is_goal(self, goal_state):
        return self.puzzle == goal_state

    def calculate_heuristic(self):
        # Manhattan distance heuristic for the 8-puzzle
        total_distance = 0
        goal_positions = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                          4: (1, 0), 5: (1, 1), 6: (1, 2),
                          7: (2, 0), 8: (2, 1), 0: (2, 2)}

        for i in range(3):
            for j in range(3):
                tile = self.puzzle[i][j]
                if tile != 0:
                    goal_row, goal_col = goal_positions[tile]
                    total_distance += abs(i - goal_row) + abs(j - goal_col)

        return total_distance

def a_star_search(initial_state, goal_state):
    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal(goal_state):
            path = []
            while current_state:
                path.append((current_state.puzzle, current_state.move))
                current_state = current_state.parent
            return path[::-1]

        closed_set.add(current_state)

        for (new_puzzle, move) in current_state.get_possible_moves():
            new_state = PuzzleState(new_puzzle, current_state, move, current_state.depth + 1)

            if new_state in closed_set:
                continue

            heapq.heappush(open_set, new_state)

    return None  # No solution found

def print_solution(path):
    if not path:
        print("No solution found.")
    else:
        print("Solution found! Steps:")
        for i, (state, move) in enumerate(path):
            print(f"Step {i + 1}: Move {move}")
            print_puzzle(state)

def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(tile) for tile in row))
    print()

def get_puzzle_from_user():
    puzzle = []
    print("Enter the puzzle configuration (3x3 grid, use numbers 0-8 where 0 represents the blank space):")
    for i in range(3):
        row = input(f"Enter row {i + 1}: ").strip().split()
        row = [int(tile) for tile in row]
        puzzle.append(row)
    return puzzle

def main():
    # Get initial and goal puzzle configurations from user
    print("Enter the initial puzzle configuration:")
    initial_puzzle = get_puzzle_from_user()

    print("Enter the goal puzzle configuration:")
    goal_puzzle = get_puzzle_from_user()

    # Create initial state and goal state objects
    initial_state = PuzzleState(initial_puzzle)
    goal_state = goal_puzzle

    # Perform A* search
    path = a_star_search(initial_state, goal_state)

    # Print the solution path
    print_solution(path)

if __name__ == "__main__":
    main()

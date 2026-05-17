import random
import time
import tracemalloc


class HillClimbingNQueens:

    def __init__(self, n):
        self.n = n

        # Random initial board
        self.board = [random.randint(0, n - 1) for _ in range(n)]

    # Count conflicts for a queen at (row, col)
    def conflicts(self, row, col):

        count = 0

        for r in range(self.n):

            if r == row:
                continue

            c = self.board[r]

            # Same column or diagonal
            if c == col or abs(c - col) == abs(r - row):
                count += 1

        return count

    # Total conflicts on board
    def total_conflicts(self):

        total = 0

        for row in range(self.n):
            total += self.conflicts(row, self.board[row])

        return total // 2

    # Hill Climbing algorithm
    def solve(self, max_steps=1000):

        for step in range(max_steps):

            total = self.total_conflicts()

            # Solution found
            if total == 0:
                return True, step

            conflicted_rows = []

            # Find queens with conflicts
            for row in range(self.n):

                if self.conflicts(row, self.board[row]) > 0:
                    conflicted_rows.append(row)

            if not conflicted_rows:
                return True, step

            # Randomly pick conflicted queen
            row = random.choice(conflicted_rows)

            best_col = self.board[row]
            min_conflict = self.conflicts(row, best_col)

            # Instead of checking all columns,
            # sample only a few random columns
            sampled_cols = random.sample(
                range(self.n),
                min(20, self.n)
            )

            for col in sampled_cols:

                conflict = self.conflicts(row, col)

                if conflict < min_conflict:
                    min_conflict = conflict
                    best_col = col

            # Move queen
            self.board[row] = best_col

        return False, max_steps


def run_hill_climbing(n):

    tracemalloc.start()

    start = time.time()

    solver = HillClimbingNQueens(n)

    solved, steps = solver.solve()

    end = time.time()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "N": n,
        "Solved": solved,
        "Steps": steps,
        "Time": round(end - start, 4),
        "Memory_MB": round(peak / 1024 / 1024, 4)
    }


if __name__ == "__main__":

    test_sizes = [10, 30, 50, 100, 200, 500]

    for n in test_sizes:

        print(f"\nRunning Hill Climbing for N = {n}")

        result = run_hill_climbing(n)

        print(result)
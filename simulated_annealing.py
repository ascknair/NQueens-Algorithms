import random
import math
import time
import tracemalloc


class SimulatedAnnealingNQueens:

    def __init__(self, n):

        self.n = n

        # Random board
        self.board = [random.randint(0, n - 1) for _ in range(n)]

    # Total conflicts
    def calculate_conflicts(self, board):

        conflicts = 0

        for i in range(self.n):

            for j in range(i + 1, self.n):

                if board[i] == board[j] or \
                   abs(board[i] - board[j]) == abs(i - j):

                    conflicts += 1

        return conflicts

    # Generate neighboring state
    def random_neighbor(self):

        neighbor = self.board[:]

        row = random.randint(0, self.n - 1)

        col = random.randint(0, self.n - 1)

        neighbor[row] = col

        return neighbor

    # Simulated Annealing algorithm
    def solve(self,
              initial_temp=100,
              cooling_rate=0.995,
              min_temp=0.001,
              max_iterations=100000):

        temperature = initial_temp

        current_board = self.board[:]

        current_conflicts = self.calculate_conflicts(current_board)

        iteration = 0

        while temperature > min_temp and iteration < max_iterations:

            if current_conflicts == 0:
                self.board = current_board
                return True, iteration

            neighbor = self.random_neighbor()

            neighbor_conflicts = self.calculate_conflicts(neighbor)

            delta = neighbor_conflicts - current_conflicts

            # Accept better solution
            if delta < 0:

                current_board = neighbor
                current_conflicts = neighbor_conflicts

            else:

                probability = math.exp(-delta / temperature)

                if random.random() < probability:

                    current_board = neighbor
                    current_conflicts = neighbor_conflicts

            # Cooling
            temperature *= cooling_rate

            iteration += 1

        self.board = current_board

        return current_conflicts == 0, iteration


def run_simulated_annealing(n):

    tracemalloc.start()

    start = time.time()

    solver = SimulatedAnnealingNQueens(n)

    solved, iterations = solver.solve()

    end = time.time()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "N": n,
        "Solved": solved,
        "Iterations": iterations,
        "Time": round(end - start, 4),
        "Memory_MB": round(peak / 1024 / 1024, 4)
    }


if __name__ == "__main__":

    test_sizes = [10, 30, 50, 100, 200, 500]

    for n in test_sizes:

        print(f"\nRunning Simulated Annealing for N = {n}")

        result = run_simulated_annealing(n)

        print(result)
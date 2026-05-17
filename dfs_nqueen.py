import time
import tracemalloc
import threading


class NQueensDFS:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solution_found = False

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def solve(self, row=0):

        if self.solution_found:
            return True

        if row == self.n:
            self.solution_found = True
            return True

        for col in range(self.n):

            if self.is_safe(row, col):

                self.board[row] = col

                if self.solve(row + 1):
                    return True

                self.board[row] = -1

        return False


def dfs_worker(solver):
    solver.solve()


def run_dfs(n, timeout_seconds=10):

    tracemalloc.start()

    start_time = time.time()

    solver = NQueensDFS(n)

    thread = threading.Thread(target=dfs_worker, args=(solver,))
    thread.start()

    thread.join(timeout_seconds)

    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_usage = peak / 1024 / 1024

    if thread.is_alive():
        status = "Timeout"
    elif solver.solution_found:
        status = "Solved"
    else:
        status = "No Solution"

    return {
        "N": n,
        "Status": status,
        "Time": round(execution_time, 4),
        "Memory_MB": round(memory_usage, 4)
    }


if __name__ == "__main__":

    test_sizes = [10, 30, 50]

    for n in test_sizes:

        print(f"\nRunning DFS for N = {n}")

        result = run_dfs(n, timeout_seconds=10)

        print(result)
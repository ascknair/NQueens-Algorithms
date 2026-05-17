import random
import time
import tracemalloc


class GeneticNQueens:

    def __init__(self,
                 n,
                 population_size=30,
                 mutation_rate=0.2,
                 generations=200):

        self.n = n
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations

        self.population = [
            self.random_board()
            for _ in range(population_size)
        ]

    # Random board
    def random_board(self):

        return [random.randint(0, self.n - 1)
                for _ in range(self.n)]

    # Conflict count
    def conflicts(self, board):

        count = 0

        for i in range(self.n):

            for j in range(i + 1, self.n):

                if board[i] == board[j] or \
                   abs(board[i] - board[j]) == abs(i - j):

                    count += 1

        return count

    # Fitness
    def fitness(self, board):

        return -self.conflicts(board)

    # Tournament selection
    def select_parent(self):

        tournament = random.sample(self.population, 3)

        tournament.sort(
            key=lambda x: self.fitness(x),
            reverse=True
        )

        return tournament[0]

    # Crossover
    def crossover(self, p1, p2):

        point = random.randint(0, self.n - 1)

        child = p1[:point] + p2[point:]

        return child

    # Mutation
    def mutate(self, board):

        if random.random() < self.mutation_rate:

            row = random.randint(0, self.n - 1)

            board[row] = random.randint(0, self.n - 1)

        return board

    # Main loop
    def solve(self):

        best_conflict = float('inf')

        for generation in range(self.generations):

            # Evaluate best solution
            best = min(
                self.population,
                key=self.conflicts
            )

            current_conflict = self.conflicts(best)

            if current_conflict < best_conflict:
                best_conflict = current_conflict

            # Perfect solution
            if current_conflict == 0:
                return True, generation

            new_population = []

            while len(new_population) < self.population_size:

                p1 = self.select_parent()
                p2 = self.select_parent()

                child = self.crossover(p1, p2)

                child = self.mutate(child)

                new_population.append(child)

            self.population = new_population

        return False, self.generations


def run_genetic_algorithm(n):

    tracemalloc.start()

    start = time.time()

    solver = GeneticNQueens(n)

    solved, generations = solver.solve()

    end = time.time()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return {
        "N": n,
        "Solved": solved,
        "Generations": generations,
        "Time": round(end - start, 4),
        "Memory_MB": round(peak / 1024 / 1024, 4)
    }


if __name__ == "__main__":

    test_sizes = [10, 30, 50, 100, 200, 500]

    for n in test_sizes:

        print(f"\nRunning Genetic Algorithm for N = {n}")

        result = run_genetic_algorithm(n)

        print(result)
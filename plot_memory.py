import matplotlib.pyplot as plt

n_values = [10, 30, 50, 100, 200]

dfs_mem = [0.0039, 0.0044, 0.0052, 0, 0]

hill_mem = [0.0047, 0.0018, 0.0022, 0.0050, 0.0065]

sa_mem = [0.0012, 0.0034, 0.0052, 0.0044, 0.0081]

ga_mem = [0.0106, 0.0153, 0.0245, 0.0492, 0.0939]

plt.figure(figsize=(10,6))

plt.plot(n_values, dfs_mem, marker='o', label='DFS')

plt.plot(n_values, hill_mem, marker='o', label='Hill Climbing')

plt.plot(n_values, sa_mem, marker='o', label='Simulated Annealing')

plt.plot(n_values, ga_mem, marker='o', label='Genetic Algorithm')

plt.xlabel('Board Size (N)')

plt.ylabel('Memory Usage (MB)')

plt.title('Memory Usage Comparison of N-Queens Algorithms')

plt.legend()

plt.grid(True)

plt.savefig("memory_comparison.pdf",
            format='pdf',
            bbox_inches='tight')

plt.show()
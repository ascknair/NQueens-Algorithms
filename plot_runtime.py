import matplotlib.pyplot as plt

n_values = [10, 30, 50, 100, 200]

dfs_time = [0.0033, 10.0438, 10.0348, 0, 0]

hill_time = [0.1297, 1.3771, 3.8248, 15.1084, 59.13]

sa_time = [0.0813, 0.9126, 2.7729, 11.8371, 49.3129]

ga_time = [1.4124, 15.6479, 47.0435, 203.5354, 833.6867]

plt.figure(figsize=(10,6))

plt.plot(n_values, dfs_time,
         marker='o',
         linewidth=2,
         markersize=8,
         label='DFS')

plt.plot(n_values, hill_time,
         marker='s',
         linewidth=2,
         markersize=8,
         label='Hill Climbing')

plt.plot(n_values, sa_time,
         marker='^',
         linewidth=2,
         markersize=8,
         label='Simulated Annealing')

plt.plot(n_values, ga_time,
         marker='d',
         linewidth=2,
         markersize=8,
         label='Genetic Algorithm')

plt.xlabel('Board Size (N)', fontsize=14)

plt.ylabel('Execution Time (seconds)', fontsize=14)

plt.title('Execution Time Comparison of N-Queens Algorithms',
          fontsize=16)

plt.legend(fontsize=12)

plt.grid(True)

plt.tight_layout()

# SAVE AS PDF VECTOR GRAPHIC
plt.savefig("runtime_comparison.pdf",
            format='pdf',
            bbox_inches='tight')

plt.show()
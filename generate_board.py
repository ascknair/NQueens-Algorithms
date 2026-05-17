import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Example valid 8-Queens solution
solution = [0, 4, 7, 5, 2, 6, 1, 3]

n = len(solution)

fig, ax = plt.subplots(figsize=(8, 8))

# Draw chessboard
for row in range(n):
    for col in range(n):

        color = '#f0d9b5' if (row + col) % 2 == 0 else '#b58863'

        square = patches.Rectangle(
            (col, n - row - 1),
            1,
            1,
            facecolor=color
        )

        ax.add_patch(square)

# Draw queens
for row, col in enumerate(solution):

    ax.text(
        col + 0.5,
        n - row - 0.5,
        '♛',
        fontsize=28,
        ha='center',
        va='center',
        color='black'
    )

# Formatting
ax.set_xlim(0, n)
ax.set_ylim(0, n)

ax.set_xticks([])
ax.set_yticks([])

ax.set_aspect('equal')

plt.title('Valid 8-Queens Solution', fontsize=16)

plt.tight_layout()

# SAVE AS HIGH-QUALITY VECTOR PDF
plt.savefig(
    'nqueens_board.pdf',
    format='pdf',
    bbox_inches='tight'
)

plt.show()
import matplotlib.pyplot as plt
import numpy as np

LABEL_SIZE = 20

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Set background to transparent
fig.patch.set_alpha(0)

# Triangle vertices
A = np.array([3, 0])  # bottom-right
B = np.array([0, 4])  # top-left  
C = np.array([0, 0])  # bottom-left (right angle)

for ax in [ax1, ax2]:
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-0.8, 3.8)
    ax.set_ylim(-0.8, 4.8)
    ax.patch.set_alpha(0)

    # Draw filled triangle
    triangle = plt.Polygon([C, A, B], facecolor='#0072b2', alpha=0.1, edgecolor='none')
    ax.add_patch(triangle)
    
    # Draw triangle outline (black will be inverted to white by book styling)
    ax.plot([C[0], A[0]], [C[1], A[1]], color='black', linewidth=2, zorder=10)
    ax.plot([A[0], B[0]], [A[1], B[1]], color='black', linewidth=2, zorder=10)
    ax.plot([B[0], C[0]], [B[1], C[1]], color='black', linewidth=2, zorder=10)

    # Draw right angle marker at C
    square_size = 0.3
    square = plt.Rectangle((0, 0), square_size, square_size, fill=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(square)

    # Labels for corners
    ax.text(C[0]-0.4, C[1]-0.15, r'$C$', fontsize=LABEL_SIZE, ha='center', va='top')
    ax.text(A[0]+0.15, A[1]-0.15, r'$A$', fontsize=LABEL_SIZE, ha='center', va='top')
    ax.text(B[0]-0.2, B[1]+0.5, r'$B$', fontsize=LABEL_SIZE, ha='center', va='bottom')

# Left figure - with katet labels
ax1.text(-0.5, 2, r'$\mathrm{katet}_1$', fontsize=LABEL_SIZE, ha='right', va='center')
ax1.text(1.3, -0.45, r'$\mathrm{katet}_2$', fontsize=LABEL_SIZE, ha='center', va='top')
ax1.text(3.0, 2.3, r'$\mathrm{Hypotenus}$', fontsize=LABEL_SIZE, ha='center', va='center')

# Right figure - with a, b, c labels
ax2.text(-0.5, 2, r'$a$', fontsize=LABEL_SIZE, ha='right', va='center')
ax2.text(1.3, -0.45, r'$b$', fontsize=LABEL_SIZE, ha='center', va='top')
ax2.text(2.4, 2.3, r'$c$', fontsize=LABEL_SIZE, ha='center', va='center')

plt.tight_layout()
plt.savefig('merged_figure.svg', format='svg', bbox_inches='tight', pad_inches=0.1, transparent=True)
print("Merged figure created successfully: merged_figure.svg")
plt.close()

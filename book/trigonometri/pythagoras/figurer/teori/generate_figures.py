import matplotlib.pyplot as plt
import numpy as np

# Figure 1: Triangle with cathetus labels
fig, ax = plt.subplots(figsize=(5, 4))
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-0.8, 3.8)
ax.set_ylim(-0.8, 4.8)

# Triangle vertices - right angle at C (top-left in this orientation means bottom-left when plotted)
A = np.array([3, 0])  # bottom-right
B = np.array([0, 4])  # top-left  
C = np.array([0, 0])  # bottom-left (right angle)

# Draw filled triangle
triangle = plt.Polygon([C, A, B], facecolor='#0072b2', alpha=0.1, edgecolor='black', linewidth=1.5)
ax.add_patch(triangle)

# Draw right angle marker at C
square_size = 0.3
square = plt.Rectangle((0, 0), square_size, square_size, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(square)

# Labels for corners
ax.text(C[0]-0.4, C[1]-0.15, r'$C$', fontsize=24, ha='center', va='top')
ax.text(A[0]+0.15, A[1]-0.15, r'$A$', fontsize=24, ha='center', va='top')
ax.text(B[0]-0.2, B[1]+0.5, r'$B$', fontsize=24, ha='center', va='bottom')

# Labels for sides (opposite sides)
# Side a (opposite to A): from C to B (left vertical side)
ax.text(-0.4, 2, r'$\mathrm{katet}_1$', fontsize=24, ha='center', va='center')

# Side b (opposite to B): from C to A (bottom horizontal side)
ax.text(1.3, -0.25, r'$\mathrm{katet}_2$', fontsize=24, ha='center', va='top')

# Side c (opposite to C): from A to B (hypotenuse)
ax.text(1.6, 2.2, r'Hypotenus', fontsize=24, ha='center', va='center')

plt.tight_layout()
plt.savefig('figur1.svg', bbox_inches='tight', pad_inches=0)
print("Figure 1 saved: figur1.svg")
plt.close()

# Figure 2: Triangle with a, b, c labels
fig, ax = plt.subplots(figsize=(5, 4))
ax.set_aspect('equal')  
ax.axis('off')
ax.set_xlim(-0.8, 3.8)
ax.set_ylim(-0.8, 4.8)

# Same triangle
triangle = plt.Polygon([C, A, B], facecolor='#0072b2', alpha=0.1, edgecolor='black', linewidth=1.5)
ax.add_patch(triangle)

# Draw right angle marker at C
square = plt.Rectangle((0, 0), square_size, square_size, fill=False, edgecolor='black', linewidth=1.5)
ax.add_patch(square)

# Labels for corners
ax.text(C[0]-0.4, C[1]-0.15, r'$C$', fontsize=24, ha='center', va='top')
ax.text(A[0]+0.15, A[1]-0.15, r'$A$', fontsize=24, ha='center', va='top')
ax.text(B[0]-0.2, B[1]+0.5, r'$B$', fontsize=24, ha='center', va='bottom')

# Labels for sides using a, b, c convention (c is hypotenuse)
# Side a (opposite to A): from C to B (left vertical side)
ax.text(-0.4, 2, r'$a$', fontsize=24, ha='center', va='center')

# Side b (opposite to B): from C to A (bottom horizontal side)  
ax.text(1.3, -0.25, r'$b$', fontsize=24, ha='center', va='top')

# Side c (opposite to C): from A to B (hypotenuse)
ax.text(1.6, 2.2, r'$c$', fontsize=24, ha='center', va='center')

plt.tight_layout()
plt.savefig('figur2.svg', bbox_inches='tight', pad_inches=0)
print("Figure 2 saved: figur2.svg")
plt.close()

print("\nNow merge the figures horizontally:")
print("Run: python merge_figures.py")

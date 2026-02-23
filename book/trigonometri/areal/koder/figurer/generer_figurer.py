"""
Generer SVG-figurer for områdeformler
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import plotmath


def main(dirname, save):
    """Generer alle områdeformelfigurer"""

    # Stil
    color_shape = plotmath.COLORS.get("blue") or "blue"
    color_dimension = plotmath.COLORS.get("red") or "red"
    fontsize = 20

    def plot_polygon(ax, points, alpha=0.1):
        plotmath.plot_polygon(*points, ax=ax, show_vertices=True, alpha=alpha)

    figures = []

    # 1. REKTANGEL
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    rect_points = [(1, 1), (4, 1), (4, 3), (1, 3)]
    plot_polygon(ax, rect_points)

    ax.annotate('', xy=(1, 0.5), xytext=(4, 0.5),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(2.5, 0.15, r'$b$', fontsize=fontsize, ha='center', color=color_dimension)

    ax.annotate('', xy=(4.5, 1), xytext=(4.5, 3),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(4.85, 2, r'$h$', fontsize=fontsize, ha='left', color=color_dimension)

    figures.append((fig, 'areal_rektangel.svg'))

    # 2. KVADRAT
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    square_points = [(1, 1), (3.5, 1), (3.5, 3.5), (1, 3.5)]
    plot_polygon(ax, square_points)

    ax.annotate('', xy=(1, 0.5), xytext=(3.5, 0.5),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(2.25, 0.15, r'$s$', fontsize=fontsize, ha='center', color=color_dimension)

    ax.annotate('', xy=(3.8, 1), xytext=(3.8, 3.5),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(4.15, 2.25, r'$s$', fontsize=fontsize, ha='left', color=color_dimension)

    figures.append((fig, 'areal_kvadrat.svg'))

    # 3. TREKANT
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    triangle_points = [(1, 1), (4, 1), (2.5, 3.5)]
    plot_polygon(ax, triangle_points)
    ax.plot([2.5, 2.5], [1, 3.5], 'k--', lw=1, alpha=0.5)

    ax.annotate('', xy=(1, 0.5), xytext=(4, 0.5),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(2.5, 0.15, r'$g$', fontsize=fontsize, ha='center', color=color_dimension)

    ax.annotate('', xy=(2.15, 1), xytext=(2.15, 3.5),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(1.7, 2.25, r'$h$', fontsize=fontsize, ha='right', color=color_dimension)

    figures.append((fig, 'areal_trekant.svg'))

    # 4. PARALLELLOGRAM
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    parallelogram_points = [(1, 1), (4, 1), (4.5, 3), (1.5, 3)]
    plot_polygon(ax, parallelogram_points)
    ax.plot([1.5, 1.5], [1, 3], 'k--', lw=1, alpha=0.5)
    ax.plot([4.5, 4.5], [1, 3], 'k--', lw=1, alpha=0.5)

    ax.annotate('', xy=(1, 0.5), xytext=(4, 0.5),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(2.5, 0.15, r'$g$', fontsize=fontsize, ha='center', color=color_dimension)

    ax.annotate('', xy=(0.7, 1), xytext=(0.7, 3),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(0.3, 2, r'$h$', fontsize=fontsize, ha='right', color=color_dimension)

    figures.append((fig, 'areal_parallellogram.svg'))

    # 5. TRAPESIUM
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    trapezium_points = [(1, 1), (4, 1), (3.5, 3), (1.5, 3)]
    plot_polygon(ax, trapezium_points)
    ax.plot([1.5, 1.5], [1, 3], 'k--', lw=1, alpha=0.5)

    ax.annotate('', xy=(1, 0.5), xytext=(4, 0.5),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(2.5, 0.15, r'$b$', fontsize=fontsize, ha='center', color=color_dimension)

    ax.annotate('', xy=(3.7, 3), xytext=(3.7, 1),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(4.1, 2, r'$h$', fontsize=fontsize, ha='left', color=color_dimension)

    ax.annotate('', xy=(1.5, 3.35), xytext=(3.5, 3.35),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(2.5, 3.65, r'$a$', fontsize=fontsize, ha='center', color=color_dimension)

    figures.append((fig, 'areal_trapesium.svg'))

    # 6. SIRKEL
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    circle = patches.Circle((2.5, 2.5), 1.5, linewidth=2, edgecolor=color_shape, facecolor=color_shape, alpha=0.2)
    ax.add_patch(circle)

    ax.plot([2.5, 4], [2.5, 2.5], 'k-', lw=1.5)
    ax.plot(2.5, 2.5, 'ko', markersize=6)
    ax.plot(4, 2.5, 'ko', markersize=5)

    ax.annotate('', xy=(2.5, 2.15), xytext=(4, 2.15),
                arrowprops=dict(arrowstyle='<->', color=color_dimension, lw=2))
    ax.text(3.25, 1.8, r'$r$', fontsize=fontsize, ha='center', color=color_dimension)

    figures.append((fig, 'areal_sirkel_figur.svg'))

    if save:
        for fig, fname in figures:
            plt.figure(fig.number)
            plotmath.savefig(dirname=dirname, fname=fname)
            plt.close(fig)


if __name__ == "__main__":
    main(dirname='.', save=True)

"""Generate the checkers starting-position figure used in Lecture 3.

Draws an 8x8 board with dark/light squares and 12 pieces per side placed on
the dark squares of the first three rows on each end (the standard checkers
setup, matching the row/column parity logic discussed in the lecture).

Run from this directory:
    python make_checkers_start_figure.py
Writes checkers_start.png next to this script.
"""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

SIZE = 8
LIGHT = "#EDD6B3"  # light squares
DARK = "#7A5230"   # dark squares (pieces live here)
P1_FACE, P1_EDGE = "#1a1a1a", "#000000"  # player 1 (top rows)
P2_FACE, P2_EDGE = "#f5f5f5", "#888888"  # player 2 (bottom rows)


def is_dark_square(row, col):
    """Dark squares are those where row and column parity differ.

    This matches the lecture's board-filling logic: on even rows the pieces
    sit in odd columns, and on odd rows in even columns.
    """
    return (row + col) % 2 == 1


def main():
    fig, ax = plt.subplots(figsize=(6, 6))

    for row in range(SIZE):
        for col in range(SIZE):
            color = DARK if is_dark_square(row, col) else LIGHT
            # Draw row 0 at the TOP (player 1's home rows), like the matrix.
            y = SIZE - 1 - row
            ax.add_patch(Rectangle((col, y), 1, 1, facecolor=color, edgecolor="none"))

            piece = None
            if is_dark_square(row, col):
                if row < 3:
                    piece = (P1_FACE, P1_EDGE)   # player 1: first three rows
                elif row >= SIZE - 3:
                    piece = (P2_FACE, P2_EDGE)   # player 2: last three rows
            if piece:
                face, edge = piece
                ax.add_patch(Circle((col + 0.5, y + 0.5), 0.35,
                                    facecolor=face, edgecolor=edge, linewidth=1.5))

    # Row letters (A..H top to bottom) and column numbers (1..8 left to right),
    # matching the labeling scheme used in the lecture.
    for row in range(SIZE):
        ax.text(-0.35, SIZE - 1 - row + 0.5, "ABCDEFGH"[row],
                ha="center", va="center", fontsize=11)
    for col in range(SIZE):
        ax.text(col + 0.5, SIZE + 0.20, str(col + 1),
                ha="center", va="center", fontsize=11)

    ax.add_patch(Rectangle((0, 0), SIZE, SIZE, fill=False, edgecolor="black", linewidth=1.5))
    ax.set_xlim(-0.8, SIZE + 0.2)
    ax.set_ylim(-0.2, SIZE + 0.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Checkers starting position", fontsize=13)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "checkers_start.png")
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

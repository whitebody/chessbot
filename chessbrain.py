self.gs = np.array([
    np.array(['bR', 'bN', 'bB', '--', 'bK', 'bB', 'bN', 'bR']),  # Row 0: Black major pieces
    np.array(['bP', 'bP', '--', '--', 'bP', 'bP', 'bP', 'bP']),  # Row 1: Black pawns
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 2: Empty
    np.array(['--', 'wN', 'bP', 'bP', '--', '--', '--', '--']),  # Row 3: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 4: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 5: Empty
    np.array(['bQ', 'wP', 'wP', 'wP', 'wQ', 'wP', 'wP', 'wP']),  # Row 6: White pawns
    np.array(['wR', 'wN', 'wB', '--', 'wK', 'wB', '--', 'wR'])   # Row 7: White major pieces
])

self.gs = np.array([
    np.array(['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']),  # Row 0: Black major pieces
    np.array(['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP']),  # Row 1: Black pawns
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 2: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 3: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 4: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 5: Empty
    np.array(['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']),  # Row 6: White pawns
    np.array(['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'])   # Row 7: White major pieces
])

self.gs = np.array([
    np.array(['bR', 'bN', 'bB', '--', 'bK', 'bB', '--', 'bR']),  # Row 0: Black major pieces
    np.array(['bP', 'bP', 'bP', 'bP', '--', 'bP', '--', 'bP']),  # Row 1: Black pawns
    np.array(['--', '--', '--', '--', '--', 'wK', '--', '--']),  # Row 2: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 3: Empty
    np.array(['--', '--', 'wQ', '--', '--', '--', '--', '--']),  # Row 4: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 5: Empty
    np.array(['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']),  # Row 6: White pawns
    np.array(['wR', 'wN', 'wB', '--', '--', 'wB', 'wN', 'wR'])   # Row 7: White major pieces
])


 
import numpy as np
import random
class Gamestate:
    def __init__(self):
        self.gs = np.array([
    np.array(['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']),  # Row 0: Black major pieces
    np.array(['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP']),  # Row 1: Black pawns
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 2: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 3: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 4: Empty
    np.array(['--', '--', '--', '--', '--', '--', '--', '--']),  # Row 5: Empty
    np.array(['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']),  # Row 6: White pawns
    np.array(['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'])   # Row 7: White major pieces
])
       
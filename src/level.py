import pygame
from sprites import Player, Box

class Level:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size

    #one basic grid for now
    def generate_grid(self):
        matrix = [[0] * self.cols for _ in range(self.rows)]
        for i in range(self.cols):
            matrix[0][i] = 1
        matrix[-1][self.cols // 2] = 2
        return matrix
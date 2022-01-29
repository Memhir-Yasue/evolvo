import numpy as np


class AdjacencyMatrix:
    def __init__(self, max_rows):
        self.max_rows = max_rows
        self.matrix = np.zeros((max_rows, max_rows))

    def activate_relation(self, elem_1, elem_2):
        self.matrix[elem_1][elem_2] = 1
        self.matrix[elem_2][elem_1] = 1

    def deactivate_relation(self, elem_1, elem_2):
        self.matrix[elem_1][elem_2] = 0
        self.matrix[elem_2][elem_1] = 0

    def get_matrix(self):
        return self.matrix

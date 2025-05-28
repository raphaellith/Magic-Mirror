import numpy as np
from Funcs import get_polygon_area


class Lens:
    def __init__(self, image_size):
        self.image_width, self.image_height = image_size
        self.grid = np.array(
            [
                [[x, y] for x in range(self.image_width+1)] for y in range(self.image_height+1)
            ]
        )

    def get_cell_areas(self):
        return np.array(
            [
                [
                    get_polygon_area([
                        self.grid[y, x],
                        self.grid[y, x+1],
                        self.grid[y+1, x+1],
                        self.grid[y+1, x]
                    ]) for x in range(self.image_width)
                ] for y in range(self.image_height)
            ]
        )

    def get_total_area(self):
        return self.image_width * self.image_height

    def get_loss(self, target_image_brightnesses):
        return self.get_cell_areas() / self.get_total_area() - target_image_brightnesses


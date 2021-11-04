import numpy as np
from typing import Tuple


class Vector2D:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def duplicate(self):
        return Vector2D(self.x, self.y)

    def set(self, vals: Tuple[float, float]):
        self.x, self.y = vals

    def normalize(self):
        normal = np.array([self.x, self.y], dtype=float)
        normal /= np.linalg.norm(normal)
        self.x = normal[0]
        self.y = normal[1]

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def sub(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def mult(self, val):
        self.x *= val
        self.y *= val

    def div(self, val):
        self.x /= val
        self.y /= val

    def limit(self, limit: float):
        normal = np.array([self.x, self.y], dtype=float)
        mag = np.linalg.norm(normal)
        f = min(mag, limit) / mag if mag != 0 else 1
        self.x = self.x * f
        self.y = self.y * f

    def set_magnitude(self, new_mag):
        normal = np.array([self.x, self.y], dtype=float)
        mag = np.linalg.norm(normal)
        self.x = self.x * new_mag / mag
        self.y = self.y * new_mag / mag

    def randomize(self):
        result = np.random.uniform(low=-1, high=1, size=(2,))
        result /= np.linalg.norm(result)
        self.x = result[0]
        self.y = result[1]

    def euclidean_dis(self, other):
        return np.linalg.norm(np.array([self.x, self.y]) - np.array([other.x, other.y]))


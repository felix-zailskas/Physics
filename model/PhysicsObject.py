import numpy as np
from model.Vector2D import Vector2D


class PhysicsObject:

    def __init__(self, x: float, y: float, mass: float, vel: [float] = [0, 0], acc: [float] = [0, 0], size: int = 15):
        self.pos = Vector2D(x, y)
        self.vel = Vector2D(vel[0], vel[1])
        self.acc = Vector2D(acc[0], acc[1])
        self.mass = mass
        self.size = size

    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)

    def seek(self, goal):
        x, y = goal
        self.acc = Vector2D(x, y)
        self.acc.sub(self.pos)
        #self.acc.normalize()
        #distance = self.acc.euclidian_dis(self.pos)
        #magnitude = 1 / distance
        self.acc.set_magnitude(0.1)

    def apply_force(self, force: Vector2D):
        self.acc.add(Vector2D(force.x / self.mass, force.y / self.mass))

    def check_edges(self, boundaries: [int]):
        width, height = boundaries
        if self.pos.x + self.size > width:
            self.pos.x = width - self.size
            self.vel.x *= -1
        if self.pos.x - self.size < 0:
            self.pos.x = self.size
            self.vel.x *= -1
        if self.pos.y + self.size > height:
            self.pos.y = height - self.size
            self.vel.y *= -1
        if self.pos.y - self.size < 0:
            self.pos.y = self.size
            self.vel.y *= -1

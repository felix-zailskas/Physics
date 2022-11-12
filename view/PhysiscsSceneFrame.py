from operator import add
import pygame
import time
from model.PhysicsScene import PhysicsScene
from model.Vector2D import Vector2D
from util.config import (
    BLACK,
    WHITE,
    GRAY,
    GREEN,
    FONT_SIZE,
    FRAME_RATE
)



class PhysicsSceneFrame:
    def __init__(self, scene: PhysicsScene, width: int, height: int):
        self.scene = scene
        self.width = width
        self.height = height
        self.add_mode = True

    def draw_objects(self, display):
        for obj in self.scene.objects:
            pygame.draw.circle(display, BLACK, (obj.pos.x, obj.pos.y), obj.size)

    def draw_attraction_forces(self, display):
        for force in self.scene.attraction_forces:
            pygame.draw.circle(display, GREEN, (force.x, force.y), 5)

    def draw_global_forces(self, display):
        font = pygame.font.SysFont(None, FONT_SIZE)
        textsurface = font.render(
            f"Gravity: ({self.scene.gravity.x}, {self.scene.gravity.y})", False, BLACK
        )
        display.blit(textsurface, (10, 0))
        textsurface = font.render(f"Adding Force: {self.add_mode}", False, BLACK)
        display.blit(textsurface, (10, FONT_SIZE))
        textsurface = font.render(f"Friction Coeff: {self.scene.friction_coefficient:.02}", False, BLACK)
        display.blit(textsurface, (10, 2*FONT_SIZE))
        for i, force in enumerate(self.scene.global_forces):
            textsurface = font.render(f"Force: ({force.x},{force.y})", False, BLACK)
            display.blit(textsurface, (10, (i + 3)*FONT_SIZE))

    def init_scene(self):
        print("Call specific Scene to init Scene")

    def start_scene(self):
        print("Call specific Scene to see Results")

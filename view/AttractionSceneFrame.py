import pygame
import time
import random
from .PhysiscsSceneFrame import PhysicsSceneFrame
from model.PhysicsScene import PhysicsScene, PhysicsObject
from model.Vector2D import Vector2D
from util.config import (
    BLACK,
    WHITE,
    GRAY,
    GREEN,
    FONT_SIZE,
    FRAME_RATE
)

class AttractionSceneFrame(PhysicsSceneFrame):
    def __init__(self, scene: PhysicsScene, width: int, height: int):
        PhysicsSceneFrame.__init__(self, scene, width, height)

    def init_scene(self):
        gravity = Vector2D(0, 0.3)
        self.scene.set_gravity(gravity)
        for _ in range(3):
            mass = random.uniform(1, 5)
            self.scene.add_object(
                PhysicsObject(random.randint(0, self.width), self.height / 2, mass, size=mass * 10)
            )

    def start_scene(self):
        pygame.init()
        pygame.display.set_caption("Physics Simulation")
        pygame.font.init()
        display = pygame.display.set_mode((self.width, self.height))

        self.add_mode = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # check for key presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.add_mode = not self.add_mode
                    if event.key == pygame.K_ESCAPE:
                        self.scene.remove_all_forces("attraction")
                # check for mouse events
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.add_mode:
                        new_force = Vector2D(0, 0)
                        new_force.set_values(pygame.mouse.get_pos())
                        self.scene.add_attraction_force(new_force)
                    else:
                        self.scene.remove_force(
                            self.scene.closest_force_to_pos(
                                pygame.mouse.get_pos(), "attraction"
                            )
                        )

            display.fill(GRAY)

            self.scene.update(boundaries=(self.width, self.height))
            self.draw_objects(display)
            self.draw_global_forces(display)
            self.draw_attraction_forces(display)

            pygame.display.update()
            time.sleep(FRAME_RATE)

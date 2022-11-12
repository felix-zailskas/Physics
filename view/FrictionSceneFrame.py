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

class FrictionSceneFrame(PhysicsSceneFrame):
    def __init__(self, scene: PhysicsScene, width: int, height: int):
        PhysicsSceneFrame.__init__(self, scene, width, height)
        self.wind = Vector2D(0.1,0)

    def init_scene(self):
        self.scene.set_gravity(Vector2D(0, 0.3))
        self.scene.add_global_force(self.wind)
        self.scene.add_global_force(Vector2D(0,-0.1))
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
                        self.scene.remove_all_forces("all")
                    if event.key == pygame.K_RIGHT:
                        self.scene.remove_force(self.wind)
                        self.wind.set_values((0.1,0))
                        self.scene.add_global_force(self.wind)
                    if event.key == pygame.K_LEFT:
                        self.scene.remove_force(self.wind)
                        self.wind.set_values((-0.1,0))
                        self.scene.add_global_force(self.wind)
                    if event.key == pygame.K_UP:
                        self.scene.set_friction_coefficient(max(-1.0, self.scene.friction_coefficient - 0.01))
                    if event.key == pygame.K_DOWN:
                        self.scene.set_friction_coefficient(min(0.0, self.scene.friction_coefficient + 0.01))
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

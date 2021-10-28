import pygame
import time
from model.PhysicsScene import PhysicsScene
from model.Vector2D import Vector2D

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (122, 122, 122)
GREEN = (0, 255, 0)


class PhysicsSceneFrame:
    def __init__(self, scene: PhysicsScene, width: int, height: int):
        self.scene = scene
        self.width = width
        self.height = height

    def draw_objects(self, display):
        for obj in self.scene.objects:
            pygame.draw.circle(display, BLACK, (obj.pos.x, obj.pos.y), obj.size)

    def draw_attraction_forces(self, display):
        for force in self.scene.attraction_forces:
            pygame.draw.circle(display, GREEN, (force.x, force.y), 5)

    def draw_global_forces(self, display):
        font_size = 20
        font = pygame.font.SysFont(None, font_size)
        textsurface = font.render(f"Gravity: ({self.scene.gravity.x}, {self.scene.gravity.y})", False, BLACK)
        display.blit(textsurface, (10, 0))
        textsurface = font.render("Forces:", False, BLACK)
        display.blit(textsurface, (10, font_size))
        """
        for i, force in enumerate(self.scene.global_forces):
            textsurface = font.render(f"{i}:({force.x} , {force.y})", False, BLACK)
            display.blit(textsurface, (10, (i + 2) * font_size))
            """

    def start_scene(self):
        pygame.init()
        pygame.font.init()
        display = pygame.display.set_mode((self.width, self.height))

        mouse_force = Vector2D(0, 0)

        mouse_pressed = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pressed = not mouse_pressed
                    if mouse_pressed:
                        mouse_force.set(pygame.mouse.get_pos())
                    self.scene.add_attraction_force(mouse_force) if mouse_pressed else \
                        self.scene.remove_force(mouse_force)

            display.fill(GRAY)

            self.scene.update(boundaries=(self.width, self.height))
            self.draw_objects(display)
            self.draw_global_forces(display)
            self.draw_attraction_forces(display)

            pygame.display.update()
            time.sleep(0.01)

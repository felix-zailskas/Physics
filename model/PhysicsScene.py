from model.PhysicsObject import PhysicsObject
from model.Vector2D import Vector2D
from typing import List, Tuple
import numpy as np
from util.config import FRICTION_COEFFICIENT

class PhysicsScene:
    objects: List[PhysicsObject]
    global_forces: List[Vector2D]
    attraction_forces: List[Vector2D]

    def __init__(self):
        self.objects = []
        self.global_forces = []
        self.attraction_forces = []
        self.gravity = Vector2D(0, 0)
        self.friction_coefficient = FRICTION_COEFFICIENT

    def set_gravity(self, gravity):
        self.gravity = gravity

    def set_friction_coefficient(self, friction_coefficient):
        self.friction_coefficient = friction_coefficient

    def add_object(self, obj: PhysicsObject):
        self.objects.append(obj)

    def add_global_force(self, force: Vector2D):
        self.global_forces.append(force)

    def add_attraction_force(self, force: Vector2D):
        self.attraction_forces.append(force)

    def closest_force_to_pos(self, pos: Tuple[float, float], type: str):
        min_dist = np.inf
        closest_force = None
        x, y = pos
        pos = Vector2D(x, y)
        if type == "attraction":
            for force in self.attraction_forces:
                dist = pos.euclidean_dis(force)
                if dist < min_dist:
                    min_dist = dist
                    closest_force = force
        return closest_force

    def remove_object(self, obj: PhysicsObject):
        if obj in self.objects:
            self.objects.remove(obj)

    def remove_force(self, force: Vector2D):
        if force in self.global_forces:
            self.global_forces.remove(force)
        if force in self.attraction_forces:
            self.attraction_forces.remove(force)

    def remove_all_forces(self, force_type: str):
        if force_type == "attraction" or force_type == "all":
            self.attraction_forces = []
        if force_type == "global" or force_type == "all":
            self.global_forces = []

    def apply_gravity(self, obj: PhysicsObject):
        apply_grav = self.gravity.duplicate()
        apply_grav.mult(obj.mass)
        obj.apply_force(apply_grav)
    
    def apply_friction(self, obj: PhysicsObject):
        friction = obj.vel.duplicate()
        if np.linalg.norm(np.array([friction.x, friction.y])) == 0:
            return
        friction.normalize()
        friction.mult(self.friction_coefficient)
        obj.apply_force(friction)

    def apply_global_forces(self, obj: PhysicsObject):
        for force in self.global_forces:
            obj.apply_force(force)

    def apply_attraction_forces(self, obj: PhysicsObject):
        for force in self.attraction_forces:
            # find relative offset to object's position
            # get the force that moves the object there
            to_apply = Vector2D(force.x, force.y)
            to_apply.sub(obj.pos)
            # normalize the force in some way
            to_apply.normalize()
            # apply force
            obj.apply_force(to_apply)

    def update(
        self,
        boundaries: Tuple[int, int] = None,
        seek_pos: Tuple[int, int] = None,
        seek_check=None,
    ):
        for obj in self.objects:
            obj.update()
            self.apply_gravity(obj)
            self.apply_friction(obj)
            self.apply_global_forces(obj)
            self.apply_attraction_forces(obj)
            if boundaries is not None:
                obj.check_edges(boundaries)
            if seek_check is not None:
                if seek_check(obj) and seek_pos is not None:
                    obj.seek(seek_pos)

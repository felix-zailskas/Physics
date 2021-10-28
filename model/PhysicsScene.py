from model.PhysicsObject import PhysicsObject
from model.Vector2D import Vector2D


class PhysicsScene:
    objects: [PhysicsObject]
    global_forces: [Vector2D]
    attraction_forces: [Vector2D]

    def __init__(self):
        self.objects = []
        self.global_forces = []
        self.attraction_forces = []
        self.gravity = Vector2D(0, 0)

    def set_gravity(self, gravity):
        self.gravity = gravity

    def add_object(self, obj: PhysicsObject):
        self.objects.append(obj)

    def add_global_force(self, force: Vector2D):
        self.global_forces.append(force)

    def add_attraction_force(self, force: Vector2D):
        self.attraction_forces.append(force)

    def remove_object(self, obj: PhysicsObject):
        if obj in self.objects:
            self.objects.remove(obj)

    def remove_force(self, force: Vector2D):
        if force in self.global_forces:
            self.global_forces.remove(force)
        if force in self.attraction_forces:
            self.attraction_forces.remove(force)

    def apply_gravity(self, obj):
        apply_grav = self.gravity.duplicate()
        apply_grav.mult(obj.mass)
        obj.apply_force(apply_grav)

    def apply_global_forces(self, obj):
        for force in self.global_forces:
            obj.apply_force(force)

    def apply_attraction_forces(self, obj):
        for force in self.attraction_forces:
            # find relative offset to object's position
            # get the force that moves the object there
            to_apply = Vector2D(force.x, force.y)
            to_apply.sub(obj.pos)
            # normalize the force in some way
            to_apply.normalize()
            # apply force
            obj.apply_force(to_apply)

    def update(self, boundaries: (int, int) = None, seek_pos: (int, int) = None, seek_check=None):
        for obj in self.objects:
            obj.update()
            self.apply_gravity(obj)
            self.add_global_force(obj)
            self.apply_attraction_forces(obj)
            if boundaries is not None:
                obj.check_edges(boundaries)
            if seek_check is not None:
                if seek_check(obj) and seek_pos is not None:
                    obj.seek(seek_pos)


import random
from model.PhysicsScene import PhysicsScene, PhysicsObject, Vector2D
from view.PhysiscsSceneFrame import PhysicsSceneFrame


def main():
    width = 800
    height = 600
    gravity = Vector2D(0, 0.1)

    scene = PhysicsScene()
    scene.set_gravity(gravity)

    for i in range(5):
        mass = random.uniform(1, 3)
        scene.add_object(PhysicsObject(random.randint(0, width), height / 2, mass, size=mass * 10))

    frame = PhysicsSceneFrame(scene, width, height)
    frame.start_scene()


if __name__ == '__main__':
    main()


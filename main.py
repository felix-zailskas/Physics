import random
from model.PhysicsScene import PhysicsScene, PhysicsObject, Vector2D
from view.AttractionSceneFrame import AttractionSceneFrame
from view.FrictionSceneFrame import FrictionSceneFrame


def main():
    width = 800
    height = 600
    
    scene = PhysicsScene()
    frame = FrictionSceneFrame(scene, width, height)
    frame.init_scene()
    frame.start_scene()


if __name__ == "__main__":
    main()

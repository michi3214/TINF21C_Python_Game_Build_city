"""
This is the class My_Sky.
    * generate a sphere around the playfield
    * create a sky for the player

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 01.05.2023
    Version 1.0.0
    license: MIT
"""

from ursina import *
from loguru import logger


class My_Sky(Entity):
    """My_Sky:
        * define the view from far away
        * define an image for sky 
    
    Test:
        * is displayed corectly
        * has the rigth scale (big enough for the playfield)
    """
    def __init__(self):
        logger.debug("Sky was initialized")
        super().__init__(
            add_to_scene_entities = False,
            parent=scene,
            model="sphere",
            texture="assets/skybox.png",
            scale = 150,
            double_sided= True
            )
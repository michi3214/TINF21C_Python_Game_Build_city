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
    """class My_Sky:
        * define the view from far away
        * define an image for the sky 
    
    Test:
        * is displayed correctly
        * has the right scale (big enough for the game field)
    
    TODO for future:
        * sky has an end, player can move out of the sky 
    """
    def __init__(self, parent):
        logger.debug("Sky was initialized")
        super().__init__(
            parent=parent,
            model="sphere",
            texture="assets/skybox.png",
            scale = 150,
            double_sided= True
            )
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

class My_Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="sphere",
            texture="assets/skybox.png",
            scale = 150,
            double_sided= True
            )
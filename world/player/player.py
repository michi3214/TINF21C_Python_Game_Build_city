"""
This is the class for My_Player.
    * create one player
    * set camera view to FirstPersonController

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 01.05.2023
    Version 1.0.0
    license: MIT
"""
from ursina.prefabs.first_person_controller import FirstPersonController

class My_Player():
    def __init__(self) -> None:
        __my_player = FirstPersonController()
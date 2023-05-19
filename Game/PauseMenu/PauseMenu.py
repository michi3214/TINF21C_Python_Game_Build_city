"""
In this script is the pause menu implemented. 
    * create pause menu
    * stop and start world (pause, resume) 
    * create buttons for save and close 
    

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 19.05.2023
    Version 1.0.0
    license: MIT
"""


# python module
from ursina import *

class My_Pause_Menu(Entity):
    """class My_Pause_Menu:
        * create pause menu
        * process user interaction with the menu 
    
    Test:
        * create menu as expected
        * can save world in csv file 
        * can stop the world and is be reactive 
    """
    
    def __init__(self, world):
        self.__world = world
        super().__init__(ignore_paused=True, parent = camera.ui)
        save_button = Button("Save world", position=Vec2(0,-0.2), on_click=self.__world.save_world(), parent=self)
        save_button.fit_to_text()
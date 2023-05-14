"""
This is the class for My_Main_Menu.
    * create the main menu
    * load existing world names
    * button to create new game/world
    * user can choose one game

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 02.05.2023
    Version 1.0.0
    license: MIT
"""


# python module
from ursina import *
from loguru import logger


#private modules
from menu.newWorld.newWorld import My_New_World


class My_Main_Menu():
    """class My_Menu:
        * create first menu of the game
        * show existing tables
        * show button to load game
        
        Args:
            handel_function
    
    
    Test:
        *  Can be initialized
        *  show the existing worlds
    """
    def __init__(self, handel_function:Func) -> None:
        logger.info("Open main menu")
        
        self.handel_function = handel_function
        button_dict = {}
        # TODO for i the correct world name must be used, use ls to get existing names
        for i in range(6, 20):
            button_dict[f'Load world {i}'] = Func(handel_function, i)
        button_dict["Add new world"] = Func(self.open_new_world_menu)
        self.bl = ButtonList(button_dict, button_height=1.5)
        self.bl.tooltip = Tooltip("Open menu to create a new world")

        
    def open_new_world_menu(self):
        logger.info("Player want to create new world")
        scene.clear()
        My_New_World(self.handel_function) 

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
from menu.newWorld.newWorldMenu import My_New_World_Menu


class My_Main_Menu(Entity):
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
    def __init__(self,handel_function, **kwargs):
        super().__init__(add_to_scene_entities = True,parent = camera.ui, **kwargs)
        logger.info("Open main menu")
        
        self.handel_function = handel_function
        bg = Entity(model="quad", scale=(16,9), texture="assets\BackgroundMenu.png")
        #Sky(texture="assets\BackgroundMenu.png", texture_scale=Vec2(1,1))
        button_dict = {}
        # TODO for i the correct world name must be used, use ls to get existing names
        for i in range(6, 20):
            button_dict[f'Load world {i}'] = Func(handel_function, i)
        button_dict["Add new world"] = Func(self.open_new_world_menu)
        self.button_list = ButtonList(button_dict, button_height=1.5, parent=self)
        self.button_list.tooltip = Tooltip("Open menu to create a new world")
    

        
    def open_new_world_menu(self):
        logger.info("Player want to create new world")
        destroy(self.button_list)
        My_New_World_Menu(self.handel_function, parent=self) 

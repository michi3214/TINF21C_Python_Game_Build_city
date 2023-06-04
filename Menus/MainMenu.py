"""
The main menu is implemented in this script.
    * show start screen
    * load existing world names
    * world selection

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 02.05.2023
    Version 1.0.0
    license: MIT
"""

# python module
from ursina import *
import os
from loguru import logger


#privat module
from Menus.NewWorldMenu import My_New_World_Menu




class My_Main_Menu(Entity):
    """class My_Main_Menu:
        * show main menu
        * load existing world names
        * let the user interact with buttons
    
        
    Test:
        * can be initialized
        * rendered menu is as expected
        * all worlds are listed and no one is out of the screen
    """
    PATH_TO_WORLDS = os.path.join( os.getcwd(), "saved_worlds")
    
    
    
    
    def __init__(self, handle_world_function:Func):
        logger.info("Main menu was opened")
        super().__init__(parent=camera.ui)
        worlds = self.load_world_names()
        self.handle_world_function = handle_world_function
        

        background = Entity(parent=self, model="quad", texture="assets\BackgroundMenu.png", scale_x=camera.aspect_ratio, z=1)
        button_dict = {}
        for world in worlds:
            button_dict[f'Load world: {world}'] = Func(self.handle_world_function, world, False)
        button_dict["Add new world"] = Func(self.open_new_world_menu)
        button_dict["Close Game"] = Func(application.quit)
        self.button_list = ButtonList(button_dict, button_height=1.5, parent=self)
    
    
    
    
    def input(self, key:str):
        """input:
            * process input of the user
            * shortcuts for the menu
        
        Args:
            * key (str): used key
        
        Return:
            None
        
        Test:
            * is only executed if the user is in this menu
            * no more tests (at the moment this function is not used/implemented)
        """
        #TODO: in later versions here can be shortcuts be implemented
        pass
    
    
    
    
    def load_world_names(self)->list:
        """load_world_names:
            * create folder for PATH_TO_WORLDS, if not existing
            * get list of all files in the PATH_TO_WORLDS path
            * make a name out of the filename 
            * return world names
        
        
        Return:
            list of existing world names
            
        
        Test:
            * find all existing worlds (use the correct path)
            * format the name correctly 
            * create folder to save new worlds, if not existing
        """
        if not os.path.exists(self.PATH_TO_WORLDS):
            os.makedirs(self.PATH_TO_WORLDS) 
        worlds = os.listdir(self.PATH_TO_WORLDS)
        
        result = []
        for world in worlds:
            result.append(world.replace("_"," ").replace(".csv", ""))
        return result
    
    
    
    
    def open_new_world_menu(self):
        """open_new_world_menu:
            * delete this menu from the scene (camera.ui)
            * open the New world menu
        
        
        Return:
            None
        
        Test:
            * actual menu is destroyed correctly
            * new world menu is opened correctly
        """
        My_New_World_Menu(self.handle_world_function)
        destroy(self)
        
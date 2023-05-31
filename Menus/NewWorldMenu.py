"""
This script contains the menu for creating a new world.
    * show menu
    * show info text by wrong input
    * show button to submit input

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 02.05.2023
    Version 1.0.0
    license: MIT
"""

# python module
from ursina import *
from loguru import logger



class My_New_World_Menu(Entity):
    """class My_New_World_Menu:
        * process user input to create a new world
        * get user input (submit, world name)
    
    Return:
        None
    
    Test:
        * user input has been read correctly
        * Buttons and Texts are represented as expected
    """
    TEXT_COLOR = color.black
    
    
    
    
    def __init__(self, handle_world_function:Func):
        logger.info("New world menu was opened")
        super().__init__(parent=camera.ui)
        
        self.handle_world_function = handle_world_function
        Text(
            text="Please enter the world name (if the world already exists, it will be overwritten):",
            position=(-0.35,0.25),
            parent=self,
            color= self.TEXT_COLOR
        )
        self.name_of_world_input = InputField(active=True, parent=self)
        btn_submit = Button("Create new world", position=(0,-0.2), on_click=self.submit, parent=self)
        btn_submit.fit_to_text()
    
    
    
    
    def submit(self)->None:
        """submit:
            * user action: want to create new world
            * get user input for world name
            * destroy the menu
            * call function from main.py to create new world
            * show warning by wrong input
        
        Return:
            None
        
        Test:
            * show warning by wrong input (validate input)
            * destroy the new world menu
            * call function of main.py / create new world
            
        TODO for the future:
            * no underlines in the name are allowed, add validation 
        """
        world_name = self.name_of_world_input.text
        if(world_name == ""):
            Text(text="Please enter a valid name (no empty string):",color=color.red, position=(-0.25,-0.10), parent=self)
        else:
            self.handle_world_function(world_name, True)
            destroy(self)

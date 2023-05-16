"""
This is the class for My_New_World.
    * create the menu to create a new world
    * user can enter a world name
    * start of a new world

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
    """My_New_World:
        * create menu to generate a new world
        * handle input of user 
    
    
    Return:
        None
    
    Test:
        * validate input of user
        * Design is as expected (position of input field / button)
    """
    TEXT_COLOR = color.black
    
    def __init__(self, handel_function:Func,  **kwargs):
        super().__init__(add_to_scene_entities = False, **kwargs)
        logger.info("Create new world menu")
        self.handel_function = handel_function
        Text(text="Please enter the world name (f the world already exists, it will be overwritten):",
             position=(-0.35,0.25),
             parent=self,
             color= self.TEXT_COLOR
             
             )
        self.name_of_world_input = InputField(active=True, parent=self)
        btn_submit = Button("Create new world", position=(0,-0.2), on_click=self.submit, parent=self)
        btn_submit.fit_to_text()
        
    def submit(self):
        """submit:
            * validate user input
            * show message when user input is not valid
        
        
        Return:
            None
        
        Test:
            * Is the error message shown to the user
            * Is the handel_function called, and a new world generated
        """
        world_name = self.name_of_world_input.text
        if(world_name == ""):
            Text(text="Please enter a valid name (no empty string):",color=color.red, position=(-0.25,-0.10), parent=self)
            pass
        else:
            # TODO create new world
            logger.info("New world(" + world_name + ") will be created")
            self.handel_function(world_name)
"""
This is the main script. 
    * create game engine (Ursina)
    * process change between main menu and gaming
    

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 01.05.2023
    Version 1.0.0
    license: MIT
"""



# python module
from ursina import *
from loguru import logger
logger.add("logs/Build_City.log")




# privat module
from Menus.MainMenu import My_Main_Menu as MainMenu
from Game.World import My_World as World
  




def handle_world_selection(world_name:str, new:bool)->None:
    """handle_world_selection:
        * create new world/game instance
        * handle function for new world menu
        * call function of My_World to load / create a world
    
    Args:
        * world_name (str): name of the world
        * new (bool): True=New world, False=Load World
    
    Return:
        None
    
    Test:
        * can be called by new world menu
        * create a new world
    """
    logger.info("Player selected: " + world_name)
    my_world = World(world_name, new)
    
    
    
    
if __name__ == "__main__":
    actual_game_state = "menu"
    
    window.title = "Build City"
    window.borderless = False
    app = Ursina()
    window.exit_button.visible = False
    window.fps_counter.enabled = False
    
    start_menu = MainMenu(handle_world_selection)
    
    app.run()
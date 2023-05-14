"""
This is the main script.
    * create the ursina app
    * handle user interactions 
    * manage user steps (e.g. playing, in the menu, pause, ...)

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
from world.world import My_World
from menu.mainMenu import My_Main_Menu

GAME_STATE = "menu"

def input(key):
    """input:
        * handels user interation
        * choose the rigth input function depending on the GAME_STATE 
    
    Args:
        * key (str): used key (e.g. Keystrokes )
    
    Return:
        None
    
    Test:
        * # TODO: test 1
        * # TODO: test 2
    """
    match GAME_STATE:
        case "menu":
            pass
        case "playing":
            my_playfield.input(key)
        case _:
            logger.error("Game is in an unplanned state (" + GAME_STATE + "). I think you underpaid the developer and he did not finished his work.")




def handle_menu_interaction(world_name:str,  new:bool=True)-> None:
    """handle_menu_interaction:
        * clear the screen  
        * handles user input from the main menu
        * create new world
        * load existing world
    
    
    Return:
        None
    
    Test:
        * can create a new world
        * load an existing world
    """
    scene.clear()
    GAME_STATE = "playing"
    logger.info("Player loaded/created " + world_name)
    # TODO: Not running can not load assests
    my_playfield = My_World(world_name, new)
        
        
    

if __name__ == "__main__":
    window.title = "Build City"
    window.borderless = False               # Show standard windows border of an application
    
    app = Ursina()
    menu =My_Main_Menu(handle_menu_interaction)
    
    

    
    
    
    window.exit_button.visible = False      # Do not show the in-game red X that closes the window
    window.fps_counter.enabled = True       # Do not show the FPS (Frames per second) counter    
    app.run()
    
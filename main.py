"""
This is the main script.
    * create the ursina app
    * handle user interactions 
    * manage game states (e.g. playing, in the menu, pause, ...)
    * close or open the menus

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
my_playfield = My_World

def input(key:str)->None:
    """input:
        * process user interaction
        * choose the right input function depending on the GAME_STATE 
        * process game menu start 
    
    Args:
        * key (str): used key (e.g. Keystrokes )
    
    Return:
        None
    
    Test:
        * call the right function at the game_state
        * all keys for opening the menu are correctly implemented
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
    my_playfield = My_World(world_name, new)
        
        
    

if __name__ == "__main__":
    window.title = "Build City"
    window.borderless = False               # Show standard windows border of an application
    
    app = Ursina()
    menu =My_Main_Menu(handle_menu_interaction)
    # my_playfield = My_World("world_name", True)
    # handle_menu_interaction("world_name", True)

    
    
    
    window.exit_button.visible = False      # Do not show the in-game red X that closes the window
    window.fps_counter.enabled = True       # Do not show the FPS (Frames per second) counter    
    app.run()
    
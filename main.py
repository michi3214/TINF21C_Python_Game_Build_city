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
import os
from ursina import *
from loguru import logger
logger.add("logs/Build_City.log")

# privat module
from world.world import My_World
from menu.mainMenu import My_Main_Menu
from menu.pauseMenu import My_Pause_Menu


my_playfield = My_World
actual_game_state = "menu"
def stop_pause():
    logger.debug("End pause")
    application.resume()
    
    
def input(key:str)->None:
    """input:
        * process user interaction
        * choose the right input function depending on the actual_game_state 
        * process game menu start 
    
    Args:
        * key (str): used key (e.g. Keystrokes )
    
    Return:
        None
    
    Test:
        * call the right function at the game_state
        * all keys for opening the menu are correctly implemented
    """
    global actual_game_state
    match actual_game_state:
        case "menu":
            # here can shortcuts for the main menu implemented
            pass
        
        case "playing":
            if key == "escape":
                logger.debug("Open pause menu")
                actual_game_state = "pause"
                application.pause()
                mouse.visible = True
                mouse.locked = False
                
                pause_handler = My_Pause_Menu(stop_pause)
                pause_handler.input = input
                # TODO Implement pause menu
            else:
                pass
                # my_playfield.input(key)
                
        case "pause":
            logger.debug("Pause menu input")
            if key == "escape":
                stop_pause()
            
            
        case _:
            logger.error("Game is in an unplanned state (" + actual_game_state + "). I think you underpaid the developer and he did not finished his work.")





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
    global actual_game_state
    global my_playfield
    actual_game_state = "playing"
    my_playfield = My_World(world_name, new)
    my_playfield.input = my_playfield.input_function

def load_existing_worlds()->list:
    path_to_worlds = os.path.join( os.getcwd(), "save_worlds")
    worlds = os.listdir(path_to_worlds)
    
    result = []
    for world in worlds:
        result.append(world.replace("_"," ").replace(".csv", ""))
    return result
    

if __name__ == "__main__":
    actual_game_state = "menu"
    window.title = "Build City"
    window.borderless = False               # Show standard windows border of an application
    app = Ursina()
    menu = My_Main_Menu(handle_menu_interaction)
    # load_existing_worlds()
    
    
    
    window.exit_button.visible = False      # Do not show the in-game red X that closes the window
    window.fps_counter.enabled = True       # Do not show the FPS (Frames per second) counter    
    app.run()
    
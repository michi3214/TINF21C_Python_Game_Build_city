"""
This is the class My_World. All functionalities of the game play itself are here. 
    * generate a new world out of voxels
    * save world to csv-file 
    * load world fom csv-file 
    * add or destroy voxels on the play field
    * add player to this world
    * add sky to this world

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 01.05.2023
    Version 1.0.0
    license: MIT
"""

# python module
import pandas as pd
from ursina import *
from loguru import logger

# privat module
from Game.Voxel.Voxel import My_Voxel_Grass
from Game.Voxel.Voxel import My_Voxel_Stone
from Game.Player.Player import My_Player
from Game.Sky.Sky import My_Sky
from Game.PauseMenu.PauseMenu import My_Pause_Menu


class My_World(Entity):
    """class My_World:
        * define the game play 
        * process input while playing
        * add new or destroy voxels
        * save / load world
    
    Test:
        * world can be created
        * existing world can be loaded
    """
    __df_world = pd.DataFrame(columns=["x","y","z","block_type"])
    
    def __init__(self, world_name:str, new:bool):
        super().__init__(parent=scene, ignore_paused = True)
        self.__STR_WORLD_NAME = world_name
        self.player_position = Vec3(5,2,5)
        FILE_NAME = self.__STR_WORLD_NAME.replace(" ", "_")
        self.__SAVE_PATH = os.path.join(os.getcwd(),"saved_worlds", FILE_NAME + ".csv")
        
        My_Sky(parent=self)
        if new:
            logger.info("Player create " + world_name)
            self.__create_world()
            
        else:
            logger.info("Player loaded " + world_name)
            self.__load_world()

        self.player = My_Player(position=self.player_position)
        self.pauseMenu = My_Pause_Menu(self)
        self.pauseMenu.visible = False
    
    
    
    
    def __create_world(self)->None:
        """__create_world:
            * create first blocks in the world
            * add blocks to dataFrame object
    
        Return:
            None
        
        Test:
            * is world generated
            * did the blocks appear around the player
            * is dataframe correctly filled
            * is table in database generated
        """
        self.add_block( Vec3(0,0,0), "grass")
        self.add_block( Vec3(0,-1,0), "grass")
        self.add_block( Vec3(5,0,5), "grass")
        self.add_block( Vec3(5,-1,5), "grass")
        # for z in range(10):
        #     for x in range(10):
        #             self.add_block( Vec3(x,0,z), "grass")
        # for x in range(10):
        #     for y in range(5):
        #         for z in range(10):
        #             self.add_block(Vec3(x,(-1*y)-1,z), "stone")




    def __load_world(self)->None:
        """__load_world:
            * load existing world from csv file
            * load csv to DataFrame
            * create world from the loaded data
            
        Return:
            None
        
        Test:
            * world is generated as expected
            * csv file is loaded correctly into DataFrame
        """
        
        logger.info("World " + self.__STR_WORLD_NAME + " will be loaded from " + self.__SAVE_PATH)
        try:
            self.__df_world = pd.read_csv(self.__SAVE_PATH)
            for index, row in self.__df_world.iterrows():
                logger.debug("Load x,y,z: " + str(row["x"]) +  str(row["y"]) + str(row["z"]))
                self.add_block(Vec3(row["x"], row["y"], row["z"]), row["block_type"])
        except Exception as err:
            logger.error("Could not load the world:")
            logger.error(str(err))
        logger.debug("World loaded")
    
    
    
    
    def save_world(self)->None:
        """save_world:
            * save world (DataFrame) to csv file
            * creates a new file or overwrites an existing one 
        
        Return:
            None
            
        Test:
            * dataFrame is saved correctly into csv
            * new file could be created
            * existing file could be overwritten
        """
        logger.info("World " + self.__STR_WORLD_NAME + " will be saved at " + self.__SAVE_PATH)
        try:
            self.__df_world.to_csv(self.__SAVE_PATH, index=False)
        except Exception as err:
            logger.error("Could not save the world:")
            logger.error(str(err))
    
    
    
    def add_block(self, position:Vec3,  block_type:str)->None:
        """add_block:
            * add voxel to scene in Ursina
            * add voxel (position and type) to DataFrame
        
        Args:
            block_type (str): type of the block_type 
            position (Vec3): (x,y,z) - Positions
        
        Return:
            None
        
        Test:
            * created correct block
            * added block to DataFrame
            * position of new block is correct
        """
        
        match block_type:
            case "grass":
                My_Voxel_Grass(self, position)
            case "stone":
                My_Voxel_Stone(self, position)
            case _:
                logger.error("Programmer used wrong block type. World do not know this type: " + block_type)
                return
        self.__df_world.loc[len(self.__df_world.index)] = [position.x,position.y,position.z,block_type]
        logger.debug("add block: " + str(position.x) + " " + str(position.y) + " " + str(position.z))
                
        
    
    
    def destroy_block(self)->None:
        """destroy_block:
            * destroy hovered block
            * delete block from DataFrame
        
        Return:
            None
        
        Test:
            * is block deleted from DataFrame
            * is blocked deleted from game-engine
        
        TODO for future:
            * delete block by position not by mouse 
        """
        position = mouse.hovered_entity.position
        destroy(mouse.hovered_entity)
        self.__df_world.drop(self.__df_world[(self.__df_world["x"] ==   position.x) & (self.__df_world["y"] ==   position.y) &  (self.__df_world["z"] ==   position.z)].index, inplace=True)
     
       
       
     # TODO: check if it is needed or can be done by on_destroy (see player)       
    def destroy(self):
        """destroy:
            * wrapper to destroy world from Ursina
            * delete player and all children from this world
        
        
        Return:
            None
        
        Test:
            * destroy world itself
            * destroy player (with hand)
        """
        self.player.destroy()
        destroy(self)
    
    
    
    
    def input(self, key:str):
        """input:
            * managing user interaction while playing
            * call functions of the different user interactions (open inventory, ...)
        
        Args:
            * key (str): used key from the user 
        
        Return:
            None
        
        Test:
            * do the function get the right keys 
            * did the case call the right function
        """
        match key:
            case "left mouse down"|"right mouse down":
                self.player.my_arm.use_hand()
            case "left mouse up"|"right mouse up":
                self.player.my_arm.passiv_hand()
            case "escape":
                if application.paused:
                    logger.info("Pause menu closed")
                    mouse.visible = False
                    mouse.locked = True
                    application.resume()
                    # TODOD: hide the arm of the player (is not pause because it is parent = camera.ui)
                    self.pauseMenu.visible = False
                else:
                    logger.info("Pause menu opened")
                    application.pause()
                    mouse.visible = True
                    mouse.locked = False
                    self.pauseMenu.visible = True
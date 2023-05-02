"""
This is the class My_Wrold. All functionalities of the gameplay itselfs are here. 
    * generate a new world out of blocks (voxels)
    * save world to database 
    * load world fom database 
    * add or destroy blocks (voxels) on the playfield
    * add player to the scene
    * add sky to the scene 

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
from world.voxel.voxel import My_Voxel
from world.voxel.voxel import My_Voxel_Grass
from world.voxel.voxel import My_Voxel_Stone
from world.player.player import My_Player
from world.sky.sky import My_Sky



class My_World():
    """class my_World:
        * create world
        * add / destroy blocks (voxels) in the world
        * load world from database 
        * save world into database
    
    Args:
        world_name (str): name of the world
        type_of_creation (str): new world or load world (e.g. "new" or "load") 
    Return:
        None
    
    Test:
        * Can be initialized
        * create first blocks (voxels) in the game-engine
    """

    __df_world = pd.DataFrame(columns=["x","y","z","block_type"])
    

    def __init__(self, world_name:str , type_of_creation:str="new") -> None:
        self.__STR_WORLD_NAME = world_name
        self.player = My_Player()
        My_Sky()
        if type_of_creation == "new":
            self.__create_world()
        elif type_of_creation == "load":
            self.__load_world()
        pass
    
    
    def __create_world(self)->None:
        """__create_world:
            * create first blocks in the world
            * add blocks to dataframe object
            * create new table in database for the world
        
        
        Return:
            None
        
        Test:
            * is world generated
            * did the blocks appear around the player
            * is dataframe correctly filled
            * is table in database generated
        """
        logger.info("Create a new world with the name" + self.__STR_WORLD_NAME)
        for z in range(10):
            for x in range(10):
                    self.add_block( Vec3(x,0,z), "grass")
        for x in range(10):
            for y in range(5):
                for z in range(10):
                    self.add_block(Vec3(x,(-1*y)-1,z), "stone")
                    
        # TODO: implement creation new tbl in database 
    
     
    def add_block(self, position:Vec3,  block_type:str)->None:
        """add_block:
            * add voxel to scene in ursina
            * add voxel to dataframe
        
        Args:
            block_type (str): type of the block_type 
            position (Vec3): (x,y,z) - Positions
        
        Return:
            None
        
        Test:
            * created correct block
            * added block to dataframe
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
                
        
    
    
     # - delete from game engine
    def destroy_block(self,position:Vec3)->None:
        """destroy_block:
            * destroy one block
            * delete block from dataframe
        
        Args:
            * position (Vec3): (x,y,z,) - Position
        
        Return:
            None
        
        Test:
            * is block deleted from dataframe
            * is blocked deleted from game-engine
        """
        self.__df_world.drop(self.__df_world[(self.__df_world["x"] ==   position.x) & (self.__df_world["y"] ==   position.y) &  (self.__df_world["z"] ==   position.z)].index, inplace=True)
        destroy(mouse.hovered_entity)
    
    # TODO: implement functionality
     # - save dataframe to sqlite
    def save_world(self)->None:
        """save_world:
            * save world (dataframe) to database
        
        
        Return:
            None
        Test:
            * connection to the database is created
            * data is loaded into the database correctly
            
        """
        pass
    
    # TODO: implement functionality
     # - load dataframe from sqlite
    def __load_world(self)->None:
        """__load_world:
            * load data from database
            * create world from the data
        
        
        Return:
            None
            
        Test:
            * Loaded world corectly from database
            * Add all blocks to ursina 
        """
        logger.info("Load world " + self.__STR_WORLD_NAME + " from database")
        pass
    
    def input(self, key)->None:
        """input:
            * managing user interaction while playing
            * call functions of the different user interactions (open inventory, ...)
        
        Args:
            * key (str): used key from the user 
        
        Return:
            None
        
        Test:
            * do the function get the rigth keys 
            * did the case call the rigth function
        """
        match key:
            case "left mouse down"|"right mouse down":
                self.player.use_hand()
            case "left mouse up"|"right mouse up":
                self.player.passiv_hand()
        
        
    

import pandas as pd 
class my_World():
    """class my_World
        * create world
        * add / destroy blocks in the world
        * load world from database 
        * save world into database
        
        Tests:
            * Can be initialized
            * create first blocks in game-engine
    """
    __df_world = pd.DataFrame(columns=["x","y","z","block"])
    __str_world_name = ""
    

    def __init__(self, world_name) -> None:
        self.__str_world_name = world_name
        self.__create_world()
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
            * is dataframe correctly filled
        """
        # TODO: implement function
        pass
    
     
    def add_block(self, block:str, x:int, y:int, z:int)->None:
        """add_block:
            * add block to scene in ursina
            * add block to dataframe
        
        Args:
            block (str): type of the block 
            x (int): X-Position
            y (int): Y-Position
            z (int): Z-Position
        
        Return:
            None
        
        Test:
            * created correct block
            * added block to dataframe
            * position of new block is correct
        """
        
        self.__df_world.loc[len(self.__df_world.index)] = [x,y,z,block]
        # TODO: implement functionality
        # - add to game engine
        pass
    
    # TODO: implement functionality
     # - delete from game engine
    def destroy_block(self,x:int, y:int, z:int)->None:
        """destroy_block:
            * destroy one block
            * delete block from dataframe
        
        Args:
            x (int): X-Position
            y (int): Y-Position
            z (int): Z-Position
        
        Return:
            None
        
        Test:
            * is block deleted from dataframe
            * is blocked deleted from game-engine
        """
        self.__df_world.drop(self.__df_world[(self.__df_world["x"] ==  x) & (self.__df_world["y"] ==  y) &  (self.__df_world["z"] ==  z)].index, inplace=True)
        pass
    
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
    def load_world(self)->None:
        """load_world:
            * load data from database
            * create world from the data
        
        
        Return:
            None
            
        Test:
            * #TODO: Add test
            * #TODO: Add test
        """
        pass
    
    def print(self)->None:
        print("Your world look like:")
        print(self.__df_world)
    


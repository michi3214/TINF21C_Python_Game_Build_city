"""
This is the class for My_Player.
    * create one player
    * set camera view to FirstPersonController
    * add hand 

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 01.05.2023
    Version 1.0.0
    license: MIT
"""
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *
from loguru import logger




class My_Player(Entity):
    """class My_Player:
        * create first person controller
        * add animation for hand
    
    Test:
        * Can be initialized
        * Arm is displayed correctly
    """
    def __init__(self,position, parent=scene):
        super().__init__(parent=parent)
        
        logger.info("Player is initialized")
        self.my_player = FirstPersonController(position=position, jump_height = 1)
        self.my_arm = My_Arm(parent=self.my_player)
     
     
     
     
    def destroy(self):
        """destroy:
            * wrapper for destroy
            * destroy arm
            * destroy player
        
        
        Return:
            None
        
        Test:
            * was the arm destroyed
            * was the FirstPersonController destroyed
        """
        destroy(self.my_arm)
        destroy(self.my_player)
        destroy(self)
    

    
        
class My_Arm(Entity):
    """My_Arm:
        * create arm animation
        * implement function to move arm
    
    Test:
        * can be initialized
        * arm is displayed as expected
    """
    __PASSIV_POSITION =  Vec2(0.7,-0.6)  
    __ACTIVE_POSITION =  Vec2(0.3,-0.5) 
    
    
    
    
    def __init__(self, parent):
        super().__init__(
            parent  = camera.ui,
            model   = "assets/arm",
            texture = "assets/arm_texture.png",
            scale   = 0.2,
            rotation= Vec3(150,-10,0),
            position= self.__PASSIV_POSITION
        )
    
    
    
    
    def use_hand(self)->None:
        """use_hand:
            * change position of hand by using
        
        Return:
            None
        
        Test:
            * did the position changed correctly 
            * no more tests (only setter)
        """
        self.position = self.__ACTIVE_POSITION
    
    
    
    
    
    def passiv_hand(self)->None:
        """passiv_hand:
            * move hand to normal position after use 
        
        
        Return:
            None
        
        Test:
            * did the position changed correctly 
            * no more tests (only setter)
        """
        self.position = self.__PASSIV_POSITION
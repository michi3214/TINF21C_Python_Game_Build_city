"""
This is the class for My_Player.
    * create one player
    * set camera view to FirstPersonController

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 01.05.2023
    Version 1.0.0
    license: MIT
"""
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import *



class My_Player(Entity):
    def __init__(self) -> None:
        super().__init__(
            parent = camera.ui,
            model = "assets/arm",
            texture = "assets/arm_texture.png",
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position=Vec2(0.7,-0.6)
        )
        __my_player = FirstPersonController()
    

    def use_hand(self):
        """use_hand:
            * change position of hand by using
        
        Return:
            None
        
        Test:
            * did the position changed correctly 
            * no more tests
        """
        self.position   =Vec2(0.3,-0.5)
    
    def passiv_hand(self):
        """passiv_hand:
            * move hand to normal position after use 
        
        
        Return:
            None
        
        Test:
            * did the position changed correctly 
        """
        self.position   =Vec2(0.7,-0.6)
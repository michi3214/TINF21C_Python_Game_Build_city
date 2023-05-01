"""
This is the class for My_Voxel and also the specific Voxels.
One Voxel is one block in the world. 
    * create one Voxel
    * handle the design of the Voxel

    Author: Michael Grote
    E-Mail: inf21111@lehre.dhbw-stuttgart.de
    Date: 01.05.2023
    Version 1.0.0
    license: MIT
"""
from loguru import logger
from ursina import *


class My_Voxel(Button):
    def __init__(self, world, position = (0,0,0)):
        self.__world = world
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = load_texture('assets/grass_block.png'),
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5
        )
    
    
    def input(self, key:str):
        """input:
            * handle user interaction with the block
            * destroy this block
            * add new block next to current block 
        
        Args:
            * key (str): used key
        
        Return:
            None
        
        Test:
            * _test1_
            * _test1_
        """
        
        if self.hovered:
            position= self.position + mouse.normal
            if key == "right mouse down":
                self.__world.add_block(position=position, block_type="grass")
            if key == "left mouse down":
                self.__world.destroy_block(position=position)
               
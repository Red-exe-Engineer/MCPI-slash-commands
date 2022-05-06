# Created by Wallee#8314/Red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set the player's position to the 32 bit limit
mc.player.setPos(2**32, 2**32, 2**32)

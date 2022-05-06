Created by Wallee#8314/Red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set the player's position to a really high number
mc.player.setPos(2**32, 2**32, 2**32)

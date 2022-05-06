Created by Wallee#8314/Red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from sys import argv

# Error protection
try:

    # Set the user's position to the arguments the user should provide
    mc.player.setPos(int(argv[1]), int(argv[2]), int(argv[3]))

# Oops, not my fault
except:

    # Tell the user the command failed
    mc.postToChat("Command failed")
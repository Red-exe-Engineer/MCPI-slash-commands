# Created by Wallee#8314/Red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from time import sleep
from sys import argv

# Check if the argument is "yes"
if len(argv) > 1 and argv[1] == "yes":

    # Tell the user how to escape MCPI
    mc.postToChat("Alt + F4 and Alt + Tab can be used to escape")

    # Pause the program for a second
    sleep(1)

    # Set the user's position to the 64 bit limit (an EXTREMELY high number)
    mc.player.setPos(2**64, 2**64, 2**64)

# Else the player may not want to freeze MCPI.
else:
    # Tell the user how to use this command and the dangers of it
    mc.postToChat("WARNING! Hardstop will cause MCPI to stop responding!!")
    mc.postToChat("If you wish to continue add a \"yes\" argument.")

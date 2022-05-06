# Created by Wallee#8314/Red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from time import sleep
from sys import argv

# Check if an argument was giving
if len(argv) > 1:

    # If the argument is yes
    if argv[1] == "yes":

        # Tell the user how to escape MCPI
        mc.postToChat("Alt + F4 and Alt + Tab are good")

        # Pause the program for a second
        sleep(1)

        # Set the user's position to a REALLY high number
        mc.player.setPos(2**64, 2**64, 2**64)

    # Else the argument wasn't yes
    else:

        # Tell the user the argument MUST be yes
        mc.postToChat("Hardstop will only work with a \"yes\" argument")

# Else no arguments were giving
else:

    # Tell the user how to use this command and the dangers of it
    mc.postToChat("WARNING! Hardstop will cause MCPI to stop responding!!")
    mc.postToChat("If you wish to continue add a \"yes\" argument")

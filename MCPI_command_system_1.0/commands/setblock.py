# Created by Wallee#8314/Red-exe-Engineer

""" WORK IN PROGRESS """

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from items import *
from sys import argv

# Error protection
try:

    # Set the command to... Uh... Magic! Yeah this was code stripped from an older buil...
    command = "setblock " + f'{argv[1]} {argv[2]} {argv[3]} {argv[4]}'

    # Get the players coordinates
    x, y, z = mc.player.getPos()

    # Get the coordintates the player wants set the block at
    sx, sy, sz, block = command[9:].split(" ")

    # Set the block ID to whatever the user said it should be by name (returns None if the block is now known)
    blockID = getBlockID(block)

    # Work in progress
    sx = sx.replace("~", str(x).split(".")[0])
    sy = sy.replace("~", str(y).split(".")[0])
    sz = sz.replace("~", str(z).split(".")[0])

    # Check if the block ID is None
    if blockID == None:

         # Set the block ID to block, may cause an error
         blockID = int(block)

    # Set the block
    mc.setBlock(int(sx), int(sy), int(sz), blockID)

# I told you "work in progress"
except:

    # Try more stuff that can cause errors
    try:

        # Tell the user something went wrong
        mc.postToChat(f'Could not set block "{block}" at {sx} {sy} {sz}')

    # Oops
    except:

        # Tell the user something went terribly wrong
        mc.postToChat("Command failed")

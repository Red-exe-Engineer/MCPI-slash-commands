# Created by Wallee#8314/Red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from sys import argv

# Tell the user this is a buggy command
mc.postToChat("Settings are weird so this may not work")

$ Try something that I don't know will cause an error
try:

    # Set the setting to whatever the user said
    mc.setting(argv[1], bool(argv[2].capitalize()))

# Oops, I don't work much with mc.setting()
except:

    # Tell the user the command failed
    mc.postToChat("Command failed")

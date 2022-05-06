# Created by Wallee#8314/Red-exe-Engineer

"""
    Example plugin to show how to make them

    RULES:
     Names must be lowercase and should only use a-z and underscores
     Names must also end with .py and must not be a hidden file, reason is so plugins can make directories that wont look like a plugin to the MCPI command code
     If a plugin starts with an underscore it will be ignored
     Please put your name and or alias at the top of the plugins code
     Comment stuff well, it is usefull for those who do not know how to make plugins
     Any plugin made may cause an error, to avoid fatal errors use try and except statements around most of your code

    INFO:
     The file name is what the command will be
     To debug an error look at terminal output, the reason stuff is posted to chat is so you know to look there
     Plugins are check first, this means commands start a bit slower but you *can* override them
     Modifying a plugin does not mean you have to restart your game :)
     Please do NOT modify commands, copy them into the plugin folder instead
"""

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Argv will allow for system arguments, like a terminal program :p
from sys import argv

# Print argv to terminal
print(argv)

# Say hello world to chat
mc.postToChat("Hello World!")

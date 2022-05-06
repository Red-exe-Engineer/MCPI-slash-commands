# Created by Wallee/red-exe-Engineer

# Imports
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from os import listdir
from sys import argv

# Set search to an empty string
search = ""

# Set plugins to the contents of the plugins directory
plugins = listdir("plugins")

# Remove helper files (files starting with an underscore)
plugins = [plugin for plugin in plugins if not plugin.startswith('_')]

# Check if any arguments were giving
if len(argv) > 1:

    # If yes then set search to the first one (plugings cannot have spaces anyways)
    search = argv[1]

# Set text to an empty string
text = ""

# Loop through the plugins
for plugin in plugins:

    # Check if the plugin isn't items.py (importable module for commands/plugins)
    if plugin != "items.py" and search in plugin:

        # Add the plugin to text
        text = text + plugin.replace(".py", "") + " "

# Check if text is blank
if text == "":

    # Check if search is blank
    if search == "":

        # Tell the user they do not have any plugins installed
        mc.postToChat("You have no plugins installed :(")

    # Else a search was giving
    else:

       # Tell the user the search term didn't bring any results
       mc.postToChat(f'No plugins were found that contain "{search}"')

# Else some plugins were found
else:

    # Post text to MCPI
    mc.postToChat(text)

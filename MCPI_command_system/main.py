# Created by Wallee#8314/Red-exe-Engineer

""" Version 1.0 """

# Imports
import subprocess
from os import listdir

from mcpi.minecraft import Minecraft
from commands.items import *

import subprocess

# Define a process to capture chat messages
def capture(exe):

    # Use subprocess to link the games output to a variable
    game = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Repeat until "break" is executed
    while True:

        # Get a message
        message = game.poll() 

        # Read the line
        line = game.stdout.readline()
        
        # Yield the line
        yield line

        # Check if message is not None
        if message is not None:

            # Break the loop
            break

# Define a method to run commands and plugins
def command(command):
    
    # Define a variable to store the commands name
    command_name = command.split(" ")[0]

    # Check if the command is in the plugins folder, the reason I check plugins first is so they *can* override default commands
    if command_name + ".py" in listdir("plugins") and not command.startswith("_"):

        # The plugin might be in development and have errors/bugs
        try:

            # Set args to the arguments the user provided
            args = command[len(command_name):]

            # Run the plugin through a subprocess
            subprocess.run(args = f'python3 plugins/{command_name}.py {args}', shell=True, check=True)

        # An error occurred
        except Exception as error:

            # Post some error info to chat
            mc.postToChat(f'Fatal error in {command_name} plugin!')
            mc.postToChat("Check the terminal output for a traceback")

    # Check if the command is in the commands folder
    elif command_name+".py" in listdir("commands"):

        # Still use a try and except statement even though all command files should already use one
        try:

            # Set args to the arguments the user provided
            args = command[len(command_name):]

            # Run the command through a subproess
            subprocess.run(args = f'python3 commands/{command_name}.py {args}', shell=True, check=True)

        # Oops, wasn't me
        except:

            # Tell the user the command wans't executed correctly
            mc.postToChat("Something went wrong 0_0")

    # Else the cammand is unknown
    else:

        # Tell the user that command doesn't exist
        mc.postToChat(f'Command "/{command_name}" doesn\'t exist')

# Repeat capture and start MCPI
for line in capture("minecraft-pi-reborn-client"):

    # Set the info message
    info = line[5:11]

    # Check if the info type was chat
    if info == b"[CHAT]":

        # Set the content to whatever the user said
        content = str(line[13:-5])[2:-1]

        if content.startswith(f'<{name}> /'):
            mc = Minecraft.create()
            command(content.split(f'<{name}> /')[1].lower())

    # Else if info is an error
    elif info == b"[ERR]:":

        # Correct the info name
        info = "[ERR]"

        # Set content to the error message
        content = str(line[16:-1])[2:-1]

    # Else set content to the content of the line
    else:

        # Set content to a minipulated version of the line
        content = str(line[17:-1])[2:-1]

    # Check if the info type is INFO
    if info == b"[INFO]":

        # Check if content starts with Setting Username:
        if content.startswith("Setting Username: "):

            # Set name to the name the user chose
            name = content.split("Setting Username: ")[1]

    # Print info and content
    print(str(info)[2:-1], content)

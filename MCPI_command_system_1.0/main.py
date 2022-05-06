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

    # Repeat for a long time
    while True:

        # Get a message
        message = game.poll() 

        # Read and yield stuff
        line = game.stdout.readline()
        yield line

        # Check if message is not None
        if message is not None:

            # Break the loop
            break

# Define a method to run commands and plugins
def command(command):

    # Check if the command is in the plugins folder, the reason I check plugins first is so they *can* override default commands
    if command.split(" ")[0] + ".py" in listdir("plugins") and not command.startswith("."):

        # The plugin may be in development and has a lots of errors/bugs
        try:

            # Set args to the arguments the user provided
            args = command[len(command.split(" ")[0]):]

            # Run the plugin through a subprocess
            subprocess.run(args = f'python3 plugins/{command.split(" ")[0]}.py {args}', shell=True, check=True)

        # Someone is a bad coder 0_0 (We all make mistakes)
        except Exception as error:

            # Post some error info to chat
            mc.postToChat(f'Fatal error in {command.split(" ")[0]} plugin!')
            mc.postToChat("Check terminal output for a traceback")

    # Check if the command is in the commands folder
    elif command.split(" ")[0]+".py" in listdir("commands"):

        # Still use a try and except statement even though all command files should already use one
        try:

            # Set args to the arguments the user provided
            args = command[len(command.split(" ")[0]):]

            # Run the command through a subproess
            subprocess.run(args = f'python3 commands/{command.split(" ")[0]}.py {args}', shell=True, check=True)

        # Oops, wasn't me
        except:

            # Tell the user the command wans't executed correctly
            mc.postToChat("Something went wrong 0_0")

    # Else the cammand is unknown
    else:

        # Tell the user that command doesn't exist
        mc.postToChat(f'Command "/{command.split(" ")[0]}" doesn\'t exist')

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

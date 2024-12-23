# Poke-Nexus-Farmer
This script combines the functionality of simulating WASD key presses and mouse clicks. Here's how it works:

WASD Loop: This loop alternates between pressing and releasing the W and S keys. You can start and stop this loop by pressing the P key.

Mouse Click Loop: This loop continuously clicks the left mouse button. It starts when you right-click and stops when you left-click.

Program Termination: The entire program can be terminated by pressing the Q key.

How to Use this Program on Poke Nexus MMO/Website
Setup:

Ensure you have the required libraries installed:

In Cmd
pip install pyautogui pynput
Running the Program:

Copy the provided script into a .py file (e.g., automation_script.py).

Run the script using Python:

In Cmd
python automation_script.py
Using the Script:

Start/Stop WASD Loop: Press the P key to start or stop the WASD loop. The script will print "WASD loop started" or "WASD loop stopped" to indicate the current state.

Start Mouse Click Loop: Right-click to start the mouse click loop. The script will print "Mouse clicking started."

Stop Mouse Click Loop: Left-click to stop the mouse click loop. The script will print "Mouse clicking stopped."

Quit Program: Press the Q key to terminate the program.

Application in Poke Nexus MMO:

The WASD loop can be used to automate movement in the game by simulating the W and S key presses.

The mouse click loop can be used to automate continuous clicking actions, which might be helpful for repeated interactions in the game.

Example Use Case:
Let's say you want to move your character back and forth while continuously interacting with an object in the game. Here's what you would do:

Start the Script: Run the script as described above.

Start WASD Loop: Press the P key to start the WASD loop. Your character will now move back and forth.

Start Mouse Click Loop: Right-click to start the mouse click loop. Your character will now continuously interact with objects.

Stop Actions: You can stop the WASD loop by pressing the P key again, and you can stop the mouse click loop by left-clicking.

Terminate the Script: Press the Q key to end the script when you're done.

NOTE:- Run This Python File From Cmd Prompt And Have The Following Command Pip Installed.

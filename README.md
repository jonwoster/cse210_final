# Alien Invasion Game for CSE 210
# Status: in progress
# Description:
Alien Invasion involves aliens descending from the sky and the player can shoot the them, trying to kill them all before they reach the ground. This project was created for the CSE 210 final project at BYU Idaho.

# Project Structure:
greed: folder housing all the parts for the game and where the __ main__.py and game design file live.
__ main__.py: contains our main function utilizing the classes in different files and builds the game window definitions for video_service.py to use in drawing the game.
game: a folder containing the files for the game to run.
casting: a folder containing the files for the to create the different interactive pieces of the game.
directing: a folder containing the files to direct the game including director.py.
services: a folder containing the files that show and receive information from the user.
shared: a folder containing the utility files for the any class to use in the game.
director.py: a file containing all info relating to the "Director" class.
keyboard_service.py: a file that intereprets user's keyboard input using the "KeyboardService" class.
video_service.py: a file that draws the game window and shows the user any information they need using the "VideoService" class.
point.py: a file containing all info relating to the "Point" class.
color.py: a file containing all info relating to the "Color" class.
actor.py: a file containing all info relating to the "Actor" class.
artifact.py: a file containing all info relating to the "Artifact" class.
cast.py: a file containing all info relating to the "Cast" class.

# Technologies Used:
- The only software required for this program is Python. You can download it here: https://www.python.org
- The collaboration was done via github: https://github.com/jonwoster/cse210_final

# How to Start:
Open __ main__.py file using python 3.

# Game Instructions:
- The objective is to shoot and destroy the aliens before the reach the ground (bottom of the screen)
- If any aliens (shown as "H" characters) reach the bottom of the screen, the game is over and the player loses
- If the player is able to eliminate all the aliens from the sky, the game is over and the player wins
- The player is at the bottom of the screen, shown as a "#"
- Player can only move left or right by using keyboard left and right arrow buttons
- Player can shoot bullets one at a time or continuously by hitting or holding down the keyboard space bar

# Acknowledgements:
- Camron Erickson: eri20010@byui.edu
- Monika Meyers: nikasparks@mac.com
- Arnaldo Suarez: sua21007@byui.edu
- Wylee Everett: eve20003@byui.edu
- Jonathan Woster: jonathanwoster@gmail.com

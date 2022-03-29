# Alien Invasion Game for CSE 210
## Status: in progress
## Description:
Alien Invasion involves aliens descending from the sky and the player can shoot the them, trying to kill them all before they reach the ground. This project was created for the CSE 210 final project at BYU Idaho.

## Project Structure:
### aliens (folder)
- The aliens folder holds all the parts for the game and it is where the __ main__.py and constants.py files are.
- __ main__.py contains our main function utilizing the classes in different files and builds the game window definitions for video_service.py to use in drawing the game.
- constants.py contains various constants so aspects like screen size, frame rate, number of rows of aliens, etc. can be easily modified.
- Within the aliens folder, there is also the game folder
### game (folder)
The game folder containing the additional folders that comprise the game. It contains the items below:
- casting (folder):  containing the files for the to create the different interactive pieces of the game.
  - actor.py contains the Actor class
  - alien.py contains the Alien class
  - bullet.py contains the Bullet class
  - cast.py contains the Cast class
  - player.py contains the Player class
  - score.py contains the Score class
- directing (folder): containing the files to direct the game including director.py.
  - director.py: a file containing all info relating to the "Director" class.
- scripting (folder): containing the files that are files that are part of the game script
  - action.py: Contains the Action class
  - control_actors_action.py: Contains the Control_actors_action class
  - draw_actors_action.py: Contains the Draw_actors_action class
  - handle_collisions_action.py: Contains the Handle_collisions_action class
  - move_actors_action.py: Contains the Move_actors_action class
  - move_bullets_action.py: Contains the Move_bullets_action class
  - script.py: Contains the Script class
- services (folder): containing the files that show and receive information from the user.
  - keyboard_service.py: a file that intereprets user's keyboard input using the "KeyboardService" class.
  - video_service.py: a file that draws the game window and shows the user any information they need using the "VideoService" class.
- shared (folder): contains utility files shown below
  - point.py: a file containing all info relating to the "Point" class.
  - color.py: a file containing all info relating to the "Color" class.
- sounds (folder): containing sound (WAV) files

## Technologies Used:
- The software required for this program is Python. You can download it here: https://www.python.org
- The raylib library is needed as well.
- The collaboration was done via github: https://github.com/jonwoster/cse210_final

## How to Start:
Open __ main__.py file using python 3.

## Game Instructions:
- The objective is to shoot and destroy the aliens before the reach the ground (bottom of the screen)
- If any aliens (shown as "H" characters) reach the bottom of the screen, the game is over and the player loses
- If the player is able to eliminate all the aliens from the sky, the game is over and the player wins
- The player is at the bottom of the screen, shown as a "#"
- Player can only move left or right by using keyboard left and right arrow buttons
- Player can shoot bullets one at a time or continuously by hitting or holding down the keyboard space bar

## Acknowledgements:
- Camron Erickson: eri20010@byui.edu
- Monika Meyers: nikasparks@mac.com
- Arnaldo Suarez: sua21007@byui.edu
- Wylee Everett: eve20003@byui.edu
- Jonathan Woster: jonathanwoster@gmail.com

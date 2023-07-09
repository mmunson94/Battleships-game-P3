# Battleships Python Project 3
Battleships is a Python terminal game, which runs on the Github Terminal on Heroku

In this game, the user will attempt to find the AI's ships that have been randomly generated
Each ship occupies one place on the board

Here is the link to the live project: https://battleships-p3-mmunson-bdc488326124.herokuapp.com/

<img width="1440" alt="Screenshot 2023-07-09 at 22 23 48" src="https://github.com/mmunson94/Battleships-game-P3/assets/114744383/879015a2-f114-42f8-996f-a3bdf0536bb8">

#

## How the game works

Battleships is based on the classic game of the same name.
In this iteration the user shall attempt to sink 5 of the computers 
ships with the amount of turns dependent on what difficulty the 
user decides to play on. Users misses are marked by '-' on the board 
and alternatively, hits are marked by 'X'.


## Features
   ### Current Features
   * Random Generated Computer Board
Ships are randomly generated on a hidden board in which the user must try to locate

   * Menu
A menu has been implemented for good UX which allows the user to select difficulty and use their name

<img width="740" alt="Screenshot 2023-07-09 at 23 54 02 1" src="https://github.com/mmunson94/Battleships-game-P3/assets/114744383/f663c2ef-8230-4ac7-a193-834f1d63cb60">

#

The Board is consistenly updated with users coordinates

Input validation has been put in place to ensure user input is correct therefore, the user cannot
enter inputs outside the games parameters and the users is notified if they have entered the same 
coordinates more than once

A restart feature has also been set up, so users can choose to play again if they choose

   ### Future Features
* Different sized ships
* User can chose to use one nuke a round that can hit multiple coordinates in one turn
* User can choose to play against another user


## Data Model
The model I chose to use for my game was a Board class. the game creates two boards, one for the computer which is hiden from the user that has the randomly genered coordinates that the user must guess and the other for the user to see the coordinates they have plotted.

The Board class will store all the relevant data which includes BOard size, ship coordinates, the number of ships, the users guesses and the number of turns the user has.

In order to play the game, the class uses methods such 'print' which shows the user the current Board, the methods 'plot_coordinates' to determine what the user has guessed and the result and the method 'plot_ships' to randomly generate the ships on the hidden AI Board.

## Testing
In order to test the validy of my code, I have done the following:
* Used PEP8 Linter to run the code and confirm no problems
* Attempted to crash my game by typing incorrect inputs and have ensured no errors occured
* Have run the game through both the Github terminal and the Heroku App and ensured no bugs occurred

## Bugs
Corrected Bugs
* I had a bug where the name and turns werent showing, in order to fix this I made them both a global variable
* I had a bug where the screen wouldnt refresh when restarting the game, I fixed this by implementing the Start_game() function 

Remaining Bugs
* No bugs remaining

Validator Testing
* No errors occured when running the code through the PEP8 Online programme

## Deployment
This project was deployed using Code Institue's mock terminal for Heroku

Steps for deployment:
* Create a new Heroku app
* Set buildbacks to 'python' and 'NodeJS' and then create Config Var called PORT. Set this to 8000.
* Link your github repository to Heroku app
* Clck Deploy

## Credits
* https://scaler.com/topics/how-to-clear-screen-in-python for the clear screen function
* https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-string-formatting for the formatting of rows and columns in the board
* https://www.youtube.com/watch?v=rfscVS0vtbw&ab_channel=freeCodeCamp.org
* Code Institute love sandwiches project

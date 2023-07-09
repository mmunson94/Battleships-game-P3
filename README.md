# Battleships Python Project 3
Battleships is a Python terminal game, which runs on the Github Terminal on Heroku

In this game, the user will attempt to find the AI's ships that have been randomly generated
Each ship occupies one place on the board

Here is the link to the live project: https://battleships-p3-mmunson-bdc488326124.herokuapp.com/


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

Board is consistenly updated with users coordinates

Input validation has been put in place to ensure user input is correct therefore, the user cannot
enter inputs outside the games parameters and the users is notified if they have entered the same 
coordinates more than once

A restart feature has also been set up, so users can choose to play again if they choose

   ### Future Features
* Different sized ships
* User can chose to use one nuke a round that can hit multiple coordinates in one turn
* User can choose to play against another user


## Data Model

## Testing

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

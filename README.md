# Battleships

## Introduction

For my Python essentials project, I chose to take another crack at a battleship game, after having unsuccessfully pursued that avenue for the JavaScript project.  Using python, I have deployed my code to a Heroku app, on which a simple version of battleship can be played against the computer.  
The user will try to beat the CPU by finding all the battleships first. Each battleship is in a 1x1 spot on the board.

A live version of the game can be found [here](livelink).

![project preview](finishedsiteimage)

## Strategy

### Project Goals

My main objective was to use python to create a functional battleship game, slightly immersive so that the user stays entertained and robust enough to handle user error.  The user plays against the computer, who guesses ship locations at random.  

### User Goals:

First Time Visitor Goals
- First time visitors can easily learn the rules of the game.
- First time visitors should be able to interact with the UI easily enough that they can see a game through to the end without complication.  
- First time visitors would look to play the game to beat the computer. 
Returning Visitor Goals
- Returning visitors will look to beat the computer. 
- Returning visitors should check in to see if new features have been added.  
- Returning visitors could return to the game as an introduction to others, showing where a functional battleship game can be found online.  

### User Expectations:

- The game should trigger automatically
- The rules of the game should be clearly explained
- The instructions the user receives should be easy to understand and follow
- The game should clearly display how much time remains, and declare a winner and loser if one side wins

## Structure

Below is a diagram showing the logic and possibilities for this game.

![project diagram](diagram)

## How to play

- Battleships is a simple board game that requires 2 players to play. In this case, the user plays against the CPU, who is at times referred to as "the enemy"
- The user first hides all 4 of their own ships, assigning them locations through choosing a row and column. 
- If the user tries to hide two ships on the same tile, one of the two is assigned a random tile instead.  
- The user then is prompted to start the guessing and is shown an empty board.  
- The user guesses a specific row and column in which the enemy ship might be.  
- After the user guess, the computer takes a randomly generated guess against the locations in which the user hid their boats at the beginning.  
- If either user or computer hits, a counter for their score is increased by 1. The user is then prompted to guess again unless the game has ended.   
- If either player gets a score count of 4, they have won, and the game ends, with an announcement declaring the winner.  
- Otherwise, there are 24 turns total in the game, after which point the game ends in a draw.  

## Features

### Existing Features
- Random computer ship generation
 - The computer ships are generated randomly onto the board, using randint. 
 - On a board the user cannot see, these locations are marked with an X.  User guesses are checked against this hidden board.  
- Accepts user input for ship locations, and guess locations
- Each player has 4 ships to hide, thus 4 enemy ships to attempt to sink.  
- The updated guess board is shown after each user guess, assuming the game hasn't ended
- Win, loss, and draw messages are in place, paired to each of their corresponding situations should either side win, or should time expire.  


![game_turn1](documentation_assets/images/game_turn1.png)

- Input validation
    - When setting locations or guesses, the only acceptable inputs are a number between 1-7 for a row and a letter between A-G for the column. 
    - If either input is not within it's respective acceptable ranges, a message is printed declaring the input invalid, and the user is asked to re-enter until their choice is within the desired range
    - If a player tries to place two ships on the same tile, one ship is assigned to another random unoccupied location instead
    - If a player tries to guess a tile already guessed, they are informed that they have already guessed that location, and asked to guess again without missing a turn. 
### Possible Future Features
 - Varying sizes of ships
 - Option to play versus a second human player
## Testing

I have manually tested this project by the following:
- Entered incorrect inputs into the terminal to make sure the correct warning messages are appearing
- Tested the game logic/flow, and played the game through in the terminal
- Tested the project on Heroku
### Embedded Testing
The most effective way I found for solving syntactic errors in my code was through the problems tab that appears to the left of the terminal. In this tab I could identify errors as they appeared, and move to fix them before even testing the code by running it or copying it through a validator.  This embedded testing and debug function was the front line of repairing the errors in my code. An example of the errors as they appear in the problems section is below.

Embedded test image

### Bugs
#### Solved Bugs
- Solved the bug of lines being too long in code by, in several instances, starting what was once the same line of code on the next line instead
- Solved a bug where it was impossible to check for both repeat location assignment and valid input for the location of ships, by changing the former check to be within 4 separate while loops at the bottom of the ship assignment function
### Remaining Bugs
- A minor bug remains--if by some small chance the computer and player win at exactly the same time, there is no contingency message, and the game simply displays that the player won, and the computer won.  
- The following problems remain confusing to me, and unresolved. 
image of problems
### Validator Testing
- [PEP8](http://pep8online.com/)
I ran the code through the PEP8 validator. I initially ran into a few issues, as you can see in the image below:
[![python_validator_errors](documentation_assets/images/python_validator_errors.png)](documentation_assets/images/python_validator_errors.png)

However, these issues were rectified by adding white spaces around operators and starting new lines of code as the line was too long. 
[![python_validator_errors](documentation_assets/images/pep8_no_errors.png)](documentation_assets/images/pep8_no_errors.png)

## Deployment
I used Heroku to deploy my final project to the cloud. To do this I had to:

1. Push all latest code to GitHub.
2. Go to [Heroku](https://dashboard.heroku.com/apps)
3. Select new in the top right corner.
4. Create new app.
5. Enter the app name and select Europe as the region.
6. Connect to GitHub.
7. Search for repo-name.
8. Select connect to the relevant repo you want to deploy.
9. Select the settings tab.
10. Add buildpack
11. Select Python, then save changes.
12. Select Nodejs, then save changes.
13. Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs
14. Navigate to the deploy tab
15. Scroll down to Manual Deploy and select deploy branch.
## End Product

Please find below some screenshots of the finished project:

User misses shot:
![user missed shot](documentation_assets/images/user_missed.png)

Computer misses shot:
![cpu missed shot](documentation_assets/images/cpu_missed.png)

User sunk first CPU ship:
![user guessed first ship](documentation_assets/images/user_guessed_first_ship.png)

Too many incorrect guesses:
![too many incorrect guesses](documentation_assets/images/game_over_incorrect_guesses.png)

User wins game:
![user wins game](documentation_assets/images/game_win.png)

## Credits

- GitHub Python Template [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template)
- Heroku deployment instructions from Code Institute
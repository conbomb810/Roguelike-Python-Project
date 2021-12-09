:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Roguelite Dungeon
## CS 110 Final Project
### Fall, 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

<< [https://github.com/<repo>](#) >>

<< [link to demo presentation slides](#) >>

### Team: Middle Team
#### << Middle team >>

***

## Project Description *(Software Lead)*
<< our project will be a dungeon game that will include randomized enemies and a single hero that can be customized by choosing a different kit/class.>>

***    

## User Interface Design *(Front End Specialist)*
* The interface consists of 5 screens: A main menu, where the player starts the game. A class select menu, where the player selects their class. A battle screen, where the player actually plays the game and battles various enemies. A game over screen for when the play lose, and a victory screen for when the player wins. The following images are the concept art of the interfaces.
![name-of-you-image](https://github.com/bucs110b1fall21/final-project-middle-team/blob/master/assets/Snapchat-569155497.jpg)
![name-of-you-image](https://github.com/bucs110b1fall21/final-project-middle-team/blob/master/assets/Snapchat-174583180.jpg)
* The followiing images are the final depiction of the GUI
![name-of-you-image](https://github.com/bucs110b1fall21/final-project-middle-team/blob/master/assets/mainmenu.png)
![name-of-you-image](https://github.com/bucs110b1fall21/final-project-middle-team/blob/master/assets/classmenu.png)
![name-of-you-image](https://github.com/bucs110b1fall21/final-project-middle-team/blob/master/assets/battlemenu.png)
![name-of-you-image](https://github.com/bucs110b1fall21/final-project-middle-team/blob/master/assets/gameovermenu.png)
![name-of-you-image](https://github.com/bucs110b1fall21/final-project-middle-team/blob/master/assets/victorymenu.png)

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
  Pygame
https://www.pygame.org/docs/
Pygame is a free set of python modules designed for writing video games. It allows programmers to create full fledged video games on nearly any platform.

Random
https://docs.python.org/3/library/random.html
This module allows programmers access to a pseudo-random number generator. When working with integers, they are randomly selected from a range. Other elements are randomly selected from a list or dictionary.

* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * Button
The button the player clicks to complete actions, to start the game, to quit, and to play the game in general
-Dialogue box
This where anything said to the player or between characters is displayed
-Health Bar
This displays the status of the player’s health
-Controller
Creates and adds functionality to the menus and the battles. Allows the player to fight different enemies with a hero of their choice, while tracking their score, and displaying a victory or defeat screen at the end of the battle.
-Hero
Creates the hero object and gives them their attributes like health and damage
-Monster
Creates the monster object and gives them their attributes like health and damage 
-Highscore
Tracks the highest score a player achieves 
-Score
Tracks the score the player accrues throughout the game
-Manabar
Displays the status of the player’s mana


## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - << Conner Smith >>

<< Worked as integration specialist by heavily modifying the sprite classes to fit in the controller and writing aditional functions inside to improve frontend efficiency. Also communicating between backend and frontend to see what minor problems arise and modifying /writing code they might.  >>

### Front End Specialist - Connor Meybohm

As the Front End Specialist, I did significant research on pygame in general. I specifically delved into everything about the controller class, such as sprites, mixers, sprite groups, and events. I also did a good portion of backend work to make sure the models worked with the controller class. I also did a large amount of research in json formatting and the json module in order to properly use them in both the controller and the highscore.py class.

### Back End Specialist - Adejo Ibrahim

<< As the Back End Specialist, I did the initial coding of the models and made sure they worked as intended. I created the files for each model and helped the frontend with any problems within the code. >>

## Testing *(Software Lead)*
* << In our testing we went about it by starting out with the basics of the game and getting the sprite classes we would need. This allowed would allow us to create out event loops more efficiently and add stuff slowly. Our first test was to make sure the sprites were working correctly and we hardcoded the values needed so we could test the basics of our code. After each essential function added, we could implemented a main into that could be called to test the class was working correctly. We would do this many times while we were coding to make sure we were on the right track. Slowly we implemented the controller class to call the additional classes and make sure they would work properly. >>
    * << while creating the hero class and its functions like the healthbar and attack, a main was implemented to make a small test GUI window that the sprite was then created on. In addition to that the update function for health bar based on damage recieved by a hardcoded value. This ensured that the hero class would properly work for the controller method to make my teammates work more efficiently. >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Start Menu  | a 1280 x 720 window is created in GUI window  | a 1280 x 720 window is created in GUI window         |
|  2  | background created for start menu  | GUI window has game background | GUI window has game background
|3    | 2 sprites created | start button and quit button are displayed in GUI | start button and quit button are displayed in GUI
|4 | start button sprite is clicked | Class menu loop is initiated, and window for selection is displayed on GUI window | gives user choices of classes for their character to be |
|5 | class is chosen | the class chosen will read in the values from JSON file for the stats of the hero | the class chosen will read in the values from JSON file for the stats of the hero
|6 | health bar is displayed | health bar for charcter will then be displayed on GUI using health bar class | health bar does not appear on GUI |
|7 | Battle loop initiated | controller creates the hero and monster sprite based on the values and image given by reading in file | controller creates the hero and monster sprite based on the values and image given by reading in file
|8| battle loop initiated | 1st round of monster will be spawned, once health of monsters = 0, next round commences | 1st round of monsters is spawned but next round will not start.
|9 | hero attck | hero attacks using attack function in hero class to damage monster sprite based on move selection which has different values and attacks for each class| Hero can only use one attack and it is automatically chosen |
| 10 | enemy attack | enemy will attack after hero has attacked and deals random amount of damage, using attack function in monster class | enemy can only use one attack  and it is automatically chosen |
| 11 | healthbar update | health bar is updated based on remaining health then displayed on GUI window | health bar is updated based on remaining health then displayed on GUI window
|12 | battle loop runs | if health of hero or monster is greater then zero, then battle will runs again and attacks are chosen again | if health of hero or monster is greater then zero, then battle will runs again and attacks are chosen again 
|13 | Health status | if characters health bar is 0, gameover loop will commence. If health of monsters is 0, next round will start. | gameover loop displays game over screen and asks to play again. When monster health is 0 GUI window displays "victory" and advances to next round | gameover loop displays game over screen and asks to play again or quit. When monster health is 0 GUI window displays "victory" but doesn't display on GUI window the next round of enemies.
| 14 | run score | if monsters health is less than zero, then score will increase by set amount and bonus socre is applied based on amount of health hero still has and displays in GUI window. If hero health less than 0, then final score is shown on GUI window during victory loop.
|14| game over | GUI window screen is deleted and program ends| GUI window screen is deleted and program ends
etc...

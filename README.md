:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Roguelite Dungeon
## CS 110 Final Project
### Fall, 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

<< [https://github.com/<repo>](#) >>

<< [](#) >>

### Team: Middle Team
#### Middle team 

***

## Project Description *(Software Lead)*
 our project will be a dungeon game that will include randomized enemies and a single hero that can be customized by choosing a different kit/class. It will include different rounds that have different enemies

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
  
         ![class diagram](https://github.com/bucs110b1fall21/final-project-middle-team/blob/master/assets/IMG-4572.jpg)
* Classes

- Button
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
    *button.py
      healthbar.py
      info.json
      controller.py
      hero.py
      manaBar.py
      dialoguebox.py
      HighScore.json
      sample_controller.py
      highscore.py
      monster.py
      score.py 
* assets
    *battleBackground.jpg
      gameovermenu.png
      OniDead.png
      battlemenu.png
      bossDead.png
      monsterDead.png
      samaraiSmall.jpg
      boss.png
      monsterSmall.png
      Snapchat-174583180.jpg
      Snapchat-569155497.jpg
      classmenu.png
      moveBox.png
      tempHighScore.jpg
      dialogueBoxNew.png
      muramasaTheme.mp3
      victorymenu.png
      ninja.png
* etc
    * <.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead -  Conner Smith 

Worked as integration specialist by heavily modifying the sprite classes to fit in the controller and writing aditional functions inside to improve frontend and backend efficiency. Also communicating between backend and frontend to see what minor problems arise and modifying writing code they might need in order to work more efficient together. 

models:
score.py
hero.py
monster.py
healthBar.py

### Front End Specialist - Connor Meybohm

As the Front End Specialist, I did significant research on pygame in general. I specifically delved into everything about the controller class, such as sprites, mixers, sprite groups, and events. I also did a good portion of backend work to make sure the models worked with the controller class. I also did a large amount of research in json formatting and the json module in order to properly use them in both the controller and the highscore.py class.


models:
controller.py
healthbar.py
hero.py
monster.py
highscore.py
button.py
dialoguebox.py



### Back End Specialist - Adejo Ibrahim


<< As the Back End Specialist, I did the initial coding of the models and made sure they worked as intended. I created the files for each model and helped the frontend with any problems within the code. >>

models:
healthbar.py
manabar.py
dialoguebox.py

## Testing *(Software Lead)*
* In our testing we went about it by starting out with the basics of the game and getting the sprite classes we would need. This allowed would allow us to create out event loops more efficiently and add stuff slowly. Our first test was to make sure the sprites were working correctly and we hardcoded the values needed so we could test the basics of our code. After each essential function added, we could implemented a main into that could be called to test the class was working correctly. We would do this many times while we were coding to make sure we were on the right track. Slowly we implemented the controller class to call the additional classes and make sure they would work properly. 
    *  while creating the hero class and its functions like the healthbar and attack, a main was implemented to make a small test GUI window that the sprite was then created on. In addition to that the update function for health bar based on damage recieved by a hardcoded value. This ensured that the hero class would properly work for the controller method to make my teammates work more efficiently. 

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Start Menu  | a 1280 x 720 window is created in GUI window  | a 1280 x 720 window is created in GUI window         |
|  2  | background created for start menu  | GUI window has game background | GUI window has game background
|3    | 2 sprites created | start button, quit button, and highscore are displayed in GUI | start button, quit button, and highscore are displayed in GUI
|4 | start button sprite is clicked | Class menu loop is initiated, and window for selection is displayed on GUI window | gives user choices of classes for their character to be |
|5 | class is chosen | two classes are presented to the user andeach has different stats that will help in battle | two classes are presented to the user andeach has different stats that will help in battle
|6 | battle screen | health bar, mana bar, move bar, monsters sprite, and hero sprite for charcter will then be displayed on GUI | health bar, mana bar, move bar for charcter will then be displayed on GUI |
|7 | move loop | user chooses between attack, defend, item and action is performed and updates the health of both monster and hero | user chooses between attack, defend, item and action is performed and updates the health of both monster and hero 
|8 | hero attck | hero attacks using attack function in hero class to damage monster sprite based on move selection which has different values and attacks for each class| hero can choose bewteen moves using move buttons|
|9| battle loop initiated | 1st round of monster will be spawned, once health of monsters = 0, next round commences | the score increases based on who is defeated and a bonus based on hero health, then the next round is commnced and new monsters are spawned | the score increases based on who is defeated and a bonus based on hero health, then the next round is commnced and new monsters are spawned
|10 | battle loop runs | if health of hero or monster is greater then zero, then battle will runs again and attacks are chosen again | if health of hero or monster is greater then zero, then battle will runs again and attacks are chosen again 
|11 | Health status | if characters health bar is 0, gameover loop will commence and a game over screen is displayed in GUI. If health of monsters is 0, next round will start. | gameover loop is initiated when hero health is zero. When monster health is 0 GUI commences next round on window|
|12| end of rounds| there are 3 round of monsters that the user must defeat, at the end of all round, a victory screen is displayed on GUI which also presents the playes score and the highscore| there are 3 round of monsters that the user must defeat, at the end of all round, a victory screen is displayed on GUI which also presents the playes score and the highscore|
|13| game over | GUI window screen is deleted and program ends| GUI window screen is deleted and program ends


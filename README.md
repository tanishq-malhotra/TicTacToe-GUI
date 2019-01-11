This is a Basic Representation of the TicTacToe Game which is made by using Python 3.7 and the Tkinter Library for adding GUI to it. It is my first gui project.

### REQUIREMENTS ###
  
  You will need Python 3.7 installed on your system. 
  If you don't have Python installed on your systen, then in that case i have added a .exe file which you can use to test the game. I have Built the .exe file using PyInstaller
  by using the --onefile method. That's why it takes some time to Load.

### HOW IT WORKS!! ###

1. The first function which is invoked by the class object is the LoginScreen function.
   In the login screen you are asked to enter the names of two player's for which i have used the Entry, Labels and a Button.

2. Then the execution is transfered to commit function which stores the value of the players
   names and then destroy the login screen window and then tranfers the execution to the start function.

3. There the real game is started.

4. Used a button list to store all the buttons and a board list which contains the board.

5. Used a click function to manage the click on the button.

6. WinCheck funtion is used to check for the WIN. If win, then the control is transfered
   to the win function.

7. Moreover I have added a menu too which contains Reset- to reset the game and Quit-to quit
   game. Used reset and quit function for that. 
   Also added some waring popup's at requres field.

### HOW TO PLAY!! ###

	Very simple, just run the tictactoe.py file or the .exe file, enter the names and click start. Now you can click on any button to add the input.
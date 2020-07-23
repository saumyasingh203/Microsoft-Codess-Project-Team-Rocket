# MICROSOFT Codess Project : Team-ROCKET

##TABLE OF CONTENTS
-Introduction
-Product Description
-Technologies
-Setup, Installation and Launch 
-User Journey
-Support
 
##INTRODUCTION
Tic-tac-toe (also known as noughts and crosses, three in a row, or Xs and Os) is a game for two players wherein each player takes turns marking the spaces, conventionally, in a 3x3 grid. The player that succeeds in placing three of their marks in either a horizontal, vertical, or diagonal row wins the game.

##PRODUCT DESCRIPTION
###Background
Microsoft’s Engage 2020 Mentorship Program aimed at equipping the students selected as mentees with the most up to date information in the field of Artificial Intelligence after having built a foundation for the same. The project undertaken by Team Rocket, a web-based application, has been designed to be an entertainment tool to be used by the crew of the Mars Colonization Project. The goal was to design a game of tic-tac-toe that utilised the concepts and principles of artificial intelligence with an original feature(s) or unique aspect(s) that set the project apart from that of others. 
The game has been developed to be played by a single player (the user) against the Team Rocket AI. The application contains varying levels of depths for the player to choose from (with level 1 being the easiest for the player to beat as opposed to the maximum depth where the computer is undefeatable) that helps showcase the capabilities of the AI. 
###Algorithm Used
The application makes use of the MINIMAX algorithm; an algorithm that is conventionally used for games that are played on a turn by turn basis, such as tic-tac-toe, chess, backgammon, etc. The backtracking algorithm, used in game theory and decision making, minimises the player’s losses and maximises his wins.  It considers the present state of the game and the moves available, then for each valid move it plays  (alternating between min and max) until it finds a terminal state (win, draw or lose).

##TECHNOLOGIES
The project has been created with the use of:
-HTML
-CSS
-JavaScript
-Python
-jQuery
-MongoDB
 
##LAUNCH
Visit <insert link> to access the deployed game.

###Setup and Installation
In order for the user to set up the game on their local machine, they are required to have Python3.5 (or a newer version) and a few dependencies installed. To set up the application, they are required to follow the following steps:
1.Clone the repository
2.Open the terminal window and execute the following command to install flask– a Python micro web framework that we have used on the backend.
```pip install flask```
3.Execute the following command to move into the 'address' directory.
```cd address```
4.Execute the following commands to install pymongo and dnspython– doing so will help you access the "leaderboard" database and consecutively view the leaderboard upon running the application on your local machine. 
```pip install pymongo```
```pip install dnspython```
5.Run the following command to launch the flask application.
```python ttt_integrated.py```
6.After executing the previous command, the following will be displayed

This means that the website is successfully running on the local machine. Copy and pasting the link into the search bar of your browser will help you launch the web application on your local machine.
 
###Viewing the database page
Upon successfully running the website on your local machine, typing the following into the search bar of your browser will display the database page. 
```localhost:5000/database```
This will allow the user to view the comments left behind by the visitors along with their scores. The data stored is then displayed as follows:


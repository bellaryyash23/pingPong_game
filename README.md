# 🕹PONG Game 🏓 using Turtle module of Python

🌟Built the classic Pong Game with help of OOP, Python Classes, Multiple Object instances, Class Inheritance, Event Listeners and more.

👉Built & Designed the Paddles in paddle.py file using Class Inheritance from Turtle Class. Use of methods like move_up & move_down for the paddle movement.

👉Ball class built in ball.py file inherited from Turtle class for specifying the ball's characteristics like movement speed and direction.
Method for bouncing ball in x-direction and y-direction defined in the class.

👉The Scoreboard class also inherited from Turtle class to design the scoreboard of the game. It updates the score of players by using attribute like l_score and r_score.
Scoreboard is modified using update_scoreboard method and user score is modified here. The Method game_over used when any player score is equal to 5.

👉The main.py implements the actual working of game. It is here where the collision of ball & paddle and the miss by paddle is detected and corresponding 
methods from above mentioned classes is called.

👉The main.py file also designs the Screen object for the game. It controls the paddle and ball animations with modifying the tracer method and updating 
the screen regularly. It also uses event listeners for making the game interactive and user responsive.

![Pong game window](https://github.com/bellaryyash23/pingPong_game/blob/master/start.JPG?raw=true)

Pong game window👆

![Pong gameover window](https://github.com/bellaryyash23/pingPong_game/blob/master/final.JPG?raw=true)

Pong gameover window👆

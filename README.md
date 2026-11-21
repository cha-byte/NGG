## THE NUMBER  GUESSING  GAME

Hello People!!

This is my first project as a beginner. Please check it out if you are interested.

### DESCRIPTION
The **Number Guessing Game** is where you have to guess the number that the computer randomly picks(but does not show it to the user). 

##### RULZ OF THE GAME

* The user will have 7 attempts the guess the number.
* The computer is gonna pick a random number between 1 to 100 and keep that to itself.
* Then, you have to guess the number that the computer has picked.
* If you guess the number in 7 attempts then you are the winner.
* If you don't, you lose.

### EXPLANATION OF THE CODE

##### THOUGHT OF THE CODE

* Firstly, __Random__ was imported for the computer to pick a random integer from 1 to 100.

    __Rand_num= random.randint( 1, 100)__

* Then, the user has to enter the input. The computer will then check whether the number entered by the user is the random integer or not.
* But here, what if the user enters a string or a float number as the input. Then, the code shows __ValueError__ . 
* So, the try-except block was used in this problem to except the ValueError and ask for another valid input without showing an error.

##### CODE EXPLANATION

* As I mentioned above, __Random__ was imported in this program.
* The rules of the game was explained clearly in the code. Then, the game starts.
* The computer picks a random number from 1 to 100.
* Then, the user enters their guess which should be an interger otherwise, the computer will not consider it and ask for another input.
* Now, the code checks whether the guessed number matches with the random integer.
* There are 3 options :

    1. If the guessed number is lower than the random integer. The computer shows you that the number is lower and make an another guess. 
    2. If the guessed number is higher than the random integer. The computer shows you that the number is higher and make an another guess. 
    3. If the guessed number matches with the random integer within the 7 attempts, then the user wins.

* After that, the __if statement__ checks whether the attempts has become zero or not. If yes, the user loses. 
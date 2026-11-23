import random
import os

print("HLOOOO !!!!")
print("WELCOME TO NGG 😃")
print("RULZ OF THE GAME")
print("1. You have a total of 7 attempts.")
print("2. The computer is gonna generate a random number which will not be shown to you.")
print("3. Then, you r gonna guess a number which will be checked if u guessed it right or not.")
print("4. If you guessed it right within 7 attempts, then u won the game. Or u lose.\n\n\n")
print("                     LET'S  START  THE  GAME !!!!                                      ")

while True :

    os.system('clear')

    Rand_num= random.randint( 1, 100)

    attempts = 7

    print(" I have picked a random number 🤫. Now it is your turn to guess it.")


    while attempts > 0 :

        while True:
            try:
                Guzd_num = int(input("Enter ur guzz: "))

                if Guzd_num < 1 or Guzd_num > 100:
                    print("U only have ur choice from 1 to 100. Not more or less than that 🤡")
                else:
                    break

            except ValueError:
                print("Are you dumb! Please enter an inteeegerrrr 🧐.")

        
        if Guzd_num > Rand_num :
            print(" 😈 Too High. Try your nxt gzz.")
        elif Guzd_num < Rand_num : 
            print(" 😈 Too Low. Try your nxt gzz.")
        else : 
            print(" AAAAHHHHHHHH!!! ")
            print("You guessed it. Congratulations 😒")
            break

        attempts = attempts-1
        print("Attempts Left :",attempts,"/7")
        
        
    if attempts == 0:
        print("Heheheehe 😏")
        print("HAHAHAHA 🤪. I WON. You LOSE.")
        

    while True:
        play_again = input("Wanna play again ? (Yes / No)").lower()

        if play_again == "yes" :
            print("Welcome Back ")
            break
        elif play_again == "no" :
            print("Enjoyed Playing With You. Byeeeee !!!")
            exit()
        else : 
            print("Enter either yes or no !")

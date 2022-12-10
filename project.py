import random

while True:

    comp_choice = random.choice(['rock', 'paper', 'scissors'])
    user_choice = input("What is your pick? ")

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("You didn't choose anything, please play again")
        continue

    print(f"Computer's choose is {comp_choice}")

    #TIE POSITION
    if comp_choice == user_choice:
        print("There is a tie between you and computer, try again")
       
    
    

    #USER WINS
    #elif comp_choice == "rock" and user_choice=="paper": 
    #   print("Congrats, You won!!")       
    #  break
    #elif comp_choice == "paper" and user_choice=="scissors":
    #   print("Congrats, You won!!")  
    #  break
    #elif comp_choice=="scissors" and user_choice =="rock":    
    #      print("Congrats, You won!!") 
    #   break
    #COMPUTER WINS
    

   #USER WINS SHORTER
    elif comp_choice == "rock" and user_choice=="paper" or  comp_choice == "paper" and user_choice == "scissors" or comp_choice=="scissors" and user_choice=="rock":  
       print("Congrats!! You won")
       break
    
    #COMPUTER WINS
    else:
        print("Oh no! Computer won!!")
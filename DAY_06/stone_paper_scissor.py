import random

class Game:
    def __init__(self):
        self.name = input("enter a name: ")
        
    def show_game(self):
        your_choice = input("enter you choice (stone/paper/ scissors): ")
        comp = random.choice(["stone", "paper", "scissors"])
        
        print("Your choice:",your_choice)
        print("Computer choice:", comp)
        
        if your_choice== comp:
            print("DRAW!")
        elif (your_choice == "stone" and comp == "scissors") or \
             (your_choice == "paper" and comp == "stone") or \
             (your_choice == "scissors" and comp == "paper"):
            print("You Win!")
        else:
            print("You Lose!")    
            
            
g= Game()
g.show_game()
        
import random
def getChoices():
    player_choice = str(input("Please enter your choices (Rock, Paper or Scissor): "))
    options = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(options)
    choices ={
        "player": player_choice,
        "computer": computer_choice
    }
    
def whowins(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie"
    
    if player_choice == "Rock":
        if computer_choice == "Paper":
            return "Paper will hold Rock, So you lost"
        else:
            return "Rock smashed scissor, so you Win!!!!"
        
    if player_choice == "Scissor":
        if computer_choice == "Paper":
            return "Scissor cuts paper, So you Win!!!"
        else:
            return "Scissor got smashed by Rock, so you lost"
        
    if player_choice == "Paper":
        if computer_choice == "Rock":
            return "Paper was able to hold rock, so you Win!!!"
        else:
            return "Paper got cut by scissor, So you lost"

choices = getChoices()
result = whowins(choices["player"], choices["computer"])
print(result)
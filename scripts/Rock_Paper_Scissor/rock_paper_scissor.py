import random

# Function to take input from the player
def getPlayer():
    player = "empty"
    player = input("Please Enter You Choice From - Rock | Paper | Scissor = ")
    while not (player == "Rock" or player == "Paper" or player == "Scissor"):
        player = input("Please Enter You Choice From - Rock | Paper | Scissor = ")
    return player

# Function to generate input from the bot
def getBot():
    lst = ["Rock", "Scissor", "Paper"]
    return random.choice(lst)

# Function to match the inputs
def getWinner(player, bot):
    if player == "Rock" and bot == "Rock":
        return "Draw"
    elif player == "Rock" and bot == "Paper":
        return "Bot"
    elif player == "Rock" and bot == "Scissor":
        return "Player"
    elif player == "Paper" and bot == "Paper":
        return "Draw"
    elif player == "Paper" and bot == "Rock":
        return "Player"
    elif player == "Paper" and bot == "Scissor":
        return "Bot"
    elif player == "Scissor" and bot == "Scissor":
        return "Draw"
    elif player == "Scissor" and bot == "Paper":
        return "Player"
    elif player == "Scissor" and bot == "Rock":
        return "Bot"
    else:
        return "DRAW"

# Main Function
def start():
    print("Welcome to the Game!\n")
    gameBegins()

# To begin game
def gameBegins():
    # To end the game if user wants
    endTheGame = "n"
    # For storing score
    player_score = 0
    bot_score = 0

    # Running the game till user wants
    while endTheGame.lower() != "y":
        player = getPlayer()
        bot = getBot()
        print("You Played -", player)
        print("Bot Played -", bot)
        winneris = getWinner(player=player, bot=bot)
        print("The Winner is - ", winneris)
        if winneris == "Player":
            player_score += 2
        elif winneris == "Bot":
            bot_score += 2
        else:
            player_score += 1
            bot_score += 1

        print("-----Score Board-----")
        print("-----Player-----", player_score)
        print("-----Bot-----", bot_score)
        print(" ")
        endTheGame = input("You wish to end? Choose Y/N: ")
    print("\nThank you for Playing!")

start()
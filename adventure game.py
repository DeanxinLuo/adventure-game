import time
import random

def print_s(s):
    print(s)
    time.sleep(0.5)

def intro(player):
    print_s("You name is Cristiano Ronaldo, and you want to be a football superstar.")
    print_s("You know you need to practice your skills and beat Messi/Neymar to become superstar.")
    print_s(player+" is 'The Goal' player in football field,\n"
            "and you are just a freshman for now in the same field.")
    print_s("You are now have an opportunity to beat other players.")
    print_s("You will get chance and beat other players in the match after 1 month")
    print_s("Now, you have not mastered any football skills, so you are not prepared.")

def play_choice(mastered_skills,player,skills):
    print_s("Enter 1 to move to the next match.")
    print_s("Enter 2 to practice hard until next match.")
    print_s("What would you like to do?")
    choice = int(input("(Please enter 1 or 2).\n").lower())
    if choice == 1:
        play_match(mastered_skills,player,skills)
    elif choice == 2:
        play_skills(mastered_skills,skills)
    else:
        print_s("not valid")
        print_s("please enter valid choice")

def play_match(mastered_skills,player,skills):
    print_s("you approach the next match")
    print_s("you are stand in the football court.")
    print_s("Wow! you are facing to " + player)
    print_s("You are trying to beat " + player)
    print_s("Would you like to\n"
            "1. shooting\n"
            "2. You realize you need do more practices and get off from the football court \n")
    action_play = int(input("please enter 1 or 2").lower())
    if action_play == 1:
        if skills in mastered_skills:
            print_s("Yes, you scored! You defeated " + player)
            print_s("You become 'the goal' pleyer")
        else:
            print_s('You missed, ' + player + ' defeated you.')
            print_s("Go back to do more practice and prepare for next match.\n")

    elif action_play == 2:
        print_s("You left the court and go back to practice a lot")

def play_skills(mastered_skills,skills):
    print_s("You work hard and successfully mastered " + skills)
    mastered_skills.append(skills)

def play_again():
    return input("Play again? [y|n]\n")

def end():
    print_s("Wait for the come back whenever, Thanks")

def football_game():
    mastered_skills = []
    player = random.choice(["Messi","Neymar","Bale","Zidane"])
    skills = random.choice(["shooting", "rainbow flick", "double scissor"])
    intro(player)
    play_choice(mastered_skills,player,skills)

def play_game():
    while True:
        football_game()
        if play_again() == 'n':
            break
    end()

football_game()

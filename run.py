import pyfiglet
import emoji

"""
Printing the Game Name
"""
game_name = pyfiglet.figlet_format("THE MANSION")
print(game_name)

player_name = input('Enter your name:\n')
print(f"Hello, {player_name} \U0001F603")
print("This game is a quest where you choose how the game ends.")
print("You will need to answer questions and take decissions.")
print("It's 3:30 AM. The phone's ringing. Who could it be?")
print("You answer. A voice at the other end says that it's the police.")
print("Your uncle, a noted scientist, has been found dead.")
print("Time to investigate the house for any clues to his death...")
print(f"Good luck \U0001F929 {player_name}!\n")
print("You are standing at entrance of the mansion.")
print("The gothic architecture lends a creepy feel to the entrance hall.")
print("You can go FORWARD to the other side of the entrance hall.")
print("There is also a door to your LEFT.")
print("You can see a glass-paned door to the RIGHT.")


def second_bedroom():
    print("\n")
    print("You find a letter where the killer is revealed!")
    answer_letter = input("\U0001F914 Would you give it to the police? (Y or N):\n")
    if answer_letter == "Y":
        print("\n")
        you_win = pyfiglet.figlet_format("YOU WIN")
        print(you_win)
        print("\U0001F603 Good job! Police is going to arrest the killer")
    elif answer_letter == "N":
        print("\n")
        game_over = pyfiglet.figlet_format("GAME OVER")
        print(game_over)
        print("\U0001F61E Unfortunetely Polsice will never know who the killer is.")


def staircase():
    print("\n")
    print("You go up the stairs. You decide to check you uncles bedroom.")
    print("You find the bed made. \U0001F914 Looks like he didn't get to his bedroom the day he died.")
    print("You decide to check the second bedroom.")
    second_bedroom()


def closet_hall():
    print("\n")
    print("You open the closet and you find a woman hat.")
    print("You realize the hat belongs to a collegue of your uncle.")
    answer_hat = input("\U0001F914 Would you INFORM the police about it or CONFRUNT the lady yourself?:\n")
    if answer_hat == "inform":
        print("\n")
        print("\U0001F603 Good job! Police is gonna question the lady about her hat.")
        staircase()
    elif answer_hat == "confrunt":
        print("\n")
        print("Because it's too late at night, you have to wait untill tomorrow.")
        print("\U0001F61E Now it's too late to use the hat as evidence.")
        staircase()
    else:
        print("You need to choose 'inform' or 'confrunt'")
        closet_hall()


def forward():
    print("\n")
    print("You reached the end of the entrance hall.")
    print("There is a STAIRCASE here.\nYou can also go to CLOSET under the stairs.")
    answer_forward = input("\U0001F914 You want to go up the STAIRCASE or check the CLOSET:\n")
    if answer_forward == "staircase":
        staircase()
    elif answer_forward == "closet":
        closet_hall()
    else:
        print("You have to choose 'staircase' or 'closet'")
        forward()


def intro():
    print("\n")
    answer_intro = input("\U0001F914 Where do you want to go? forward/left/right:\n")
    if answer_intro == "forward":
        forward()
    elif answer_intro == "left":
        print("\n")
        print("You enter in your late uncle's office and see on his desk a letter.")
        print("You pick up the letter an read it \U0001F9D0")
        print("You find out he had a meeting with the University dean two days ago.")
        print("You call the dean but he said your uncle never made it to ther meeting \U0001F615")
        intro()
    elif answer_intro == "right":
        print("\n")
        print("You have a walk in the garden and realize the flower beds are dry.")
        print("That is a clue your uncle didn't take care of the garden lately.")
        print("You are back in the house")
        intro()
    else:
        intro()


intro()

import time

#Function for the introduction of the Game
def introduction():
    print("Welcome to 'The Quest for the Enchanted Sword'!")
    time.sleep(1)
    print("You, brave adventurer, are on a quest to find the legendary Enchanted Sword.")
    time.sleep(1)
    print("Your journey begins now...\n")

#Function to ensure valid input choice at different phases of the game
def make_choice(choices):
    while True:
        print("Choose your path:")
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice}")

        try:
            user_input = int(input("Enter the number of your choice: "))
            if 1 <= user_input <= len(choices):
                return user_input
            else:
                print("Invalid input. Please enter a valid number.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

def forest_path():
    print("You find yourself in a dense forest.")
    time.sleep(1)
    print("1. Venture deeper into the forest.")
    print("2. Take the path to the right.")
    print("3. Climb a tree to get a better view.")

    choice = make_choice(["Venture deeper", "Take the right path", "Climb a tree"])

    if choice == 1:
        print("As you venture deeper, you encounter a group of friendly elves who offer guidance.")
        return "elves_guidance"
    elif choice == 2:
        print("The right path leads you to a river. You spot a mysterious figure on the other side.")
        return "mysterious_figure"
    else:
        print("You climb the tree and see a distant castle. There might be valuable information there.")
        return "castle_path"

def castle_path():
    print("You approach the castle and discover a secret entrance.")
    time.sleep(1)
    print("1. Enter the castle stealthily.")
    print("2. Knock on the front door.")

    choice = make_choice(["Enter stealthily", "Knock on the front door"])

    if choice == 1:
        print("You navigate the castle quietly, avoiding guards and finding useful information.")
        return "continue_path"
    else:
        print("The door opens, and you are greeted by a friendly castle resident who shares knowledge.")
        return "continue_path"

def elves_guidance():
    print("The elves share ancient knowledge about the Enchanted Sword and suggest two paths.")
    time.sleep(1)
    print("1. Follow the mountain trail.")
    print("2. Cross the enchanted bridge.")

    choice = make_choice(["Follow the mountain trail", "Cross the enchanted bridge"])

    if choice == 1:
        print("The mountain trail is treacherous but leads you to a hidden cave.")
        return "hidden_cave"
    else:
        print("The enchanted bridge takes you to a magical garden where the sword is said to be.")
        return "magical_garden"

def mysterious_figure():
    print("You approach the mysterious figure who reveals to be a wise old wizard.")
    time.sleep(1)
    print("1. Ask for magical assistance.")
    print("2. Politely decline and continue your journey.")

    choice = make_choice(["Ask for magical assistance", "Politely decline"])

    if choice == 1:
        print("The wizard grants you a magical amulet that can protect you from harm.")
        return "wizard_amulet"
    else:
        print("You thank the wizard and continue on your path.")
        return "continue_path"

def hidden_cave():
    print("In the hidden cave, you find the sword protected by a guardian.")
    time.sleep(1)
    print("1. Engage in a battle with the guardian.")
    print("2. Try to negotiate with the guardian.")

    choice = make_choice(["Engage in a battle", "Negotiate"])

    if choice == 1:
        print("The battle is fierce, but you emerge victorious and claim the Enchanted Sword.")
        return "victory"
    else:
        print("Your negotiation skills impress the guardian, and it allows you to take the sword.")
        return "victory"

def magical_garden():
    print("In the magical garden, the sword is surrounded by mystical creatures.")
    time.sleep(1)
    print("1. Approach cautiously.")
    print("2. Use the wizard amulet to calm the creatures.")

    choice = make_choice(["Approach cautiously", "Use the wizard amulet"])

    if choice == 1:
        print("The creatures sense your pure intent and allow you to take the Enchanted Sword.")
        return "victory"
    else:
        print("The wizard amulet works like a charm, and the creatures let you take the sword.")
        return "victory"

def wizard_amulet():
    print("With the wizard amulet, you feel a magical shield protecting you.")
    time.sleep(1)
    print("You continue your journey with confidence.")
    time.sleep(1)
    print("After sometime, You found out that the path splits up in two ways.")
    print("1. Take the path to the left.")
    print("2. Take the path to the right.")

    choice = make_choice(["Turn left", "Turn right"])

    if choice == 1:
        print("You found a castle.")
        return "castle_path"
    else:
        print("You found a Magical Garden.")
        return "magical_garden"

def continue_path():
    print("You continue on your path with determination.")
    print("You encounter a wild beast.")
    time.sleep(1)
    print("1.Fight with the beast")
    print("2. Run away from the beast")

    choice = make_choice(["Fight", "Run Away"])

    if choice == 1:
        print("The beast killed you")
        return "lost"
    else:
        print("While running away from the beast, you saw ancient ruins.")
        return "ancient_ruins"

def ancient_ruins():
    print("You enter in the ancient ruins.")
    print("You encounter with a witch.")
    time.sleep(1)
    print("1. Engage in a battle with the witch.")
    print("2. Ask for magical assistance.")

    choice = make_choice(["Engage in a battle", "Ask for magical assistance"])

    if choice == 1:
        print("The witch turned you into a statue.")
        return "lost"
    else:
        print("The witch grants you a wish.")
        print("You ask for the Magical Sword.")
        return "victory"

#Function if you achieve Victory in the Game
def victory():
    print("Congratulations! You have successfully obtained the Enchanted Sword.")
    time.sleep(1)
    print("You return to the kingdom as a hero, ready to face the ancient dragon.")

#Function if you lost in the Game
def lost():
    print("You Lost !!")
    print("Better Luck Next Time.")
    time.sleep(1)
    print("Thank You")

if __name__ == "__main__":
    introduction()
    current_location = forest_path()

    #Starting of the While Loop
    while current_location != "victory":

        if current_location == "lost":
            break

        if current_location == "elves_guidance":
            current_location = elves_guidance()

        elif current_location == "mysterious_figure":
            current_location = mysterious_figure()

        elif current_location == "hidden_cave":
            current_location = hidden_cave()

        elif current_location == "magical_garden":
            current_location = magical_garden()

        elif current_location == "wizard_amulet":
             current_location =  wizard_amulet()

        elif current_location == "continue_path":
            current_location = continue_path()

        elif current_location == "castle_path":
            current_location = castle_path()

        elif current_location == "ancient_ruins":
            current_location = ancient_ruins()
        #End of the While Loop

    if current_location == "lost":
        lost()
    else:
        victory()

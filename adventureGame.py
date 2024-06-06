class Adventure:
    def __init__(self):
        self.name = input("Type your name: ")
        print("Welcome", self.name, "to this adventure!")

    def start(self):
        answer = input(
            "You are on a dirt road. It has come to an end, and you can go left, right, or straight. Which way would you like to go? ").lower()

        if answer == "left":
            self.left_path()
        elif answer == "right":
            self.right_path()
        elif answer == "straight":
            self.straight_path()
        else:
            print('Not a valid option. You lose.')

    def left_path(self):
        answer = input(
            "You come to a river. Do you want to walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

        if answer == "swim":
            print("You swam across and were eaten by an alligator.")
        elif answer == "walk":
            print("You walked for many miles, ran out of water, and you lost the game.")
        else:
            print('Not a valid option. You lose.')

    def right_path(self):
        answer = input(
            "You come to a bridge. It looks wobbly. Do you want to cross it or head back? Type cross to cross it or back to head back: ").lower()

        if answer == "back":
            print("You go back and lose.")
        elif answer == "cross":
            self.bridge_crossing()
        else:
            print('Not a valid option. You lose.')

    def bridge_crossing(self):
        answer = input(
            "You cross the bridge and meet a stranger. Do you want to talk to them or ignore them? Type talk to talk to them or ignore to ignore them: ").lower()

        if answer == "ignore":
            print("You ignore the stranger, and they are offended. You lose.")
        elif answer == "talk":
            print("You talk to the stranger, and they give you gold. You WIN!")
        else:
            print('Not a valid option. You lose.')

    def straight_path(self):
        answer = input(
            "You find a hidden path. It's dark and mysterious. Do you want to explore it or go back? Type explore to go forward or back to go back: ").lower()

        if answer == "explore":
            print("You venture into the unknown and find treasure. You WIN!")
        elif answer == "back":
            print("You decide to go back and lose.")
        else:
            print('Not a valid option. You lose.')

    def end(self):
        print("Thank you for trying", self.name)


# Create an instance of Adventure and start the adventure
game = Adventure()
game.start()
game.end()

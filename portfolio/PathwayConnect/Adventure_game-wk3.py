"""
This adventure game consists of multiple levels, with each level presenting the player with a scenario and possible choices and outcome. The player's choices determine the outcome of the scenario and lead to different subsequent levels.  The game includes option at any point to decide on their current situation. Overall, the game works by presenting the player with multiple scenarios and choices, with each choice leading to a different outcome and subsequent level. The player must carefully consider their choices and think strategically to reach the desired outcome.
"""


# Import 'random' module  to select items from list
import random

# To fulfil my creative task, i added extra level 4 and extended the game scenario to accommodate more options

# Level 0 Introduction
print("\n ~~~~~~~~ Introduction ~~~~~~~\n")
print("You find yourself lost in a dark forest with no idea how you got there.")
print("You see two paths leading in different directions, choose one:")
print()


# Choice of path to follow
path_choice = input("LEFT\nRIGHT\nEnter your choice: ")
print()

# Level 1
# Make choice of direction to proceed to level 1
# Path to cave is left
if path_choice.upper() == "LEFT":
    print("Welcome to Level 1")
    print("You have come across a cabin. You see a sleeping guard and a locked chest")
    print("What do you do?")
    print()
    cabin_choice = input("STEAL\nSNEAK\nEnter your choice: ")
    print()

    # Cabin choice chosen, steal the key
    if cabin_choice.upper() == "STEAL":
        print("You successfully steal the key and open the chest")
        print("You find a map and a compass")
        print("Which direction do you go now?")
        cabin_direction = input("NORTH\nEAST\nSOUTH\nWEST\nEnter your choice: ")
        print()

        # Level 2
        # Cave direction to north
        if cabin_direction.upper() == "NORTH":
            print("Welcome to level 2")
            print(
                "You proceed north on a footpath that leads straight to a pit oof fire"
            )
            print("You look back to discover your path is blocked")
            print("You also discover you are being sucked towards the pit, you fall in")
            print("You are no more, game over")
            print()

        # Cave direction to east
        elif cabin_direction.upper() == "EAST":
            print("Welcome to level 2")
            print("You proceed east and hear drumbeats and laughter")
            print("You you see a crowd of merry makers dancing")
            print("You join them in the dance only to realize that as they are dancing")
            print("They have sad worried frowns on their faces,")
            print("You also realize they are not laughing but wailing as they dance")
            print("You try to stop dancing but a force keeps you dancing")
            print("You can not proceed any further as you dance till exhaustion")
            print("GAME OVER")
            print()

        # Cave direction to south
        elif cabin_direction.upper() == "SOUTH":
            print("Welcome to level 2")
            print("You walk along a winding bending road and appear at a beach")
            print("You decide to take a quick swim as you are all sweaty")
            print("You are swallowed by a big fish")
            print("GAME OVER")

        # Cave direction to west
        elif cabin_direction.upper() == "WEST":
            print("Welcome to level 2")
            print("You walk briskly along a foot path that leads to a short bridge")
            print(
                "You cross the bridge and is met by a smiling individual who hand you a note"
            )
            print(
                "You read the note and it says you are entitled to a night at a five star hotel"
            )
            print(
                "You are led to the hotel then your room, you put on the TV and and greeted with a question"
            )
            print()
            tv_choice = input(
                "Do you want to PROCEED to level 3?\nOr STOP here forever?\n Enter your choice: "
            )
            print()

            # TV choice to proceed
            if tv_choice.upper() == "PROCEED":
                print("You are welcome to level 3")
                print(
                    "You have shown focus and determination by indicating your intention to proceed"
                )
                print("Luck smiles on you")
                print("Congratulations, you receive a $1,000,000.00 as a reward")
                print("Chill out and enjoy yourself")

            # TV choice to stop here
            elif tv_choice.upper() == "STOP":
                print("Thanks for playing the game")
                print("I hope you enjoy your stay?")
                print("GAME OVER")

        else:
            print("Invalid Input. Try again from beginning.")
            print()

    # Cabin choice chosen, sneak past guard
    elif cabin_choice.upper() == "SNEAK":
        print("You successfully sneaked past the guard and exit the cabin")
        print("You find your self in a corridor with three doors")
        print("Which door should you choose?")
        print()
        door_choices = input("FIRST door\nSECOND door\nTHIRD door\nEnter your choice: ")
        print()

        # Level 2
        # Options for treasure behind first door
        if door_choices.upper() == "FIRST":
            print("Welcome to Level 2")
            print("You find a treasure room with a locked door")
            print("What do you do?")
            print()
            treasure_choice = input(
                "PICK the lock\nSEARCH for key\nEnter your choice: "
            )
            print()

            # Level 3
            # Pick the lock
            if treasure_choice.upper() == "PICK":
                print("You ponder and decide to pick the door")
                print(
                    "You succeed in opening the, you open the door and step into a dark room"
                )
                print(
                    "The door shuts behind you, you are stuck in the darkness and feel your self falling"
                )
                print("GAME OVER")
                print()

            # Search for the key
            elif treasure_choice.upper() == "SEARCH":
                print("You begin to look around the room for the key")
                print("You search under every item in the room but cant find the key")
                print("You are confused as you did not locate the key")
                print("You stand and ponder, you put both hands into your pockets")
                print("You then feel a key in one of your pockets")
                print("Excited you bring in out and try it in the lock")
                print(
                    "The door opens and you see a treasure box in the center of the lit room"
                )
                print(
                    "You open the box and a monster jumps out of the box and knocks you out"
                )
                print("GAME OVER")
                print()

            else:
                print("Invalid Input. Try again from beginning.")
                print()

        # Options for traps behind second door
        elif door_choices.upper() == "SECOND":
            print("Welcome to Level 2")
            print("You come across a trap filled room")
            print("What do you do?")
            print()
            trap_choice = input("Try to DISARM trap\nAVOID traps\nEnter your choice: ")
            print()

            # level 3
            # Disarm the trap
            if trap_choice.upper() == "DISARM":
                print("Welcome to Level 3")
                print("Your hearts beats loudly as you attempt to disarm the traps")
                print("It takes you a while, you are all sweaty")
                print("Finally, you disarm all the traps")
                print("A treasure chest appears in the center of the room")
                print("You open the chest and find a large hand sized ruby")
                print("Congratulations you receive a reward")
                print()

            # Avoid the traps
            elif trap_choice.upper() == "AVOID":
                print("Welcome to Level 3")
                print("You attempt to avoid the traps but mistakenly set one off")
                print("You are blown to up")
                print("GAME OVER")
                print()

            else:
                print("Invalid Input. Try again from beginning.")
                print()

        # Options behind third door
        elif door_choices.upper() == "THIRD":
            print("Welcome to Level 2")
            print("You find a dark room with a sleeping dragon")
            print("What do you do?")
            print()
            dragon_choice = input(
                "Try to SNEAk_PAST the dragon\nWAKE_UP the dragon and fight it\nEnter your choice: "
            )
            print()

            # Level 3

            # Sneak past the dragon
            if dragon_choice.upper() == "SNEAK_PAST":
                print("Welcome to level 3")
                print("You quietly sneak past the dragon and reach an alter")
                print("You discover a shining scroll on the alter")
                print(
                    "You are bold, determined, smart and full of tact, you are safe now"
                )
                print()

            # Wake up the dragon
            elif dragon_choice.upper() == "WAKE_UP":
                print("Welcome to level 3")
                print("You boldly wake up the dragon")
                print("You ask it what it has for you")
                print("The dragon gobbles you up and goes back to sleep")
                print("GAME OVER")
                print()

            else:
                print("Invalid Input. Try again from beginning.")
                print()

        else:
            print("Invalid Input. Try again from beginning.")
            print()
    else:
        print("Invalid Input. Try again from beginning.")
        print()


# Path to cave is right
elif path_choice.upper() == "RIGHT":
    print("Welcome to Level 1")
    print("You come across a cave. You encounter a dangerous monster")
    print("What do you do?")
    print()
    cave_choice = input("You FIGHT\nYou FLEE\nEnter your choice: ")
    print()

    # Cave choice chosen is fight
    if cave_choice.upper() == "FIGHT":
        print("Welcome to level 2")
        print("You successfully defeated the monster and find a map and a compass")
        print("Which direction do you go? ")
        cave_direction = input("NORTH\nEAST\nSOUTH\nWEST\nEnter your choice: ")
        print()

        # Direction north
        if cave_direction.upper() == "NORTH":
            print("Welcome to Level 3")
            print("You come across a river with a dangerous current")
            print("What do you do?")
            print()
            river_choice = input(
                "CROSS the river\nFollow the river DOWNSTREAM\nEnter your choice: "
            )
            print()

            # Game over on river cross
            if river_choice.upper() == "CROSS":
                print("Welcome to Level 4")
                print(
                    "You attempt to cross the river and get swept away by the current"
                )
                print("GAME OVER")
                print()

            # Follow river downstream to safety
            elif river_choice.upper() == "DOWNSTREAM":
                print("Welcome to Level 4")
                print("You follow the river downstream and find a safe crossing")
                print("You have reached safety, you did great")
                print()

            else:
                print("Invalid Input. Try again from beginning.")
                print()

        # Direction East
        elif cave_direction.upper() == "EAST":
            print("Welcome to Level 3")
            print("You come across a bridge that is guarded by bandits")
            print("What do you do?")
            print()
            bandit_choice = input(
                "FIGHT the bandits\nBRIBE the bandits\nEnter your choice: "
            )
            print()

            # Bandit choice to fight
            if bandit_choice.upper() == "FIGHT":
                print("Welcome to Level 4")
                print("You fight the bandits and get injured in the process")
                print("You proceed but injuries slow you down")
                print("You eventually see a nearby village in the distance")
                print()
                village_choice = input(
                    "GO_TO the village\nStay HIDDEN\nEnter your choice: "
                )

                # Village choice to go to
                if village_choice.upper() == "GO_TO":
                    print("You go to the village and find help.")
                    print("You are taken to safety.")
                    print()

                # Village choice to stay hidden
                elif village_choice.upper() == "HIDDEN":
                    print(
                        "You stay hidden and eventually make your way to safety on your own."
                    )
                    print("You suffer from hunger and dehydration along the way.")
                    print("GAME OVER")
                    print()

                else:
                    print("Invalid Input. Try again from beginning.")
                    print()

            # Bandit choice to surrender
            elif bandit_choice.upper() == "BRIBE":
                print("Welcome to Level 4")
                print(
                    "You bribe and surrender to the bandits and they take all your belonging after"
                )
                print("You eventually reach safety but with nothing left")
                print()

            else:
                print("Invalid Input. Try again from beginning.")
                print()

        # Direction South
        elif cave_direction.upper() == "SOUTH":
            print("Welcome to Level 3")
            print("You come across a desert with limited supplies")
            print("What do you do?")
            print()
            desert_choice = input(
                "RISK crossing the desert\nTake a LONGER_ROUTE\nEnter your choice: "
            )
            print()

            # Cross desert choice
            if desert_choice.upper() == "RISK":
                print("Welcome to Level 4")
                print("You risk crossing the desert and die in the process")
                print("GAME OVER")
                print()

            # Take a longer route
            elif desert_choice.upper() == "LONGER_ROUTE":
                print("Welcome to Level 4")
                print("You take a longer route and ran out of provisions")
                print("You nearly died but eventually reached safety")
                print("Congratulations, but you did not complete the whole game")
                print("Try again from start.")
                print()

            else:
                print("Invalid Input. Try again from beginning.")
                print()

        # Direction WEST
        elif cave_direction.upper() == "WEST":
            print("Welcome to Level 3")
            print("You come across a dense forest with dangerous animals")
            print("What do you do?")
            print()
            forest_choice = input(
                "Try to FIND_A_WAY through the forest\nGO_AROUND the forest\nEnter your choice: "
            )
            print()

            # Build a fire in forest choice
            if forest_choice.upper() == "FIND_A_WAY":
                print("Welcome to Level 4")
                print("You build a fire and it attracts the attention of rescuers")
                print("You are rescued and taken too safety")
                print()

            # Climb a tree
            elif forest_choice.upper() == "GO_AROUND":
                print("Welcome to Level 4")
                print("You go around the forest and end up walking in circles")
                print(
                    "You eventually climb a tree after a long route round and spotted a road"
                )
                print("You make your way to the road and eventually reach safety")
                print()

            else:
                print("Invalid Input. Try again from beginning.")
                print()

        else:
            print("Invalid Input. Try again from beginning.")
            print()

    # cave choice chosen is to flee
    else:
        cave_choice.upper() == "FLEE"
        print("Thank you for fleeing, you loose")
        print("Game Over")
        print()
else:
    print("Invalid Input. Try again from beginning.")
    print()

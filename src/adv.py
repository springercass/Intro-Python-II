from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.

player_name = input("Hello, what is your name?")
new_player = Player(player_name, room['outside'])

# Write a loop that:
# * Prints the current room name
while True:
    print(
        f"{new_player.name}, your current location is {new_player.current_room.name}.")

    # * Prints the current description (the textwrap module might be useful here).
    print(f"{new_player.current_room.description}.")
    print("---")
    print("North: n, East: e, South: s, West: w, Quit: q")

    # * Waits for user input and decides what to do.
    direction = input("Which direction would you like to go?")
    answer = direction.lower()
    print("---")
    if len(answer) == 1:
        if direction not in ["n", "e", "s", "w", "q"]:
            print("Please enter a valid direction.")
            continue

        if direction == "q":
            print("End game.")
            break

        current_room = new_player.current_room

        if direction == "n":
            if current_room.n_to is None:
                print("You can't go that way.")
                continue

            else:
                new_player.current_room = current_room.n_to

        elif direction == "e":
            if current_room.e_to is None:
                print("You can't go that way.")
                continue

            else:
                new_player.current_room = current_room.e_to

        elif direction == "s":
            if current_room.s_to is None:
                print("You can't go that way.")
                continue

            else:
                new_player.current_room = current_room.s_to

        elif direction == "w":
            if current_room.w_to is None:
                print("You can't go that way.")
                continue

            else:
                new_player.current_room = current_room.w_to

    else:
        print("Please enter a valid direction.")

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    # If the user enters "q", quit the game.

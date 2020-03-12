# ##############################################################################
#
#               Text based RPG game - Easy level
#
# ##############################################################################

# import person class
from GameClasses import person

# define general functions
def print_line():
    print("\t***---***---***---***---***---***---***---***---***---***---***---***---***")

# ##############################################################################
#                   main program
# ##############################################################################

# ###################
#   start the game
# ###################
print_line()
print("\t\t\t Welcome to play")
print("\t\t\t This game is text base RPG game")
print("\t\t\t Your task is to kill bad gays, they are your enemies")
name = input('\t\t\t First, give your name: ').capitalize()

""" ----------------------------------------------
    create player and enemy objects
    ---------------------------------------------- """
player = person(name, 500, 0, 100)
enemy = person("Dragon", 500, 500, 100)
""" ----------------------------------------------
    print player's and enemy's statistics
    ---------------------------------------------- """
print_line()
player.get_stat()
enemy.get_stat()

# ##########################
# start main loop of game
# ##########################
keep_playing = True
while (keep_playing == True):
    """ ----------------------------------------------
        player's turn to choose action to take
        ---------------------------------------------- """
    print_line()
    player_action = player.choose_action()
    damage = player.generate_dmg(player_action)
    new_hp = enemy.take_dmg(damage)

    print("\t\t\t Enemy's damage is: {}".format(damage))

    """ ----------------------------------------------
        player's turn to choose action to take
        ---------------------------------------------- """
    damage = enemy.generate_dmg(player_action)
    new_hp = player.take_dmg(damage)

    print("\t\t\t player's damage is: {}".format(damage))

    """ ----------------------------------------------
        print player's and enemy's statistics
        ---------------------------------------------- """
    print_line()
    player.get_stat()
    enemy.get_stat()

    if player.hp == 0:
        keep_playing = False
    elif enemy.hp == 0:
        keep_playing = False
    else:
        pass

# ##############################################################################
#
#               Text based RPG game
#
# ##############################################################################

# import person class
from GameClasses import Person, Magic


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
player = Person(name, 500, 500, 100)
enemy = Person("Dragon", 500, 500, 100)
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
        First player take action to damage the enemy
        Then enemy take action to damage the player
        ---------------------------------------------- """
    print_line()
    player_action = player.choose_action()
    if player_action == 1:
        """ First player generates damage for enemy """
        enemy_damage = player.generate_dmg(player_action)
        """ Then enemy generates damage for player """
        player_damage = enemy.generate_dmg(player_action)
        """ no magic damage in this case """
        magic_damage = 0
    elif player_action == 2:
        """ at this stage enemy does not generate magic powers """
        enemy_damage = 0
        magic = player.choose_magic()
        if magic == 1:
            magic_damage = player.generate_magic_damage()
        elif magic == 2:
            magic_damage = player.generate_magic_damage()
        elif magic == 3:
            magic_damage = player.generate_magic_damage()
        elif magic == 4:
            magic_damage = player.generate_magic_damage()
        else:
            keep_playing = False
    elif player_action == 9:
        keep_playing = False

    """  First player gives a damage to the enemy """
    new_hp = enemy.take_dmg(enemy_damage)
    new_mp = enemy.update_mp(magic_damage)

    print("\t\t\t Enemy's damage is: {}".format(enemy_damage))
    print("\t\t\t Enemy's magic damage is: {}".format(magic_damage))

    """ Then enemy gives a damage the playere """
    magic_damage = 0
    new_hp = player.take_dmg(player_damage)
    new_mp = player.update_mp(magic_damage)

    print("\t\t\t player's damage is: {}".format(player_damage))
    print("\t\t\t player's magic damage is: {}".format(magic_damage))

    """ ----------------------------------------------
        print player's and enemy's statistics
        ---------------------------------------------- """
    print_line()
    player.get_stat()
    enemy.get_stat()

    if player.hp == 0 or player.mp == 0:
        keep_playing = False
    elif enemy.hp == 0 or enemy.mp == 0:
        keep_playing = False
    else:
        pass

# end while
print_line()
print("\t\t\t Good Bye!")
print("\t\t\t Thank you for playing this game.")
print("\t\t\t Hopefully I'll see you again soon.")
print_line()
# end of the game

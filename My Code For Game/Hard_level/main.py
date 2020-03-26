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
skip_enemy_dmg = False
enemy_damage = 0
magic_damage = 0
while (keep_playing == True):
    """ ----------------------------------------------
        First player take action to damage the enemy
        Then enemy take action to damage the player
        ---------------------------------------------- """
    print_line()
    player_action = player.choose_action()
    if player_action == 1:
        """ First player generates damage for enemy """
        enemy_damage = player.generate_dmg()
        magic_damage = 0
    elif player_action == 2:   # dark magic
        """ at this stage player does generates magic powers """
        enemy_damage = 0
        magic = player.choose_magic()
        if magic == 1:    # magic - Fire
            magic_damage = player.generate_magic_damage()
        elif magic == 2:    # magic - Lightning
            magic_damage = player.generate_magic_damage()
        elif magic == 3:    # magic - Hurricane
            magic_damage = player.generate_magic_damage()
        elif magic == 4:    # magic - Corona
            magic_damage = player.generate_magic_damage()
            """ corona extra damage: 30 points """
            magic_damage += 30
        else:
            keep_playing = False
    elif player_action == 3:    # light magic = healing
        """ Player will be given healing and at the same time no enemy damage """
        enemy_damage = 0
        magic_damage = 0
        skip_enemy_dmg = True
        new_hp = player.healing()
        if new_hp == player.max_hp:
            print("\t\t\t Your HP is full")
        else:
            print("\t\t\t The light magic heals 100 points of hp")
        # endif
    elif player_action == 9:    # player wants end the game, so no enemy action
        enemy_damage = 0
        magic_damage = 0
        keep_playing = False
        skip_enemy_dmg = True
    # endif

    """  First player gives a damage to the enemy """
    if skip_enemy_dmg == False:
        new_hp = enemy.take_dmg(enemy_damage)
        new_mp = enemy.update_mp(magic_damage)
        if new_hp <= 0 or new_mp <= 0:
            player_damage = 0
            magic_damage = 0
            keep_playing = False
            skip_enemy_dmg = True
        # endif
    else:
        skip_enemy_dmg = False
    # endif

    print("\t\t\t Enemy's damage is: {}".format(enemy_damage))
    print("\t\t\t Enemy's magic damage is: {}".format(magic_damage))

    """ player wants continue playing the game (default supposition)
        -- if this False -> player wants to end the game, so no enemy actions """
    if keep_playing == True:
        """ Then enemy's turn to give a damage the player
            enemy's brain: enemy will now select the action randomly
            If enemy chooses magic, and the magic choice is also a random choice
            generate_dmg """
        enemy_action = enemy.enemy_action_magic()
        """ after the choice of action (or amgic) print out the choice """
        if enemy_action == 1:    # basic action
            print("\t\t\t Enemy's choice: basic action")
        elif enemy_action == 2:    # Healing
            print("\t\t\t Enemy's choice: Healing")
        elif enemy_action == 3:    # magic - Fire
            print("\t\t\t Enemy's choice: Fire")
        elif enemy_action == 4:    # magic - Lightning
            print("\t\t\t Enemy's  choice: Lightning")
        elif enemy_action == 5:    # magic - Hurricane
            print("\t\t\t Enemy's  choice: Hurricane")
        elif enemy_action == 6:    # magic - Corona
            print("\t\t\t Enemy's  choice: Corona")
        # endif
        """ Then enemy generates damage for player """
        player_damage = enemy.generate_player_dmg(enemy_action)
        if enemy_action == 1:
            """ no magic damage in this case """
            magic_damage = 0
            new_hp = player.take_dmg(player_damage)
        elif enemy_action == 2:
            """ no any damage in this case """
            player_damage = 0
            magic_damage = 0
        elif 3 <= enemy_action <= 6:
            """ no action damage in this case """
            magic_damage = player_damage
            new_mp = player.update_mp(magic_damage)
            player_damage = 0
        # endif
        # new_hp = player.take_dmg(player_damage)
        # new_mp = player.update_mp(magic_damage)
    # endif if keep_playing == True:

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
        print_line()
        print("\n\t\t\t ENEMY WON!!!!\n")
        # print_line()
    elif enemy.hp == 0 or enemy.mp == 0:
        keep_playing = False
        print_line()
        print("\n\t\t\t PLAYER WON!!!!\n")
        # print_line()
    else:
        pass
    # endif

# end while
print_line()
print("\t\t\t Good Bye!")
print("\t\t\t Thank you for playing this game.")
print("\t\t\t Hopefully I'll see you again soon.")
print_line()
# end of the game

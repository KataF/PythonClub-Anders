""" ##############################################################################
        This file includes all classes used in the game
    ##############################################################################"""

# import random library
import random

""" define person class """
class Person:
    name = "xXx"
    hp = 500
    max_hp = hp
    mp = 0
    max_mp = mp
    atk_high = 0
    atk_low = 0
    action = []
    """ This function will initialize created person object """
    def __init__(self, name, hp, mp, atk):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Attack", "Magic, Heal"]

    def get_stat(self):
        """ This function will print out player's/enemy's name and statistics of HP/MaxHP, MP/MaxMP
            input parameters:
                None
            returns: None
        """
        print("\t\t\t {}\'s,".format(self.name))
        print("\t\t\t health points are {}/{}".format(self.hp, self.max_hp))
        print("\t\t\t magic points are {}/{}".format(self.mp, self.max_mp))


    def generate_dmg(self):
        """ This function calculates a attack damage value randomly between atk_high and atk_low.
            player or enemy generates damage to other one
            input parameters:
                None
            returns: damage_value - attack's damage value
        """
        damage_value = random.randrange(self.atk_low, self.atk_high)
        return damage_value

    def take_dmg(self, damage_value):
        """ This function calculates the HP loss and return new HP points
            player or enemy takes a hit to itself
            check if health points goes to negative then place zero to health point
            input parameters:
                damage_value - damage value from attack
            returns: self.hp - player's / enemy's new health points (HP points)
        """
        self.hp = self.hp - damage_value
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def choose_action(self):
        """ ask player to choose what kind of action to take
            remember convert input str to int
            input parameters:
                None
            returns: atk - player's action choice
        """
        print("\t\t\t Choose action from below")
        print("\t\t\t Actions are:")
        print("\t\t\t 1 - Attack")
        print("\t\t\t 2 - Magic")
        print("\t\t\t 3 - Heal")
        print("\t\t\t 9 - exit")
        atk = int(input('\t\t\t '))
        return atk

    def update_mp(self, magic_damage):
        """ This function will be deducted mp after each execution
            input parameters:
                magic_damage - mp is deducted by magic_damage
            returns: deducted mp value
        """
        self.mp = self.mp - magic_damage
        if self.mp <= 0:
            self.mp = 0
        return self.mp

    def choose_magic(self):
        """ ask player to choose what kind of magic to take
            remember convert input str to int
            input parameters:
                None
            returns: magic - player's magic choice
        """
        print("\t\t\t Choose Magic")
        print("\t\t\t 1 - Fire")
        print("\t\t\t 2 - Lightning")
        print("\t\t\t 3 - Hurricane")
        print("\t\t\t 4 - Corona")
        # print("\t\t\t 5 - Power Boost") - future feature
        magic = int(input('\t\t\t '))
        return magic

    def generate_magic_damage(self):
        """ This function will generate magic damage and will return a random value
            between dmg + 15 and dmg - 15
            check if health points goes to negative then place zero to health point
            input parameters:
                None
            returns: magic_damage - player's / enemy's magic damage value
        """
        magic_damage = 0
        m_low = -15
        m_high = 15
        magic_damage = Magic.dmg + random.randrange(m_low, m_high)
        """" muutos tässä """
        if self.mp > self.max_mp:
            self.mp = self.max_mp
        return magic_damage

    def healing(self):
        """ This function will heal player and gives more health points.
            So far this is fix value for healing: 100 hp points.
            Function will also check health points that they does not
            go to negative or over the maximum health point.
            input parameters:
                None
            returns: health point - player's new health point
        """
        self.hp = self.hp + 100
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif 0 < self.hp and self.hp < self.max_hp:
            dummy = 0    # return as it is
        elif self.hp < 0:
            self.hp = 0
        # endif
        return self.hp

    def enemy_action_magic(self):
        """ Enemy's brain: choose what kind of action to take
            Generate randomly what kind of action enemy will choose
            input parameters:
                None
            returns: enemy_action - enemy's choice
        """
        # these initial number equals to action at main module
        action_min = 1
        action_max = 3
        magic_min = 3
        magic_max = 6
        enemy_action = random.randrange(action_min, action_max)
        if enemy_action == 3:
            enemy_action = random.randrange(magic_min, magic_max)
        # endif
        return enemy_action

    def generate_player_dmg(self, action):
        """ Enemy's brain: generate damage for the player
            Generate randomly damage value
            input parameters:
                action - describes what action damage value to generate
            returns: player_damage -  player's damage value
        """
        if action == 1: # basic action
            player_damage = self.generate_dmg()
        elif action == 2: # Healing
            player_damage = self.healing()
        elif action == 3: # magic - Fire
            player_damage = self.generate_magic_damage()
        elif action == 4: # magic - Lightning
            player_damage = self.generate_magic_damage()
        elif action == 5: # magic - Hurricane
            player_damage = self.generate_magic_damage()
        elif action == 6:  # magic - Corona
            player_damage = self.generate_magic_damage()
        # endif
        return player_damage

""" define Magic class """
class Magic:
    name = "zZz"
    mp_cost = 1000
    dmg = 50
    type = "dark" # possible values are dark or light
    def __init__(self, name, type):
        self.name = name
        self.mp_cost = 100
        self.dmg = 50
        self.type = type

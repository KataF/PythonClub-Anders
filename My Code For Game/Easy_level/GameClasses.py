""" ##############################################################################
        This file includes all classes used in the game - Easy level
    ##############################################################################"""

# import random library
import random

""" define person class """
class person:
    name = "xXx"
    hp = 500
    max_hp = hp
    mp = 0
    max_mp = mp
    atk_high = 0
    atk_low = 0
    """ This function will initialize created person object """
    def __init__(self, name, hp, mp, atk):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Attack"]

    def get_stat(self):
        """ This function will print out player's/enemy's name and statistics of HP/MaxHP, MP/MaxMP
            input parameters:
                None
            returns: None
        """
        print("\t\t\t {}\'s,".format(self.name))
        print("\t\t\t health points are {}/{}".format(self.hp, self.max_hp))
        print("\t\t\t magic points are {}/{}".format(self.mp, self.max_mp))


    def generate_dmg(self, atk):
        """ This function calculates a attack damage value randomly between atk_high and atk_low.
            player or enemy generates damage to other one
            input parameters:
                atk - chosen attack action
            returns: damage_value - attack's damage value
        """
        damage_value = 0
        if atk == 1:
            damage_value = random.randrange(self.atk_low, self.atk_high)
        elif atk == 9:
            """ this value gives player to chance to stop game whenever she/he wants """
            damage_value = 5000
        """ elif:  Future actions """
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
        print("\t\t\t 9 - exit")
        atk = int(input('\t\t\t '))
        return atk

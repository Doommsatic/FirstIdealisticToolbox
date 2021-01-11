import variables
import random


def attack(atk, block=0):
    return (max(1, (random.randrange(18, 25) + atk) - block))


def youattack():
    pcdamage = attack(variables.pcatk, variables.modef)
    variables.moshp = variables.moshp - pcdamage
    print("You do " + str(pcdamage) + " damage to the monster, it is now at " +
          str(max(0, (variables.moshp))) + " health")
    if variables.moshp <= 0:
        print("The monster FUCKING dies")
        variables.dead = True


def theyattack():
    modamage = attack(variables.moatk, variables.pcdef + variables.tempdef)
    variables.pchp = variables.pchp - modamage
    print("The monster does " + str(modamage) +
          " damage to you, you are now at " + str(max(0, (variables.pchp))) +
          " health")
    if variables.pchp <= 0:
        print("You FUCKING die")
        variables.dead = True

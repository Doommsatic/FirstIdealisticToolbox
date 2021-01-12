import variables
import attack
print("An evil monster appears in front of you!")

while variables.dead == False:
  print("attack, defend or pass?")
  action=input("Action: ")
  if action == "attack":
    attack.youattack()
    if variables.dead==True:
      break
  elif action == "defend":
    variables.tempdef=10
  else:
    print("You do nothing like an idiot")
    pass
  attack.theyattack()
  variables.tempdef=0
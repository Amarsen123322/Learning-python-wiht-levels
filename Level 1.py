#print("Welcome to the Level 1 game")
from importlib.metadata import pass_none

# 3 life
#Mistake
#life = 3
#while life > 0:
#    question = input("did you win or lose: ")
#    if question == "lose":
#        life -= 1
#        print("You lose")
#    elif question == "win":
#        print("You win")
 #       break
  #  else:
   #     print("You lost")

#correction

#life = 3

#while life > 0:
 #   question = input("Did you win or lose? ")

  #  if question == "lose":
   #     life -= 1
    #    print("You lose")
     #   print("Lives remaining:", life)

    #elif question == "win":
     #   print("You win")

    #else:
     #   print("Invalid input. Please enter win or lose.")

#print("Game Over")


#Error

#students = 5

#while students > 0:
#    question = int(input("Enter Student Score: "))
#    if question >= 50:
#        print("Pass")
#        students -= 1
#    else:
#        print("Fail")
#print("Student passed", students)

# Fixed Error

#students = 5
#passed = 0

#while students > 0:
#    question = int(input("Enter Student Score: "))

#    if question >= 50:
#        print("Pass")
#        passed += 1
#    else:
#        print("Fail")

#    students -= 1

#print("Students passed:", passed)

#Error

#games = ["Hanuman", "Wukong", "GTA", "God of War", "FIFA"]
#found = False
#question = input("name a game : ")
#for game in games:
#    if game == question:
#        found = True
#        print("game found")
#    else:
#        print("game not found")

#Fixed
#games = ["Hanuman", "Wukong", "GTA", "God of War", "FIFA"]

#found = False

#question = input("Name a game: ")

#for game in games:
#    if game == question:
#        found = True

#if found:
#    print("Game found")
#else:
#    print("Game not found")

#error

#enemy = 5
#defeated = 5

#while enemy > 0:
#    question = input("Did you defeat the enemy yes/no: ")
#    if question == "no":
#        print ("Enemy survived")
#    else:
#        print ("enemy Defeated")
#        enemy -= 1
#    print("enemies defeated : ", enemy)


#Fixed code
#enemy = 5
#defeated = 0

#while enemy > 0:
#    question = input("Did you defeat the enemy? yes/no: ")

#    if question == "yes":
#        print("Enemy defeated!")
#       defeated += 1
#        enemy -= 1

#    elif question == "no":
#        print("Enemy survived!")
#        enemy -= 1

#   else:
#        print("Invalid input")

#print("Enemies defeated:", defeated)

# Corrected
#portions = 3
#while portions > 0:
#    question = input("Use a potion? yes/no: ")
#    if question == "yes":
#        print("portion used")
#        portions -= 1
#    elif question == "no":
#        print("portion not used")
#    else:
#        print("Invalid input")
#print("no portion left")

# Error

#coins = 100

#while coins > 0:
#    question = input("Do you want to buy or skip coins: ")
#    if question == "buy":
#        coins -= 20
#        print("You buy coins.")
#    elif question == "skip":
#        print("skipped")
#    else:
#        print("Please enter either buy or skip")
#print("Game over")

#Fixed

#coins = 100

#while coins > 0:
#    question = input("Do you want to buy or skip? ")

#    if question == "buy":
#        if coins >= 20:
#            coins -= 20
#            print("You bought an item. Coins left:", coins)
#        else:
#            print("Not enough coins")

#    elif question == "skip":
#        print("Skipped")

#    else:
#        print("Please enter either buy or skip")

#print("Game Over")

#Error

#games = ["Hanuman", "Wukong", "GTA", "God of War", "FIFA"]
#for game in games:
#    if len(game) == 3:
#        print(game)

#corrected
#games = ["Hanuman", "Wukong", "GTA", "God of War", "FIFA"]

#matches = 0

#for game in games:
#    if len(game) > 3:
#        print(game)
#        matches += 1

#print("Games matched:", matches)


#Fixed

#enemies = [10, 25, 15, 30, 20]

#total_damage = 0

#for damage in enemies:
#    print("Damage:", damage)
#    total_damage += damage

#print("Total damage:", total_damage)

#Training Stamina

#Error

#Stamina = 100
#while Stamina > 0:
#    question = int(input("How much stamina did you use?: "))
#    left = 100 - question
#    if left > 50:
#        print("Strong")
#    elif left > 1:
#        print("Weak")
#    else:
#        print("Exhausted")
#print("Traning completed")

#Fixed
#stamina = 100

#while stamina > 0:
#    question = int(input("How much stamina did you use?: "))

#    stamina -= question

#    if stamina > 50:
#        print("Strong", stamina)
#    elif stamina > 0:
#        print("Tired", stamina)
#    else:
#        print("Exhausted")

#print("Training complete")
#error
#scores = [45, 72, 90, 33, 61, 88]
#pass = 0
#for score in scores:
#    if score > 50:
#        print("You win!")
#        pass += 1
#    elif score < 50:
#        print("You lose!")
#print ("Students passed:",pass)

#Fixed
#scores = [45, 72, 90, 33, 61, 88]

#passed = 0

#for score in scores:
#    if score >= 50:
#        print("Pass")
#        passed += 1
#    else:
#        print("Fail")

#print("Students passed:", passed)

#Find the Strongest Enemy
#Error
#enemies = [25, 70, 45, 90, 60, 30]
#for en in enemies:
#    if en > 90:
#        print("Strongest enemy health: ", en)

#Correct
enemies = [25, 70, 45, 90, 60, 30]
strongest = 0
for health in enemies:
    if health > strongest:
        strongest = health
print("Strongest enemy health:", strongest)

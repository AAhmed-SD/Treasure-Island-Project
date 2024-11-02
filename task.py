zprint(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1= input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n' ).lower()
if choice_1 == "left":
    choice_2 =  input('You\'re now at the lake'
                      'There is an island in the middle of the lake'
                      'Type "wait" to wait for a boat'
                      'Type "swim" to swim across\n').lower()
    if choice_2 == "wait":
        choice_3 = input('You have now arrived on the Island l'
                         'You have come across a building'
                         'There are three doors'
                         'Select "red", "yellow" or "blue"\n').lower()
        if choice_3 == "red":
            print("You have entered a room full of fire")
        elif choice_3 == "blue":
            print("You have selected a room full of beast")
        elif choice_3 == "yellow":
            print("You have entered a room full of treasure")
        else:
            print("You have entered a room that does not exist")
else: print("You have fallen in a hole, Game Over")



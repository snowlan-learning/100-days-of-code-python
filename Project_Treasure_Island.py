print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

# You're at a cross road. Where do you want to go? Type "left" or "right".

cross_roads = input("You stand at an enigmatic crossroads under the soft glow of a crescent moon. An aged signpost marks two diverging trails: one veers to the left, the other to the right. Which course will you chart? Type 'left' or 'right': ")

if cross_roads.lower() == "left":
    print("Heart pounding, you wander down the path to the left. The overarching branches finally part, revealing a clearing bathed in moonlight. A mesmerizing lake unfurls before you, its placid waters reflecting the celestial sky.")
    cross_roads = input("A quaint wooden pier extends over the silvery liquid expanse. Do you venture into the lake for a swim or opt to savor the moment on the pier? Type 'swim' or 'wait': ")
    if cross_roads.lower() == "wait":
        print("You settle onto the pier, allowing your senses to fully absorb the surrounding natural beauty. Time seems to suspend itself, and then something miraculous transpires...")
        print("In a flash of ethereal light, you find yourself facing a triad of mystical doors.")
        door = input("Pick one of the three doors that beckon you. Type 'green', 'yellow', or 'blue': ")
        if door.lower() == "green":
            print("GAME OVER: Engulfed by malevolent creatures.")
        elif door.lower() == "yellow":
            print("Congratulations: You unearth an unimaginable treasure!")
        elif door.lower() == "blue":
            print("GAME OVER: Swept away by a torrential flood.")
        else: 
            print("Indecision grips you, and you select an option not given. Your inability to choose leaves you ensnared at the crossroads, forever trapped between possibilities.")
    elif cross_roads.lower() == "swim":
        print("GAME OVER: Your tranquil swim takes a tragic turn. An unseen aquatic beast strikes, leaving you grievously wounded and far from aid.")
    else:
        print("Indecision grips you, and you select an option not given. Your inability to choose leaves you ensnared at the crossroads, forever trapped between possibilities.")
elif cross_roads.lower() == "right":
    print("GAME OVER: As you amble down the rightward path, disaster strikes. Unseen thieves pilfer your essential belongings like your cherished treasure map, rendering you lost and powerless. Your quest meets an untimely demise.")
else:
    print("Indecision grips you, and you select an option not given. Your inability to choose leaves you ensnared at the crossroads, forever trapped between possibilities.")
player_hp = 100
player_name = " John"
print("narator: you are" + player_name)
print("narator: Hello, " + player_name + "! Welcome to the game.")

print("narator: You are going to the store")

money = 100
print("narator: You have " + str(money) + " dollars.")

sword_price = 50

print("narator: you can buy a sword")
print("narator: The sword costs " + str(sword_price) + " dollars.")
print("narator: You can buy a sword for " + str(sword_price) + " dollars.")
print("narator: you bought a sword")
money = money - sword_price
sentence = "narator: You have " + str(money) + " dollars left."
print(sentence)

player_choice = input("Do you want to fight level on zombies? (yes/no): ")
if player_choice.lower() == "yes":
    print("narator: You chose to fight level one zombies.")
    print("narator: You are fighting level one zombies.")
    print("narator: You won the fight!")
    print("narator: You earned 50 dollars.")
    money = 100
    print("narator: You have " + str(money) + " dollars now.")
else: 
    print("narator: You chose not to fight level one zombies.")
    player_choice = input("Do you want to go home? (yes/no): ")
if player_choice.lower() == "yes":
    print("narator: You chose to go home.")
    player_choice = input("Do you want to go to sleep or to the store (store/sleep): ")
    if player_choice.lower() == "sleep":
        print("narator: You chose to go to sleep.")
        print("narator: It is now morning.")
        
    else:
        print("narator: You chose to go to the store.")
        print("narator: You are at the store.")
        print("narator: You can buy a sword.")
        print("narator: you will now speak to the shopkeeper.")
        print("shopkeeper: Hello, " + player_name + "! Welcome to the store.")
        print("shopkeeper: You can buy a sword for " + str(sword_price) + " dollars.")
        print("or you can buy a shield for 30 dollars")
        player_choice = input("Do you want to buy a sword or a shield? (sword/shield): ")
        if player_choice.lower() == "sword":
            print("shopkeeper: You chose to buy a sword.")
            print("shopkeeper: You bought a sword for " + str(sword_price) + " dollars.")
            money = money - sword_price
            print("shopkeeper: You have " + str(money) + " dollars left.")
        if player_choice.lower() == "shield":
            print("shopkeeper: You chose to buy a shield.")
            print("shopkeeper: You bought a shield for 30 dollars.")
            money = money - 30
            print("shopkeeper: You have " + str(money) + " dollars left.")

        player_choice = input("Do you want to fight level one zombies? (yes/no): ")
        if player_choice.lower() == "yes":
            print("narator: You chose to fight level one zombies.")
            print("narator: You are fighting level one zombies.")
            print("narator: You won the fight!")
            print("narator: You earned 50 dollars.")
            money = money + 50
            player_choice = input("Do you want to fight level two zombies? (yes/no): ")
            if player_choice.lower() == "yes":
                print("narator: You chose to fight level two zombies.")
                print("narator: You are fighting level two zombies.")
                print("narator: You won the fight!")
                print("narator: You earned 100 dollars.")
                money = money + 100
                print("narator: You have " + str(money) + " dollars now.")

          
            else:
                print("narator: You chose not to fight level two zombies.")
                player_choice = input("Do you want to go home? (yes/no): ")
                if player_choice.lower() == "yes":
                    print("narator: You chose to go home.")
                    player_choice = input("Do you want to go to sleep or to the store (store/sleep): ")
                    if player_choice.lower() == "sleep":
                        print("narator: You chose to go to sleep.")
                        print("narator: It is now morning.")
                    else:
                        print("narator: You chose to go to the store.")
                        print("narator: You are at the store.")
                        print("narator: You can buy a sword.")
                        print("narator: you will now speak to the shopkeeper.")
                        print("shopkeeper: Hello, " + player_name + "! Welcome to the store.")
                        print("shopkeeper: You can buy a sword for " + str(sword_price) + " dollars.")
            print("narator: You have " + str(money) + " dollars now.")
            if player_choice.lower() == "yes":
                    print("narator: You chose to go to the store.")
                    print("narator: You are at the store.")
                    print("narator: you will now speak to the shopkeeper.")
                    print("shopkeeper: Hello, " + player_name + "! Welcome to the store.")
                    print("shopkeeper: You can buy a sword upgrade for " + str(sword_price) + " dollars.")
                    print("or you can buy a shield for 30 dollars")
                    player_choice = input("Do you want to buy a sword or a shield? (sword/shield): ")
                    if player_choice.lower() == "sword upgrade":
                        player_choice = input("Do you want to buy anything else? (yes/no): ")
                    if player_choice.lower() == "shield":
                        print("shopkeeper: Sorry, but you already own this item.")
                    if player_choice.lower() == "sword":
                        money = money - sword_price
                        print("narator: You bought a sword upgrade for " + str(sword_price) + " dollars.")
                        print("narator: You have " + str(money) + " dollars left.")
                        print("narator: You can now fight level three zombies.")
                        money = money - sword_price
                        player_choice = input("Do you want to fight level three zombies? Or level four (four/three): ")
                        if player_choice.lower() == "three":
                            print("narator: You chose to fight level three zombies.")
                            print("narator: You are fighting level three zombies.")
                            print("narator: You won the fight!")
                            print("narator: You earned 150 dollars.")
                            money = money + 150
                            print("narator: You have " + str(money) + " dollars now.")
                        if player_choice.lower() == "four":
                            print("narator: You chose to fight level four zombies.")
                            print("narator: You are fighting level four zombies.")
                            print("narator: You took 50 damage!")
                            player_hp = player_hp - 50
                            print("narator: You have " + str(player_hp) + " hp left.")
                            print("narator: You won the fight!")
                            print("narator: You earned 200 dollars.")
        else:
            print("narator: You chose not to fight level one zombies.")
            player_choice = input("Do you want to go home? (yes/no): ")
            if player_choice.lower() == "no":
                print("narator: You chose not to go home.")
                player_choice = input("Do you want to go to the store? (yes/no): ")
                if player_choice.lower() == "yes":
                    print("narator: You chose to go to the store.")
                    print("narator: You are at the store.")
                    print("narator: You can buy a sword.")
                    print("narator: you will now speak to the shopkeeper.")
                    print("shopkeeper: Hello, " + player_name + "! Welcome to the store.")
                    print("shopkeeper: You can buy a sword for " + str(sword_price) + " dollars.")
                else:
                    print("narator: You chose not to go to the store.")
            if player_choice.lower() == "yes":
                print("narator: You chose to go home.")
                player_choice = input("Do you want to go to sleep or to the store (store/sleep): ")
                if player_choice.lower() == "sleep":
                    print("narator: You chose to go to sleep.")
                    print("narator: It is now morning.")
                else:
                    print("narator: You chose to go to the store.")
                    print("narator: You are at the store.")
                    print("narator: You can buy a sword.")
                    print("narator: you will now speak to the shopkeeper.")
                    print("shopkeeper: Hello, " + player_name + "! Welcome to the store.")
                    print("shopkeeper: You can buy a sword for " + str(sword_price) + " dollars.")
                    print("or you can buy a shield for 30 dollars")
                    player_choice = input("Do you want to buy a sword or a shield? (sword/shield): ")

                    if player_choice.lower("sword"):
                        print("shopkeeper: Sorry, but you already own this item.")

                    if player_choice.lower("shield"):
                        player_choice = input("Do you want to fight level one zombies? (yes/no): ")

                        if player_choice.lower() == "yes":
                            print("narator: You chose to fight level one zombies.")
                            print("narator: You are fighting level one zombies.")
                            print("narator: You won the fight!")
                            print("narator: You earned 50 dollars.")
                            money = money + 50
                            player_choice = input("Do you want to fight level two zombies? (yes/no): ")
                            player_choice = input("Do you want to go to the store? (yes/no): ")
                if player_choice.lower() == "yes":
                    print("narator: You chose to go to the store.")
                    print("narator: You are at the store.")
                    print("narator: you will now speak to the shopkeeper.")
                    print("shopkeeper: Hello, " + player_name + "! Welcome to the store.")
                    print("shopkeeper: You can buy a sword upgrade for " + str(sword_price) + " dollars.")
                    print("or you can buy a shield for 30 dollars")
                    player_choice = input("Do you want to buy a sword or a shield? (sword/shield): ")
                    if player_choice.lower() == "sword upgrade":
                        player_choice = input("Do you want to buy anything else? (yes/no): ")
                    if player_choice.lower() == "shield":
                        print("shopkeeper: Sorry, but you already own this item.")
                    if player_choice.lower() == "sword":
                        money = money - sword_price
                        print("narator: You bought a sword upgrade for " + str(sword_price) + " dollars.")
                        print("narator: You have " + str(money) + " dollars left.")
                        print("narator: You can now fight level three zombies.")
                        player_choice = input("Do you want to fight level three zombies? Or level four (four/three): ")
                        if player_choice.lower() == "three":
                            print("narator: You chose to fight level three zombies.")
                            print("narator: You are fighting level three zombies.")
                            print("narator: You won the fight!")
                            print("narator: You earned 150 dollars.")
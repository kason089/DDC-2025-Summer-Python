# 🐶 Day 4: Virtual Pet Simulator

"""
👾 Welcome to Code Island’s Virtual Pet Challenge!

Today you’ll build a pet simulator where players can take care of a digital pet.
They’ll feed it, play with it, and keep it alive and happy using Python code!

🔍 What you’ll practice:
- Using variables to track your pet’s status (like hunger or happiness)
- Using loops to keep your program running
- Using `if` statements to react to the player’s actions

🐾 Game Idea:
You adopt a virtual pet — a dog, cat, alien, or anything silly!
Players must keep it alive by choosing actions like FEED, PLAY, or REST.
If they ignore it or make bad choices, the pet gets sad or runs away!

🎨 Remix Challenges (do at least 2–3):
✅ Let the user choose their pet’s name and type
✅ Add a “happiness” or “energy” meter
✅ Add a timer (limited rounds)
✅ Use `random.choice()` to add surprises (like "Your pet found a toy!")
✅ Add ASCII art or emoji to show how the pet feels 🥹😎🥴
✅ Add a restart or game over loop

📸 When You Finish:
- Let someone else try to take care of your pet
- Show off your best pet survival record
- Submit your `.py` file or Replit link
"""

# 🐾 Starter Code
print("🐾 Welcome to the Virtual Pet Game!")
name = input("What would you like to name your pet? ")
pet_type = input("What kind of pet is it? (dog, cat, alien, etc): ")

hunger = 5  # 0 is full, 10 is starving
happiness = 5  # 0 is sad, 10 is super happy
energy = 5
skills = 0
wins = 0
contest_level = 5

print(f"\nYou adopted a {pet_type} named {name}! Take good care of it.")

# Game loop (runs for 10 turns)
for turn in range(10000000000000000000000000000):
    print('----------------------------------------------------')
    print("\nWhat would you like to do?")
    print(f"energy = {energy}")   
    print(f"hunger = {hunger}")     
    print(f"happiness = {happiness}")
    print(f"skill level = {skills}")
    print(f"wins = {wins}")
    print("1 - Feed")
    print("2 - Play")
    print("3 - rest")
    print("4 - Do nothing")
    print("5 - training")
    print('6 - pet contest')
    print('7 - retire')
    choice = input("Enter the number of your choice: ")
    

    if choice == "1":
        hunger = max(0, hunger - 2)
        energy = min(50, energy + 2)
        print('----------------------------------------------------')
        print(f"You fed {name}.")
    elif choice == "2": 
        if energy <= 0:
            print('----------------------------------------------------')
            print(f"{name} is too tired to play.😴")
        elif hunger >=10:
            print('----------------------------------------------------')
            print(f'{name} too hungery to play.🍖')
        else:
            happiness = min(10, happiness + 2)
            hunger = min(10, hunger + 1)  # playing makes it hungry
            energy = max(0, energy - 2)
            print('----------------------------------------------------')
            print(f"You played with {name} .")
    elif choice == "3":
        energy = min(10, energy + 3)
        hunger = min(10, hunger + 2)
        happiness = min(10, happiness - 2)
        print('----------------------------------------------------')
        print (f"{name} got some sleep but got hungery and bored.")
    elif choice == "4":
        hunger = min(10, hunger + 2)
        happiness = max(0, happiness - 2)
        print('----------------------------------------------------')
        print(f"You did nothing. {name} looks bored and hungry... 😢")
    elif choice == "44":
        hunger = min(10, hunger + 1000)
        happiness = min(0, happiness - 1000)
        energy = min(0, energy - 1000)
        print('----------------------------------------------------')
        print (f"You have left {name} to rot... look at what you did... 💀")    
        break
    elif choice == "top 1":
        skills = min(55000000, skills + 55000000)
        print('----------------------------------------------------')
        print(f'{name} is now top 1.')
    elif choice == "5":
        if energy <= 0:
            print('----------------------------------------------------')
            print(f"{name} is to tired to train.😴")
        elif hunger >=10:
            print('----------------------------------------------------')
            print(f'{name} too hungery to train.🍖')
        else: 
            skills = min(55000000, skills + 1)
            hunger = min(10, hunger + 2)
            energy = max(0, energy -5)
            print('----------------------------------------------------')
            print(f"{name} started training...💪")
    elif choice == "above all":
        wins = min(10000000000000000, wins + 10000000000000000)
        print('----------------------------------------------------')
        print(f'{name} is above all')
    elif choice == "6":
        if energy <= 0:
            print('----------------------------------------------------')
            print(f"{name} is too tired to compete.😴")
        elif hunger >=10:
            print('----------------------------------------------------')
            print(f'{name} too hungery to compete.🍖')
        else:
            if skills <= contest_level:
                print('----------------------------------------------------')
                print(f"{name} didn't win, skill is to low. (required skill level = {contest_level})")
            elif skills >= contest_level:
                wins = min(10000000000000000, wins + 1)
                contest_level = min(50000000, contest_level + 5)
                print('----------------------------------------------------')
                print(f"{name} has won the pet contest!🏆")
    elif choice == "7":
        if wins <= 10:
            print('----------------------------------------------------')
            print(f'not enough wins to retire. ({wins}/10) ')
        else:
            print('----------------------------------------------------')
            print(f'you have retired with {wins} wins.')
            break
    else:
        print('----------------------------------------------------')
        print("Invalid choice. Nothing happens.")

# End of game
print('----------------------------------------------------')
print("\n🧾 Game Over!")
if hunger >= 10 and happiness <= 0 and energy <= 0:
    print('----------------------------------------------------')
    print(f"{name} has been left to die alone... ⚰️")
    print('----------------------------------------------------')
else:
    print('----------------------------------------------------')
    print(f"You and {name} have retired with {wins} wins! 🎉")
    print('----------------------------------------------------')
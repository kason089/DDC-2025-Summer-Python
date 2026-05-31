# 🛂 Digital Passport to Code Island!
print("🌴🏝️ Welcome to Code Island! 🏝️🌴")
print("Before you begin your journey, let's create your DIGITAL PASSPORT.\n")

# Collect basic info
name = input("👤 What's your full name? ")
age = input("🎂 How old are you? ")
emoji = input("😄 What's your favorite emoji? ")
color = input("🎨 What's your favorite color? ")
dream_job = input("💼 What's your dream job? ")
code_name = input("🕵️‍♂️ Choose a cool code name for your passport: ")
island = input("🏖️ Name a magical island you'd love to visit: ")
petsyn = input("😸 Did you bring any pets with you yes/no? ")
pet = input("🦙 if you do have a pet what kind of pet? ")


# Generate passport
print("\n🔒 Generating your secure passport...\n")
print("=========================================")
print("          🌐 CODE ISLAND PASSPORT        ")
print("=========================================")
print(f"👤 Name: {name}")
print(f"🆔 Code Name: {code_name}")
print(f"🎂 Age: {age}")
print(f"🎨 Favorite Color: {color}")
print(f"💼 Dream Job: {dream_job}")
print(f"🌴 Dream Island: {island}")
print(f"😎 Emoji ID: {emoji}")
print(f"😸 pet on board: {petsyn}") 
print(f"🦙 pet type: {pet}")
print("=========================================")
print("🌟 You're now an official explorer of Code Island! 🌟\n")

# Bonus stamps
stamps = ["🌺", "🐚", "🦜", "🌊", "🍍"]
print("🔖 Stamping your passport...")
for s in stamps:
    print(f"{s} ", end="")
print("\n\n✔️ All set! Enjoy your journey.\n")

# ==========================
# 🛠️ YOUR TURN TO CUSTOMIZE!
# ==========================
# Add your own fun facts or sections to the passport here:

# 👉 Example:
hobby = input("🕹️ What's your favorite hobby? ")
game = input("🎮 What's your favorite video game? ")
food = input("🍔what's your favorite food? ")
holiday = input("🎄 what's your favorite holiday? ")
sportstype = input("(⚽ what is your favorite sport? ")
sportslike = input("🏉 what do you like about that sport? ")

# Print custom section
print("===== BONUS INFO =====")
print(f"🎨 Hobby: {hobby}")
print(f"🎮 Favorite Game: {game}")
print(f"🍔 favorate food: {food}")
print(f"🎄 favorite holiday: {holiday}")
print(f"🏐 favorite sport: {sportstype}")
print(f"🏀 reason for liking {sportstype}: {sportslike}")
print("======================")

# CHALLENGE: Add at least 2 more sections below!
# For example: favorite snack, favorite animal, favorite song, etc.

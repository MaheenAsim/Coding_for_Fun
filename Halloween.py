import time
import random

# A list of Halloween phrases for spooky vibes
phrases = [
    "BOO! Did I scare you? 👻",
    "It's spooky season! 🎃",
    "Happy Halloween! 🍬",
    "Beware the witching hour! 🧙‍♀️",
    "Are you afraid of the dark? 🌑",
]

# Function to print the ghost scene
def print_ghost_scene():
    ghost = """
          .-.
         (o o) Boo!
         | O |
        _/`-`\\_
      _/       \\_
     /           \\
    """
    print(ghost)

# Halloween decorations
def halloween_decor():
    print("🕸️🎃🕸️" * 5)

#.,. Halloween greeting
def halloween_greeting():
    halloween_decor()
    print("\nWelcome to the Haunted House!\n")
    time.sleep(1)
    print_ghost_scene()
    time.sleep(1)
    print(random.choice(phrases))
    halloween_decor()

# a trick or treat
def ask_for_trick_or_treat():
    name = input("What’s your name, brave soul? ")
    time.sleep(1)
    choice = input(f"Hello {name}! Do you want a 'trick' or 'treat'? ").lower()
    
    if choice == "treat":
        print(f"\n🎉 Sweet treats for you, {name}! 🍫🍬🍭 Enjoy the Halloween goodies!")
    elif choice == "trick":
        print(f"\n😈 Oh, a brave one, huh? Prepare for a spooky surprise, {name}!")
        time.sleep(1)
        print("Did you hear that? 👻")
        time.sleep(1)
        print("Something's right behind you...")
        time.sleep(1)
        print("BOO!")
    else:
        print("\n😜 Only the brave get the candy! Pick 'trick' or 'treat' next time!")

# Run the Halloween greeting and ask for trick or treat
halloween_greeting()
ask_for_trick_or_treat()

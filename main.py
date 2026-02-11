import sys, random

print("Welcoe to the Psych `SideKick Name Picker.\n")
print("A name just like Sean would pick for Gus:\n\n")

first = (
    "Zaphod",
    "Moonbeam",
    "Fizban",
    "Glimmer",
    "Tiberius",
    "Banana",
    "Clementine",
    "Orville",
    "Pippin",
    "Nimbus"
)

last = (
    "Beeblebrox",
    "Twistypop",
    "Snickerdoodle",
    "Funkle",
    "Quackenbush",
    "Wobbleton",
    "Sprocket",
    "Bumbleshoot",
    "Flapjack",
    "Cracklehorn"
)

while True:
    firstName = random.choice(first)

    lastName = random.choice(last)

    print("\n\n")
    print("{}{}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry Again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")
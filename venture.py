from blaster import Blaster
from binaryQuest import Binary

print("Howdy there, captain! My name is SCOR, the mechanical navigator of the SS...")
shipName = input("Huh, that's weird... what was the ship's name again? ")      
print(f"Ah, that's right. The mighty {shipName}. Beautiful birdie, isn't she?")

beautyBird = Binary()
if (beautyBird.which == True):
    print("Truly, truly a work of art. Good taste, mate.")
if (beautyBird.which == False):
    print("Bit rude, ain't ya?")
capName = input("What're you called, anywho? ")
print(f"Aye, aye, Captain {capName}! Welcome to the crew, mate.")



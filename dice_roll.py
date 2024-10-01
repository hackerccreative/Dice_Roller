from random import randint as r
import os
import time
from playsound import playsound
import threading
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_dice(a):
    dice_faces = {
        1: ["⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜",
            "⬜⬜🔴⬜⬜",
            "⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜"],
        2: ["⬜⬜⬜⬜⬜",
            "⬜🔴⬜⬜⬜",
            "⬜⬜⬜⬜⬜",
            "⬜⬜⬜🔴⬜",
            "⬜⬜⬜⬜⬜"],
        3: ["⬜⬜⬜⬜⬜",
            "⬜🔴⬜⬜⬜",
            "⬜⬜🔴⬜⬜",
            "⬜⬜⬜🔴⬜",
            "⬜⬜⬜⬜⬜"],
        4: ["⬜⬜⬜⬜⬜",
            "⬜🔴⬜🔴⬜",
            "⬜⬜⬜⬜⬜",
            "⬜🔴⬜🔴⬜",
            "⬜⬜⬜⬜⬜"],
        5: ["⬜⬜⬜⬜⬜",
            "⬜🔴⬜🔴⬜",
            "⬜⬜🔴⬜⬜",
            "⬜🔴⬜🔴⬜",
            "⬜⬜⬜⬜⬜"],
        6: ["⬜⬜⬜⬜⬜",
            "⬜🔴⬜🔴⬜",
            "⬜🔴⬜🔴⬜",
            "⬜🔴⬜🔴⬜",
            "⬜⬜⬜⬜⬜"]
    }
    print(a)
    for line in dice_faces[a]:
        print(line)

def play_sound():
    playsound('dice_roll.mp3')
    

def roll_dice():
    sound_thread = threading.Thread(target=play_sound)
    sound_thread.start()

    for _ in range(10):
        a = r(1, 6)
        clear_console()
        print_dice(a)
        time.sleep(0.05 + i / 50)
    sound_thread.join()
    return a


clear_console()
print("*"*51)
print(" "*19,"DICE ROLLER")
print("*"*51)
print("\nGet ready...")
for i in range(3, 0, -1):
    print(i, "...")
    time.sleep(1)
while True:
    clear_console()
    final_number = roll_dice()
    clear_console()
    print("Final roll:")
    print_dice(final_number)

    x = input("Choose 'y' for roll again / 'n' for exit: ")
    if (x == 'n'):
        break

print("*"*7,"Thanks for choosing me as your dice.","*"*7,end="*")
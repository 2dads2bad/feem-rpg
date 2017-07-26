import pyglet
import os

SOUND_DIR = "data/sound/"
SOUNDS = dict()
for filename in os.listdir(SOUND_DIR):
    SOUNDS[filename[:-4]] = pyglet.media.load(SOUND_DIR + filename, streaming=False)

print("Hello, this is a wrapper for testing feem-rpg modules.")

doFeem = True
while doFeem:
    cmnd = input("What would you like to do?\n").lower()
    
    if cmnd == "help":
        print(open("HELP", "r").read()[:-1])
        SOUNDS["tap"].play()
        
    elif cmnd in ("quit", "exit", "stop", "goodbye", "please no more"):
        print("Well, goodbye!")
        doFeem = False
        
    elif cmnd == "honk":
        print("Honk honk honk!")
        SOUNDS["breathe"].play()
        
    else:
        print("I don't recognize that command. Try 'help'.")
        SOUNDS["snap"].play()

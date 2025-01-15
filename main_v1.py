import subprocess
import time
import pychrome
from pynput import keyboard
import threading
import random

browser = pychrome.Browser(url="http://127.0.0.1:1234")
print(__file__)
tab = browser.new_tab("chrome://dino")
tab.start()

def on_press(key):
    global tab
    try:
        if key.char == 'k':
            tab.Runtime.evaluate(expression="Runner.instance_.gameOver()")
        elif key.char =='c':
            tab.Runtime.evaluate(expression="Runner.instance_.horizon.addCloud()")
        elif key.char == "g":
            tab.Runtime.evaluate(expression="Runner.instance_.tRex.groundYPos=0")
        elif key.char == "f":
            tab.Runtime.evaluate(expression="Runner.instance_.tRex.flashing=true")
        elif key.char == "r":
            tab.Runtime.evaluate(expression="Runner.instance_.activated=false")
        elif key.char == "s":
            tab.Runtime.evaluate(expression="Runner.instance_.setArcadeMode()")
        elif key.char == "t":
            tab.Runtime.evaluate(expression="Runner.instance_.playingIntro=true")

    except:
        print("oshibka!")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


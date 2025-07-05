from time import sleep
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Listener, Button, Controller as MouseController

TIME_TO_WAIT = 0.01
bToggleCopy = True  # bool - toggle copy and paste

bIsWorking = False 

keyboard = KeyboardController()
mouse = MouseController()

def key_press(key):
    keyboard.press(key)
    keyboard.release(key)
    sleep(TIME_TO_WAIT)

def key_hold(key):
    keyboard.press(key)
    sleep(TIME_TO_WAIT)

def key_release(key):
    keyboard.release(key)
    sleep(TIME_TO_WAIT)

def copy():
    key_hold(Key.ctrl)
    key_press('c')
    key_release(Key.ctrl)

def paste():
    key_hold(Key.ctrl)
    key_press('v')
    key_release(Key.ctrl)

def mouse_press(button, time_to_wait = TIME_TO_WAIT):
    mouse.press(button)
    mouse.release(button)
    sleep(time_to_wait)

def fun():
    global bToggleCopy

    mouse_press(Button.left)
    
    if bToggleCopy:
        copy()
        bToggleCopy = False
    else:
        paste()
        bToggleCopy = True

def on_click(x, y, button, pressed):
    global bIsWorking
    if not bIsWorking and pressed:
        if button == Button.middle:
            bIsWorking = True
            fun()
            bIsWorking = False
        elif button in [Button.right]:
            return False

def main():
    print("Program started. Press the middle mouse button to toggle copy/paste. "
          "Press right mouse button to exit.")
    with Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()

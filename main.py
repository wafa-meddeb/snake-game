from pynput.keyboard import Key, Controller
import time
import pynput.keyboard
keyboard = Controller()
time.sleep(10)
keyboard.press(Key.right)
time.sleep(5)
keyboard.release(Key.right)


import pyautogui
import pynput
from pynput.keyboard import Key, Controller   #to control the keyboard
import pyscreeze
import PIL


grid_height = 531
grid_width = 545
step_x = grid_width / 17   #number of pixels by square
step_y = grid_height / 15  #number of pixels by square

x_food, y_food = pyautogui.locateCenterOnScreen("apple.PNG", grayscale=True, confidence=0.2)  #search the screen for the coordinalities of the apple
print("x_food =", x_food)
print("y_food =", y_food)
x_head, y_head = pyautogui.locateCenterOnScreen("snake_head.PNG", grayscale=True, confidence=0.9)  #search the screen for the coordinalities of the head of the snake
y_head = y_food
print("x_head =", x_head)
print("y_head =", y_head)
keyboard = Controller()    #to controle the keyboard
pyautogui.sleep(2)  #to give time for opening the game's window

while True:
    #conditions: directions
    print("itération")
    if  x_head < x_food:
        print("x_head=", x_head)
        print("x_food", x_food)
        pyautogui.press('right')
        print("right")
        x_head += step_x



    if y_head > y_food:
        print("y_head=", y_head)
        print("y_food", y_food)
        pyautogui.press('up')
        print("up")
        y_head -= step_y



    if y_head < y_food:
        print("y_head=", y_head)
        print("y_food", y_food)
        pyautogui.press('down')
        print("down")
        y_head += step_y



    if x_head > x_food:
        print("x_head=", x_head)
        print("x_food", x_food)
        pyautogui.press('left')
        print("left")
        x_head -= step_x

    pyautogui.sleep(0.05)





























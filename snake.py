from pynput.keyboard import Key, Controller
import time
import pyautogui
import pynput.keyboard


def go_up():
    while Fy < Snake[-1][1] :
        # y-=1
        new_position = [snake[-1][0], snake[-1][1]-1]
        snake.append(new_position)
        snake.remove(snake[0])


def go_right():
    while Fx > Snake[-1][0] :
        # x += 1
        new_position = [snake[-1][0] + 1, snake[-1][1]]
        snake.append(new_position)
        snake.remove(snake[0])


def go_left():
    while Fx < Snake[-1][0]:
        # x -= 1
        new_position = [snake[-1][0] - 1, snake[-1][1]]
        snake.append(new_position)
        snake.remove(snake[0])


def go_down():
    while Fy > Snake[-1][1]:
        # y+= 1
        new_position = [snake[-1][0], snake[-1][1]+1]
        snake.append(new_position)
        snake.remove(snake[0])


grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
snake = [[3, 8], [4, 8], [5, 8]]
food = [13, 8]
Fx = food[0]
Fy = food[1]

keyboard = Controller()
time.sleep(5)
keyboard.press(Key.right)

if Fx < Snake[-1][0]:
    go_left()
if Fx > Snake[-1][0]:
    go_right()
if Fy > Snake[-1][1]:
    go_down()
if Fy < Snake[-1][1]:
    go_up()












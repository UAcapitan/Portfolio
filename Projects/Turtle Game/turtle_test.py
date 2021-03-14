from turtle import Screen, Turtle
import random
import keyboard
import time
import mysql.connector
from tkinter import *

# Запрос имени
name = input('Name: ')
print()

# Объект для окна
screen = Screen()

# Объекты для игроков
t = Turtle()
t1 = Turtle()
t2 = Turtle()
t1.color('green')
t2.color('orange')

# Таймер
time_start_game = time.time()

# Счёт
points_player = 0

# Счёт в конце игры
points = 0

# Переменные
x = 0
y = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
arr_coordinates_player = []
arr_coordinates_t1 = []
arr_coordinates_t2 = []
arr_coordinates = []

# Функция нажатия кнопки вверх
def up():
    global y
    global arr_coordinates
    global arr_coordinates_t1
    global arr_coordinates_t2
    y += 10
    t.goto(x,y)
    arr_coordinates = arr_coordinates_player + arr_coordinates_t1 + arr_coordinates_t2
    check_coordinates()
    arr_coordinates_player.append([x,y])
    opponents_move()

# Функция нажатия кнопки вниз
def down():
    global y
    global t1
    global arr_coordinates
    global arr_coordinates_t1
    global arr_coordinates_t2
    y -= 10
    t.goto(x,y)
    arr_coordinates = arr_coordinates_player + arr_coordinates_t1 + arr_coordinates_t2
    check_coordinates()
    arr_coordinates_player.append([x,y])
    opponents_move()

# Функция нажатия кнопки вправо
def right():
    global x
    global arr_coordinates
    global arr_coordinates_t1
    global arr_coordinates_t2
    x += 10
    t.goto(x,y)
    arr_coordinates = arr_coordinates_player + arr_coordinates_t1 + arr_coordinates_t2
    check_coordinates()
    arr_coordinates_player.append([x,y])
    opponents_move()

# Функция нажатия кнопки влево
def left():
    global x
    global arr_coordinates
    global arr_coordinates_t1
    global arr_coordinates_t2
    x -= 10
    t.goto(x,y)
    arr_coordinates = arr_coordinates_player + arr_coordinates_t1 + arr_coordinates_t2
    check_coordinates()
    arr_coordinates_player.append([x,y])
    opponents_move()

# Функция для проверки нету ли столкновения
def check_coordinates():
    if [x,y] in arr_coordinates or x > 310 or x < -310 or y > 250 or y < -250:
        stop_game()
        screen.clear()

# Функция поведения соперников
def opponents_move():
    global x1
    global y1
    global t1
    global x2
    global y2
    global t2
    global arr_coordinates
    global arr_coordinates_t1
    global arr_coordinates_t2

    arr_coordinates = arr_coordinates_player + arr_coordinates_t1 + arr_coordinates_t2

    possible_moves = []
    if ([x1+10,y1] in arr_coordinates) == False and x1+10 < 310:
        possible_moves.append(1)
    if ([x1-10,y1] in arr_coordinates) == False and x1-10 > -310:
        possible_moves.append(2)
    if ([x1,y1+10] in arr_coordinates) == False and y1+10 < 250:
        possible_moves.append(3)
    if ([x1,y1-10] in arr_coordinates) == False and y1-10 > -250:
        possible_moves.append(4)
    len_possible_moves = len(possible_moves)
    if len_possible_moves > 0:
        move_t1 = possible_moves[random.randint(0,len_possible_moves-1)]
        if move_t1 == 1:
            x1 += 10
        elif move_t1 == 2:
            x1 -= 10
        elif move_t1 == 3:
            y1 += 10
        elif move_t1 == 4:
            y1 -= 10
        t1.goto(x1,y1)
    else:
        arr_coordinates_t1 = []
        while ([x1,y1]) in arr_coordinates:
            x1 = (random.randint(-309,309) // 10) * 10
            y1 = (random.randint(-249,249) // 10) * 10
        points_update()
        t1.clear()
        t1.goto(x1,y1)
        t1.clear()

    possible_moves2 = []
    if ([x2+10,y2] in arr_coordinates) == False and x2+10 < 310:
        possible_moves2.append(1)
    if ([x2-10,y2] in arr_coordinates) == False and x2-10 > -310:
        possible_moves2.append(2)
    if ([x2,y2+10] in arr_coordinates) == False and y2+10 < 250:
        possible_moves2.append(3)
    if ([x2,y2-10] in arr_coordinates) == False and y2-10 > -250:
        possible_moves2.append(4)
    len_possible_moves2 = len(possible_moves2)
    if len_possible_moves2 > 0:
        move_t2 = possible_moves2[random.randint(0,len_possible_moves2-1)]
        if move_t2 == 1:
            x2 += 10
        elif move_t2 == 2:
            x2 -= 10
        elif move_t2 == 3:
            y2 += 10
        elif move_t2 == 4:
            y2 -= 10
        t2.goto(x2,y2)
    else:
        arr_coordinates_t2 = []
        while ([x2,y2]) in arr_coordinates:
            x2 = (random.randint(-309,309) // 10) * 10
            y2 = (random.randint(-249,249) // 10) * 10
        points_update()
        t2.clear()
        t2.goto(x2,y2)
        t2.clear()

    # Запись ходов соперников
    arr_coordinates_t1.append([x1,y1])
    arr_coordinates_t2.append([x2,y2])

# Увеличить количество очков на 100
def points_update():
    global points_player
    points_player += 100

# Сохранить результат
def save_results(name, points):
    f = open('results.txt', 'a')
    f.write('{} - {}\n'.format(name, points))
    f.close()

# Открыть результат
def open_results():
    f = open('results.txt', 'r')
    f_text = f.readlines()
    n = 0
    for i in f_text:
        if n > 9:
            break
        print(i)
        n += 1

# Остановить игру
def stop_game():
    global points
    time_end_game = time.time()
    time_played = time_end_game - time_start_game
    points = round((len(arr_coordinates_player) + points_player) / time_played, 1)
    screen.clear()
    save_results(name, points)
    open_results()
    screen._destroy()

# При нажатии кнопки будут использоваться нужные им функции
keyboard.add_hotkey('up',up)
keyboard.add_hotkey('down',down)
keyboard.add_hotkey('right',right)
keyboard.add_hotkey('left',left)

screen.mainloop()
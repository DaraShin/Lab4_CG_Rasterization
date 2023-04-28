from tkinter import Tk

from CircleResultsFrame import CircleResultsFrame
from ResultsFrame import ResultsFrame

import time

def step_by_step_method(start_x, start_y, end_x, end_y):
    points = []
    if abs(end_y - start_y) <= abs(end_x - start_x):
        if start_x > end_x:
            start_x, end_x = end_x, start_x
            start_y, end_y = end_y, start_y
        tg = (end_y - start_y) / (end_x - start_x)
        for x in range(start_x, end_x + 1):
            point = [x, int(round(tg * (x - start_x) + start_y))]
            points.append(point)
    else:
        if start_y > end_y:
            start_x, end_x = end_x, start_x
            start_y, end_y = end_y, start_y
        atg = (end_x - start_x) / (end_y - start_y)
        for y in range(start_y, end_y + 1):
            point = [int(round(atg * (y - start_y) + start_x)), y]
            points.append(point)
    return points


def dda_method(start_x, start_y, end_x, end_y):
    dx = end_x - start_x
    dy = end_y - start_y
    L = max(abs(dx), abs(dy))
    points = [[start_x, start_y]]
    x, y = start_x, start_y
    for i in range(L):
        x = x + dx / L
        y = y + dy / L
        points.append([int(round(x)), int(round(y))])
    return points


def bresenham_line(start_x, start_y, end_x, end_y):
    x_long = abs(end_x - start_x) >= abs(end_y - start_y)
    if not x_long:
        start_x, start_y = start_y, start_x
        end_x, end_y = end_y, end_x

    if end_x < start_x:
        start_x, end_x = end_x, start_x
        start_y, end_y = end_y, start_y

    dx = end_x - start_x
    dy = end_y - start_y
    sign_dy = 1 if dy >= 0 else -1

    x, y = start_x, start_y
    tg = dy / dx
    e = tg - sign_dy * 0.5
    points = [[start_x if x_long else start_y, start_y if x_long else start_x]]

    y_step = 1 if dy >= 0 else -1
    while x < end_x:
        if sign_dy * e >= 0:
            x += 1
            y += y_step
            e += tg - y_step
        else:
            x += 1
            e += tg
        points.append([x if x_long else y, y if x_long else x])
    return points


def put_circle_point(x, y, points, center_x, center_y):
    points.append([x + center_x, y + center_y])     # 2
    points.append([-x + center_x, y + center_y])    # 3
    points.append([x + center_x, -y + center_y])    # 7
    points.append([-x + center_x, -y + center_y])   # 6
    points.append([y + center_x, x + center_y])     # 1
    points.append([y + center_x, -x + center_y])    # 4
    points.append([-y + center_x, x + center_y])    # 8
    points.append([-y + center_x, - x + center_y])  # 5
    return points


def bresenham_circle(radius, center_x, center_y):
    x, y = 0, radius
    e = 3 - 2 * radius
    points = put_circle_point(x, y, [], center_x, center_y)

    while x < y:
        if e >= 0:
            e += 4 * (x - y) + 10
            x += 1
            y -= 1
        else:
            e += 4 * x + 6
            x += 1
        points = put_circle_point(x, y, points, center_x, center_y)
    return points


# start = time.time()
# step_by_step_method(0,0,1000000,1000000)
# end = time.time()
# print("Пошаговый алгоритм: " + str(end-start) + " с")
#
# start = time.time()
# dda_method(0,0,1000000,1000000)
# end = time.time()
# print("алгоритм ЦДА: " + str(end-start) + " с")
#
# start = time.time()
# bresenham_line(0,0,1000000,1000000)
# end = time.time()
# print("алгоритм Брезенхема: " + str(end-start) + " с")
#
# start = time.time()
# bresenham_circle(1000000,0,0)
# end = time.time()
# print("алгоритм Брезенхема(окружность): " + str(end-start) + " с")


window = Tk()
window.title('Lab 4. Basic raster algorithms')
window.geometry("1200x768")

step_frame_results = ResultsFrame(step_by_step_method, "Пошаговый алгоритм")
step_frame = step_frame_results.root_frame
step_frame.grid(row=0, column=0)

dda_frame_results = ResultsFrame(dda_method, "ЦДА")
dda_frame = dda_frame_results.root_frame
dda_frame.grid(row=0, column=1)

bresenham_frame_results = ResultsFrame(bresenham_line, "алгоритм Брезенхема")
bresenham_frame = bresenham_frame_results.root_frame
bresenham_frame.grid(row=1, column=0)

circle_frame_results = CircleResultsFrame(bresenham_circle, "алгоритм Брезенхема (окружность)")
circle_frame = circle_frame_results.root_frame
circle_frame.grid(row=1, column=1)

window.mainloop()

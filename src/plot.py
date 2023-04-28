import numpy as np
from matplotlib import pyplot as plt


def draw_rasterized_figure( points, title):
    x_min = min(point[0] for point in points)
    x_max = max(point[0] for point in points)
    y_min = min(point[1] for point in points)
    y_max = max(point[1] for point in points)

    width = round((x_max - x_min) * 1.2)
    width = width if width > x_max - x_min else x_max - x_min + 1
    height = round((y_max - y_min) * 1.2)
    height = height if height > y_max - y_min else y_max - y_min + 1

    img = np.empty((height, width, 3), np.uint8)
    img.fill(255)
    red = [255, 0, 0]

    for i in range(len(points)):
        img[points[i][1] - y_min, points[i][0] - x_min] = red

    fig, ax = plt.subplots(figsize=(width, height))

    # ticks_frequency = min(round(width / 10), round(height / 10))
    # ticks_frequency = 1 if ticks_frequency < 1 else ticks_frequency

    max_side = max(width, height)
    if max_side <= 10:
        ticks_frequency = 1
    elif max_side <= 20:
        ticks_frequency = 2
    elif max_side <= 50:
        ticks_frequency = 5
    elif max_side <= 100:
        ticks_frequency = 10
    else:
        ticks_frequency = 20

    left_x = x_min
    right_x = x_min + width
    bottom_y = y_min
    top_y = y_min + height

    ax.set(xlim=(left_x - ticks_frequency, right_x + ticks_frequency),
           ylim=(bottom_y - ticks_frequency, top_y + ticks_frequency), aspect='equal')

    if (left_x - ticks_frequency) * (right_x + ticks_frequency) < 0:
        x_ticks = np.concatenate((np.arange(0, left_x - ticks_frequency, -ticks_frequency),
                                  np.arange(0, right_x + ticks_frequency, ticks_frequency)))
    else:
        start = int((left_x - ticks_frequency) / ticks_frequency) * ticks_frequency
        x_ticks = np.arange(start, right_x + ticks_frequency, ticks_frequency)

    if (bottom_y - ticks_frequency) * (top_y + ticks_frequency) < 0:
        y_ticks = np.concatenate((np.arange(0, bottom_y - ticks_frequency, -ticks_frequency),
                                  np.arange(0, top_y + ticks_frequency, ticks_frequency)))
    else:
        start = int((bottom_y - ticks_frequency) / ticks_frequency) * ticks_frequency
        y_ticks = np.arange(start, top_y + ticks_frequency, ticks_frequency)

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-15, y=0.98, rotation=0)

    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    plt.title(title, pad=10)

    plt.imshow(img, origin='lower', extent=[left_x - 0.5, right_x - 0.5, bottom_y - 0.5, top_y - 0.5])

    return fig
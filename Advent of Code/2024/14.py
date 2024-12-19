import re
import cv2
import numpy as np
import os

robots = []
with open("input", "r") as file:
    for line in file:
        match = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line.strip())
        if match:
            x, y, dx, dy = map(int, match.groups())
            robots.append([x, y, dx, dy])

width = 101
height = 103
scale = 8
output_folder = "temp"
os.makedirs(output_folder, exist_ok=True)

def puzzle1():
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        x, y, dx, dy = robot
        for _ in range(100):
            # x is position of column
            # y is position of row
            x += dx
            if x < 0:
                x += width
            elif x >= width:
                x -= width

            y += dy
            if y < 0:
                y += height
            elif y >= height:
                y -= height

        print(x, y)
        if x < width // 2:
            if y < height // 2:
                print(f"Quadrant 1 - {x}, {y}")
                q1 += 1
            elif y > height // 2:
                print(f"Quadrant 3 - {x}, {y}")
                q3 += 1
        elif x > width // 2:
            if y < height // 2:
                print(f"Quadrant 2 - {x}, {y}")
                q2 += 1
            elif y > height // 2:
                print(f"Quadrant 4 - {x}, {y}")
                q4 += 1
    print(q1, q2, q3, q4)
    print(q1 * q2 * q3 * q4)


def puzzle2():
    scaled_width = width * scale
    scaled_height = height * scale
    for i in range(10000):
        grid = np.zeros((scaled_width, scaled_height, 3), dtype=np.uint8)

        for idx, robot in enumerate(robots):
            x, y, dx, dy = robot
            # x is position of column
            # y is position of row
            x += dx
            if x < 0:
                x += width
            elif x >= width:
                x -= width

            y += dy
            if y < 0:
                y += height
            elif y >= height:
                y -= height

            robots[idx] = [x, y, dx, dy]
            scaled_x = x * scale
            scaled_y = y * scale
            cv2.circle(grid, (scaled_x, scaled_y), 5, (0, 255, 0), -1)

        filename = os.path.join(output_folder, f"{i + 1}.png")
        cv2.imwrite(filename, grid)

        cv2.imshow("Robot Visualization", grid)
        key = cv2.waitKey(1)  # Wait for 1 ms between frames
        if key == 27:  # Exit when ESC is pressed
            break

    cv2.destroyAllWindows()

puzzle2()
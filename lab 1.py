red = '\x1b[48;5;196m'
white = '\x1b[48;5;15m'
blue = '\x1b[48;5;21m'
stop = '\033[0m'

def draw_pix(row, size):

    if row < size // 3:
        color = red
    elif row < 2 * size // 3:
        color = white
    else:
        color = blue


    for col in range(size * 2):
        print(color + '  ', end='')
    print(stop)

def netherlands_flag(size):
    for row in range(size):
        draw_pix(row, size)


netherlands_flag(15)


# 2. График функции y = 2x

def graph_y_equals_x_mult_2():
    width = 20
    height = 10
    for y in range(height, -1, -1):
        for x in range(width + 1):
            if x == 0 and y == 0:
                print('+', end=' ')
            elif x == 0:
                print('|', end=' ')
            elif y == 0:
                print('-', end=' ')
            elif y == x // 1:
                print(' *', end=' ')
            else:
                print('   ', end=' ')

        print()


graph_y_equals_x_mult_2()

# 3 задание чарт

white = '\x1b[48;5;15m'
stop = '\033[0m'
file = open("sequence.txt")
file_ms = [float(i) for i in file]
cor_dig = [i for i in file_ms if ((i <= 5) and (i >= -5))]
print(cor_dig)
print(len(cor_dig))
less_0 = len([i for i in cor_dig if (i > 0)])
more_0 = len(cor_dig) - less_0


def draw_line(count):
    print(white * (count < less_0), '  ', stop, ' ', white * (count < more_0), '  ', stop, )


def chart():
    for i in range(max(less_0, more_0), 0, -1):
        draw_line(i)


chart()
print(' <0     >0')

white = '\x1b[48;5;15m'
stop = '\033[0m'


# 4 задание фигурa

def process_numbers():
    with open('sequence.txt') as file:
        numbers = [float(line.strip()) for line in file]

    group_1 = [n for n in numbers if 5 <= n <= 10]
    group_2 = [n for n in numbers if -10 <= n <= -5]

    total = len(group_1) + len(group_2)

    percent_group_1 = len(group_1) / total * 100 if total > 0 else 0
    percent_group_2 = len(group_2) / total * 100 if total > 0 else 0

    print(f"Числа от 5 до 10: {percent_group_1:.2f}%")
    print(f"Числа от -5 до -10: {percent_group_2:.2f}%")

    max_height = 10
    group_1_height = int(max_height * percent_group_1 / 100)
    group_2_height = int(max_height * percent_group_2 / 100)


process_numbers()

import time
import os

SET_COLOR = '\x1b[48;5;15m'
END = "\x1b[0m"
CLEAR = "\033[H"


def pattern(position=0, radius=6):
    for y in range(2 * radius + 1):
        for x in range(4 * radius + 2):
            if (x - radius) * 2 + (y - (radius + position))**2 <= radius ** 2:
                print(f"{SET_COLOR}{' '}{END}", end='')
            elif (x - (3 * radius + 1)) * 2 + (y - (radius + position))**2 <= radius ** 2:
                print(f"{SET_COLOR}{' '}{END}", end='')
            else:
                print(" ", end='')

        print()


def main():
    position = 0
    frames = 0

    while True:
        pattern(position)

        frames += 1
        if frames >= 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            frames = 0

        position += 2
        if position > 10:
            position = 0

        time.sleep(0.5)


if __name__ == "__main__":
    main()
import random

file_path = 'D:\\last_655_draw.txt'

try:
    with open(file_path, 'r') as file:
        last_draw = file.read()
except FileNotFoundError:
    print("The file does not exist. Creating a new file...")
    last_draw = ''
    with open(file_path, 'w') as file:
        file.write(last_draw)

draw = []

if not last_draw:
    for _ in range(6):
        num = random.randint(1, 45)
        while num in draw:
            num = random.randint(1, 45)
        draw.append(num)
    draw.sort()
    with open(file_path, 'w') as file:
        file.write(",".join(map(str, draw)))
    print("Last 655 Lottery Draw: ", draw)
else:
    print("Last 655 Lottery Draw: ", last_draw.split(','))

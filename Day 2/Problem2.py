with open("input.txt", 'r') as file:
    readings, horizontal, depth, aim = [x.strip() for x in file.readlines()], 0, 0, 0
    for x in readings:
        aim += (1 if x[0] == 'd' else -1 if x[0] == 'u' else 0) * int(x.split()[-1])
        if x[0] == 'f':
            horizontal += int(x.split()[-1])
            depth += aim * int(x.split()[-1])
    print(horizontal * depth)

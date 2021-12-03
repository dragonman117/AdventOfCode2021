with open("input.txt", 'r') as file:
    readings = [list(x.strip()) for x in file.readlines()]
    gama = [1 if (sum([int(y[x]) for y in readings]) > (len(readings) / 2)) else 0 for x in range(0, len(readings[0]))]
    print(int("".join([str(x) for x in gama]), 2) * int("".join(["1" if x == 0 else "0" for x in gama]), 2))

with open("input.txt", 'r') as file:
    readings = [x.strip() for x in file.readlines()]
    print(sum([int(x.split()[-1]) for x in readings if x[0] == 'f']) * sum([(1 if x[0] == 'd' else -1) * int(x.split()[-1]) for x in readings if x[0] == 'd' or x[0] == 'u']))

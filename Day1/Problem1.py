with open("input.txt", 'r') as file:
    readings = [int(x.strip()) for x in file.readlines()]
    print(sum([1 if readings[x] > readings[x-1] else 0 for x in range(1, len(readings))]))

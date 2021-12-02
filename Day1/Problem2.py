with open("input.txt", 'r') as file:
    readings = [int(x.strip()) for x in file.readlines()]
    setOfThree = [sum([readings[x-2] if x - 2 >= 0 else 0, readings[ x - 1], readings[x]]) for x in range(2, len(readings))]
    print(sum([1 if setOfThree[x] > setOfThree[x - 1] else 0 for x in range(1, len(setOfThree))]))

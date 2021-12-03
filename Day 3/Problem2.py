def filterList(lst, cmpStr, index, filterLambda):
    tmp = [x for x in lst if int(cmpStr) == int(x[index])]
    if len(tmp) <= 1: return tmp[0]
    return filterList(tmp, filterLambda(tmp, index + 1), index + 1, filterLambda)


with open("input.txt", 'r') as file:
    readings = [list(x.strip()) for x in file.readlines()]
    oxegenStr = lambda lst, i: int(sum([int(x[i]) for x in lst]) * 2 >= len(lst))
    co2Str = lambda lst, i: int(sum([int(x[i]) for x in lst]) * 2 < len(lst))
    print(int("".join(filterList(readings, oxegenStr(readings, 0), 0, oxegenStr)), 2) * int(
        "".join(filterList(readings, co2Str(readings, 0), 0, co2Str)), 2))

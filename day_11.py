def monkey_1(id:int, items:list[list[int]]) -> (list[list[int]], int):
    count = 0
    if id == 0:
        for entry in items[0]:
            count += 1
            new = (entry * 5) // 3
            if new % 3 == 0:
                items[7].append(new)
            else:
                items[4].append(new)
        items[0] = []
    elif id == 1:
        for entry in items[1]:
            count += 1
            new = (entry + 6) // 3
            if new % 17 == 0:
                items[3].append(new)
            else:
                items[0].append(new)
        items[1] = []
    elif id == 2:
        for entry in items[2]:
            count += 1
            new = (entry + 5) // 3
            if new % 2 == 0:
                items[3].append(new)
            else:
                items[1].append(new)
        items[2] = []
    elif id == 3:
        for entry in items[3]:
            count += 1
            new = (entry + 2) // 3
            if new % 19 == 0:
                items[7].append(new)
            else:
                items[0].append(new)
        items[3] = []
    elif id == 4:
        for entry in items[4]:
            count += 1
            new = (entry * 7) // 3
            if new % 11 == 0:
                items[5].append(new)
            else:
                items[6].append(new)
        items[4] = []
    elif id == 5:
        for entry in items[5]:
            count += 1
            new = (entry + 7) // 3
            if new % 5 == 0:
                items[2].append(new)
            else:
                items[1].append(new)
        items[5] = []
    elif id == 6:
        for entry in items[6]:
            count += 1
            new = (entry + 1) // 3
            if new % 13 == 0:
                items[5].append(new)
            else:
                items[2].append(new)
        items[6] = []
    else:
        for entry in items[7]:
            count += 1
            new = (entry * entry) // 3
            if new % 7 == 0:
                items[4].append(new)
            else:
                items[6].append(new)
        items[7] = []

    return (items, count)

def monkey_2(id:int, items:list[list[int]]) -> (list[list[int]], int):
    count = 0
    if id == 0:
        for entry in items[0]:
            count += 1
            new = (entry * 5)
            if new % 3 == 0:
                items[7].append(new)
            else:
                items[4].append(new)
        items[0] = []
    elif id == 1:
        for entry in items[1]:
            count += 1
            new = (entry + 6)
            if new % 17 == 0:
                items[3].append(new)
            else:
                items[0].append(new)
        items[1] = []
    elif id == 2:
        for entry in items[2]:
            count += 1
            new = (entry + 5)
            if new % 2 == 0:
                items[3].append(new)
            else:
                items[1].append(new)
        items[2] = []
    elif id == 3:
        for entry in items[3]:
            count += 1
            new = (entry + 2)
            if new % 19 == 0:
                items[7].append(new)
            else:
                items[0].append(new)
        items[3] = []
    elif id == 4:
        for entry in items[4]:
            count += 1
            new = (entry * 7)
            if new % 11 == 0:
                items[5].append(new)
            else:
                items[6].append(new)
        items[4] = []
    elif id == 5:
        for entry in items[5]:
            count += 1
            new = (entry + 7)
            if new % 5 == 0:
                items[2].append(new)
            else:
                items[1].append(new)
        items[5] = []
    elif id == 6:
        for entry in items[6]:
            count += 1
            new = (entry + 1)
            if new % 13 == 0:
                items[5].append(new)
            else:
                items[2].append(new)
        items[6] = []
    else:
        for entry in items[7]:
            count += 1
            new = (entry * entry)
            if new % 7 == 0:
                items[4].append(new)
            else:
                items[6].append(new)
        items[7] = []

    return (items, count)

def part1() -> int:
    items = [[66, 71, 94],
             [70],
             [62, 68, 56, 65, 94, 78],
             [89, 94, 94, 67],
             [71, 61, 73, 65, 98, 98, 63],
             [55, 62, 68, 61, 60],
             [93, 91, 69, 64, 72, 89, 50, 71],
             [76, 50]]
    
    counts = [0 for i in range(8)]
    
    for i in range(20):
        for j in range(8):
            items, iter_count = monkey_1(j, items)
            counts[j] += iter_count
    
    counts.sort()
    return counts[-1] * counts[-2]

def part2():
    items = [[66, 71, 94],
             [70],
             [62, 68, 56, 65, 94, 78],
             [89, 94, 94, 67],
             [71, 61, 73, 65, 98, 98, 63],
             [55, 62, 68, 61, 60],
             [93, 91, 69, 64, 72, 89, 50, 71],
             [76, 50]]
    
    counts = [0 for i in range(8)]
    
    for i in range(10000):
        print(f"Round {i}:")
        for j in range(8):
            print(f"\tMonkey {j}:\t", end="")
            items, iter_count = monkey_2(j, items)
            counts[j] += iter_count
            print("Complete")
        print()
    
    counts.sort()
    return counts[-1] * counts[-2]

print(part2())
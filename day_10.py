total = 1
cycle = 0
output = ""

for line in open("day_10_input.txt"):
    print(line[:-1])
    if line == "noop\n" or line == "noop":
        output = output + "."
        print("noop caught")
    else:
        output = output + ".#"
        print("not noop")
    print()

for i in len(output) // 40:
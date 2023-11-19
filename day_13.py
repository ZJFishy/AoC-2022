def parse_list(string_in):
    temp_list = []
    if type(string_in) == str:
        list_in = list(string_in)
    else:
        list_in = string_in
    current_token = 0
    token_in_use = False
    brack_index_and_count = [0, 0]

    for i in range(len(list_in)):
        entry = list_in[i]
        try:
            this_entry = int(entry)
            if brack_index_and_count == [0, 0]:
                current_token += (this_entry / 10)
                current_token *= 10
                token_in_use = True
        
        except:
            if entry == ",":
                if current_token != 0:
                    temp_list.append(int(current_token))
                    current_token = 0
                    token_in_use = False
            elif entry == "[":
                if brack_index_and_count == [0, 0]:
                    brack_index_and_count = [i, 1]
                else:
                    brack_index_and_count[1] += 1
            elif entry == "]":
                brack_index_and_count[1] -= 1
                if brack_index_and_count[1] == 0:
                    temp_list.append(parse_list(list_in[brack_index_and_count[0]+1:i]))
                    brack_index_and_count = [0, 0]
    if token_in_use:
        temp_list.append(int(current_token))

    return temp_list

def compare_list(left_in, right_in):
    pointer = 0
    while (pointer < len(left_in)) & (pointer < len(right_in)):
        if type(left_in[pointer]) == type(right_in[pointer]) == int:
            if left_in[pointer] == right_in[pointer]:
                pointer +=1
            elif left_in[pointer] < right_in[pointer]:
                return "right order"
            else:
                return "wrong order"
        elif type(left_in[pointer]) == int:
            result = compare_list([left_in[pointer]], right_in[pointer])
            if result == "equal":
                pointer += 1
            else:
                return result
        elif type(right_in[pointer]) == int:
            result = compare_list(left_in[pointer], [right_in[pointer]])
            if result == "equal":
                pointer += 1
            else:
                return result
        else:
            result = compare_list(left_in[pointer], right_in[pointer])
            if result == "equal":
                pointer += 1
            else:
                return result
    if pointer == len(left_in) == len(right_in):
        return "equal"
    elif len(right_in) > len(left_in):
        return "right order"
    else:
        return "wrong order"

packets = []
index_sum = 0

for line in open("./day_13_input.txt"):
    if len(line.split()) > 0:
        packets.append(line.split()[0][1:-1])

for i in range(0, len(packets), 2):
    left = parse_list(packets[i])
    right = parse_list(packets[i+1])
    result = compare_list(left, right)
    print(left, right, result, "\n", sep="\n")
    if result in ["equal", "right order"]:
        index_sum += (i / 2) + 1

print(int(index_sum))
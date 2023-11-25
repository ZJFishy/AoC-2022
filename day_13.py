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
                if token_in_use:
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

def compare_lists(left_in, right_in):
    pointer = 0
    left_length = len(left_in)
    right_length = len(right_in)
    while ((pointer < left_length) & (pointer < right_length)):
        if type(left_in[pointer]) == type(right_in[pointer]) == int:
            if left_in[pointer] == right_in[pointer]:
                pointer +=1
            elif left_in[pointer] < right_in[pointer]:
                return "right order"
            else:
                return "wrong order"
        elif type(left_in[pointer]) == int:
            result = compare_lists([left_in[pointer]], right_in[pointer])
            if result == "equal":
                pointer += 1
            else:
                return result
        elif type(right_in[pointer]) == int:
            result = compare_lists(left_in[pointer], [right_in[pointer]])
            if result == "equal":
                pointer += 1
            else:
                return result
        else:
            result = compare_lists(left_in[pointer], right_in[pointer])
            if result == "equal":
                pointer += 1
            else:
                return result
    if pointer == left_length == right_length:
        return "equal"
    elif right_length > left_length:
        return "right order"
    else:
        return "wrong order"

def sort_lists(packets_in):
    if len(packets_in) == 1:
        return packets_in
    
    pivot = len(packets_in) // 2
    left = sort_lists(packets_in[:pivot])
    right = sort_lists(packets_in[pivot:])

    sorted_lists = []
    left_pointer = 0
    right_pointer = 0
    
    while ((left_pointer < len(left)) & (right_pointer < len(right))):
        result = compare_lists(left[left_pointer], right[right_pointer])

        if result == "right order":
            sorted_lists.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_lists.append(right[right_pointer])
            right_pointer += 1
    
    if left_pointer == len(left):
        for entry in right[right_pointer:]:
            sorted_lists.append(entry)
    
    else:
        for entry in left[left_pointer:]:
            sorted_lists.append(entry)
    
    return sorted_lists

def part_1():
    packets = []

    for line in open("./day_13_test_input.txt"):
        if len(line.split()) > 0:
            packets.append(line.split()[0][1:-1])
    index_sum = 0

    for i in range(0, len(packets), 2):
        left = parse_list(packets[i])
        right = parse_list(packets[i+1])
        result = compare_lists(left, right)
        print(left, right, result, "\n", sep="\n")
        if result in ["equal", "right order"]:
            index_sum += (i / 2) + 1

    print(int(index_sum))

def part_2():
    packets = []

    for line in open("./day_13_input_2.txt"):
        if len(line.split()) > 0:
            packets.append(parse_list(line.split()[0][1:-1]))

    sorted_packets = sort_lists(packets)
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)

print(part_2())
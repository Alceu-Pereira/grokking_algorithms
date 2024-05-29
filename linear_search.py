def linear_search(list, target):
    actual_index = 0
    while actual_index < len(list):
        if target == list[actual_index]:
            return actual_index
        else:
            actual_index += 1
    return None

my_list = [1, 2, 3, 6, 8]
print(linear_search(my_list, 9))
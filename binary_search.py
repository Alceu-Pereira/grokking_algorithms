def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        center_index = (high + low) // 2
        center_item = list[center_index]

        if center_item == target:
            return center_index
        
        if center_item > target:
            high = center_index - 1

        else:
            low = center_index + 1

    return None

my_test_list = [1, 2, 4, 9, 10]
print(binary_search(my_test_list, 4))
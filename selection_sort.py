def smallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def selection_sort(list):
    sorted_list = []
    for i in range(len(list)):
        smallest_ = smallest(list)
        sorted_list.append(list.pop(smallest_))
    return sorted_list

my_list = [1, 5, 8, -1, 1, 3, 0, 0]
print(selection_sort(my_list))

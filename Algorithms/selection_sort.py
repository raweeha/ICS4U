##def selection_sort_in_place(a_list):
##
##    indexing_length = len(a_list) - 1
##
##    for i in range(0, indexing_length):
##
##        min_value = i
##
##        for j in range(i+1, len(a_list)):
##            
##            if a_list[j] < a_list[min_value]:
##
##                min_value = j
##
##
##        if min_value != i:
##            a_list[i], a_list[min_value] = a_list[min_value], a_list[i]
##
##
##    return a_list
##
##a_list = [6, 0, 1, 4, 2, 3, 6, 9, 15, 23]
##print(selection_sort(a_list))


def selection_sort_out_of_place(a_list):
    unsorted_list = a_list[:]
    a_list.clear()

    for i in range(0, len(unsorted_list)):
        minimum = unsorted_list[i]

        for next_element in range(i + 1, len(unsorted_list)):
            compared_element = unsorted_list[next_element]

            if compared_element < minimum:
                minimum = compared_element

        unsorted_list.remove(minimum)
        unsorted_list.insert(i, minimum)
        a_list.append(minimum)

numbers = [8, 8, 18, 13, 36, 0, 2, -2, -5]
selection_sort_out_of_place(numbers)
print(numbers)



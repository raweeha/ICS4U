def Bubble_Sort(a_list):

    indexing_length = len(a_list) - 1

    swapped = False

    while not swapped:
        swapped = True

        for i in range(0, indexing_length):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

                swapped = False


    return a_list

a_list = [3, 0, 4, 3, 2, 7, 5, 9, 13]
print(Bubble_Sort(a_list))



##def Bubble_Sort(a_list):
##
##    indexing_length = len(a_list) - 1
##
##    swapped = True
##
##    while swapped:
##        swapped = False
##
##        for i in range(0, indexing_length):
##            if a_list[i] > a_list[i+1]:
##                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
##
##                swapped = True
##
##        indexing_length -= 1
##
##    return a_list
##
##a_list = [3, 0, 4, 3, 2, 7, 5, 9, 13]
##print(Bubble_Sort(a_list))

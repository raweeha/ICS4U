##Question 4
##Given the following algorithm, generate a Python implementation. 
##The algorithm deletes a given item from list.
##
##
##given a list and item in list
##
##repeat until list[index] = item:
##
##   index + 1
##
##list <- list[0:index-1] + list[index+1:n]


def delete_item(a_list, item):
    for index in range(0, len(a_list)):
        while a_list[index] != item:
            index += 1
        a_list = a_list[0:index] + a_list[index+1:]
        return a_list

a_list = [8, 4, 3, 6, 12, 9, 10]
item = 3

print(delete_item(a_list, item))

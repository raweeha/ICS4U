

def Insertion_Sort(a_list):

    for i in range(1, len(a_list)):

        value = a_list[i]

        while a_list[i-1] > value and i > 0:
            a_list[i-1], a_list[i] = a_list[i], a_list[i-1]

            i = i - 1

    return a_list

a_list = [7, 4, 3, 10, 54, 32, 9, 14]
print(Insertion_Sort(a_list))

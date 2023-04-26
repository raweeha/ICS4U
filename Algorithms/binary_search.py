
def binary_search(a_list, t):
    L = 0
    R = len(a_list) - 1
    m = (L + R) // 2

    while a_list[m] != t:
        if L > R:
            return -1
        else:
            m = (L + R) // 2
            if a_list[m] < t:
                L = m + 1
            elif a_list[m] > t:
                R = m - 1
            else:
                return m
        
a_list = [1, 1, 2, 4, 6, 8, 9, 14, 17, 19, 45, 38]
t = 17
print(binary_search(a_list, t))
    

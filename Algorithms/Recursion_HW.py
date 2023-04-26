# Recursion Programming Exercises HW

# 1.How many calls are made to fibonacci? 5 - 1: the first one for 4. 2: (n-1) which is 3. 3:
#                                                Within 3, two calls are made. for (2) and 4: (1). 5: og (n-2) = 2.

##def fibonacci(n):
##    if n == 1:
##        return 1
##    elif n == 2:
##        return 1
##    else:
##
##        return fibonacci(n-1) + fibonacci(n-2)	    	
##
##print (fibonacci(4))
##
##output: 3

# 2. There are THREE errors in the code at this link.

##'''
##This method should print the sum of squares from 1 to n
##For example sumOfSquares(4) = 30
##1^2 + 2^2 + 3^2 + 4^2 = 30
##'''

#CODE:

##def sumOfSquares(n):
##    if n == 1:
##            return 0
##	    
##    else:
##        return (n+n) + sumOfSquares(n + 1)
##	
##	
##print (sumOfSquares(4))

#CORRECTION:

##def sumOfSquares(n):
##    if n == 1:
##        return 1
##	    
##    else:
##        return (n+n) + sumOfSquares(n - 1)
##	
##	
##print (sumOfSquares(4))

##** find how to fix last error. Currently output is 19. https://pythontutor.com/visualize.html#mode=display

## 3. Create a recursive function that returns the sum of the numbers in a list.

##'e.g. sumOfNumbers(4) = 1+2+3+4 = 10'
##
##def sumOfNumbers(n):
##    if n == 1:
##        return 1
##
##    else:
##        return n + sumOfNumbers(n-1)
##
##print(sumOfNumbers(4))

## 4. Create a recursive function that returns a string version of an integer n with commas added.
##For example, add_commas('15866321') should return '15,866,321'

##def add_commas(n):
##    if len(n) <= 3:
##        return n
##    else:
##        return add_commas(n[:-3]) + ',' + n[-3:]
##
##print(add_commas('98735893'))

##5. Create a recursive function that returns the result of of reversing a string.
##For example reverse('hello world') should return 'dlrow olleh'

##def reverse(s):
##    if len(s) == 0:
##        return s
##    else:
##        return reverse(s[1:]) + s[0]
##    
##print (reverse("hello world"))

##6. Create a recursive function that returns the index of an item in a list.
##def index_list(some_list, item):
##
##    if len(some_list) == 0:
##        return -1
##    elif some_list[-1] == item:
##        return len(some_list)-1
##    else:
##        return index_list(some_list[0:-1], item)
##
##some_list = [6, 4, 2, 8, -4, -9]
##item = 4
##print(index_list(some_list, item))







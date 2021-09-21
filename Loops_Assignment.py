'''
Iterate through every number in a list named my_list to separate out even and odd numbers. Identify possible
outlier values as well. Outliers means, values greater than 90 in this list.
(my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4])
Expected Output:
Even numbers [2, 4, 6, 32, 2, 4]
Odd numbers [1, 3, 5, 7, 21, 33]
outliers [100, 110]
(Hint: Loop and If Else If will be use to solve this problem) And google that how to add value in list in python
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
even_numbers = []
odd_numbers = []
outliers = []
for number in my_list:
    if number > 90:
        outliers.append(number)
    elif number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f'Even numbers {even_numbers}')
print(f'Odd numbers {odd_numbers}')
print(f'Outliers {outliers}')




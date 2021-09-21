'''
Challenge 2: Calculate the cumulative sum of all elements in a list named my_list.
(my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4])
Expected Output:
The cummulative sum of the list [1, 3, 6, 10, 15, 21, 28, 128, 238, 259, 292, 324, 326, 330]'''

my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
cummulative_list = []
cummunumber = 0
for number in range(0, len(my_list)):
    cummunumber += my_list[number]
    cummulative_list.append(cummunumber)
print(f'The cummulative sum of the list {cummulative_list}')

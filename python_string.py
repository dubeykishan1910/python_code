word = "kishan"

print(word.upper())


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
single_list = [j for i in list_of_lists for j in i]

print(single_list)



from itertools import chain

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
single_list = list(chain.from_iterable(list_of_lists))

print(single_list)

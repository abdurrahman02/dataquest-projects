search_list = ['apple', 'orange', 'pear', 'fig', 'passionfruit']


def search(strings, term, index=0):
    # Implement your recursive solution here.
    if index == len(strings):
        return -1
    elif strings[index] == term:
        return index
    else:
        return search(strings, term, index + 1)


apple_index = search(search_list, "apple", 0)
pear_index = search(search_list, "pear", 0)
foo_index = search(search_list, "foo", 0)


def traverse_list(values):
    return traverse_list(values)


# traverse_list([1, 2])

# Load your file and cast it to integers here.

def summation(values):
    # Implement your recursive solution here.
    return None


fi = open("random_integers.txt")
li = [int(data[:-1]) for data in fi.readlines()]

divide_and_conquer_sum = summation()

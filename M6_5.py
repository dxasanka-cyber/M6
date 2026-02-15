def remove_uneven(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)

    return new_list

numbers = [5, 12, 25, 32, 43, 59]

print("Original list:", numbers)

cut_list = remove_uneven(numbers)

print("List without uneven numbers:", cut_list)

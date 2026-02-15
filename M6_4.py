def sum_list(l):
    result = 0
    for n in l:
        result += n
    return result


# Main program
numbers = [5, 12, 25, 32, 43, 59]

print("List:", numbers)

total = sum_list(numbers)

print("The sum of list number is:", total)

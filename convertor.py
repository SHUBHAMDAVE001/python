def find_max(value):
    numbers = value.split()
    # print(numbers)
    maximum = int(numbers[0])
    for value in numbers:
        # print(value, maximum)
        value = int(value)
        if value > maximum:
            maximum = value

    max_number = maximum
    return f"{max_number} is largest value"

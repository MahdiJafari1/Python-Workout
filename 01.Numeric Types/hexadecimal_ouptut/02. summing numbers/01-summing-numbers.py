def my_sum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(f"Sum of givin numbers: {my_sum(1, 2, 3, 4, 5, 6)}")

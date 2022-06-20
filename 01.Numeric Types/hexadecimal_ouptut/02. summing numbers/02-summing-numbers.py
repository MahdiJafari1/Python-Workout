def my_sum(*numbers, start=0):
    sum = start
    for number in numbers:
        sum += number
    return sum

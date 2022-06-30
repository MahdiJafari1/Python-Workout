def sum_ints(filename):
    total = 0

    for one_line in open(filename):
        for one_word in one_line.split():
            if one_word.isdigit():
                total += int(one_word)

    return total


def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time and number of runs."""

    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input("Enter 10 km run time: ")

        if not one_run:
            break

        number_of_runs += 1
        total_time += float(one_run)

        avg_time = total_time / number_of_runs

        print(f"Average of {avg_time}, over {number_of_runs} runs")

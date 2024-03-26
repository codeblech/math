def sum_previous_current(number):
    previous_number = 0
    for i in range(number):
        sum = previous_number + i
        print(sum)
        previous_number = i


sum_previous_current(10)



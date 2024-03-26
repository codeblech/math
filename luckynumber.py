lucky_numbers = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37]
while True:
    user_input = int(input("Number: "))
    if user_input in lucky_numbers:
        print("Good Luck!")
    else:
        print("Bad Luck!")


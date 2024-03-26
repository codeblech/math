number = float(input("Number: "))
nearest_to = input('Precision: ').lower()
if nearest_to == "1":
    print(round(number, 1))
elif nearest_to == "2":
    print(round(number, 2))
elif nearest_to == "3":
    print(round(number, 3))
elif nearest_to == "4":
    print(round(number, 4))
else:
    print("Enter value from 1 to 4!")
print("This is a program to find the sum of FIRST 'n' term!")

known = input(
    "What is known?  a1 / a2 / common difference(d) / last term(l) / Number of"
    " terms(n): "
).lower()
if known == "a1 a2 n":
    a1 = int(input("First Term of AP: "))
    a2 = int(input("Second Term of AP: "))
    n = int(input("'nth' term of AP: "))
    common_difference = d = a2 - a1
    sum_n = (n / 2) * (2 * a1 + ((n - 1) * d))
    print(f"Sum of FIRST 'n' terms is {sum_n}")
elif known == "a1 a2 l":
    a1 = int(input("First Term of AP: "))
    a2 = int(input("Second Term of AP: "))
    l = int(input("Last term of AP: "))
    common_difference = d = a2 - a1
    n = ((l - a1) / d) + 1
    sum_n = (n / 2) * (a1 + l)
    print(f"Sum of FIRST 'n' terms is {sum_n}")
elif known == "a1 d l":
    a1 = int(input("First Term of AP: "))
    common_difference = d = int(input("Common Difference"))
    l = int(input("Last term of AP: "))
    n = ((l - a1) / d) + 1
    sum_n = (n / 2) * (a1 + l)
    print(f"Sum of FIRST 'n' terms is {sum_n}")
elif known == "a1 d n":
    a1 = int(input("First Term of AP: "))
    common_difference = d = int(input("Common Difference"))
    n = int(input("'nth' term of AP: "))
    sum_n = (n / 2) * (2 * a1 + ((n - 1) * d))
    print(f"Sum of FIRST 'n' terms is {sum_n}")
elif known == "a1 l n":
    a1 = int(input("First Term of AP: "))
    l = int(input("Last term of AP: "))
    n = int(input("'n': "))
    sum_n = (n / 2) * (a1 + l)
    print(f"Sum of FIRST 'n' terms is {sum_n}")
elif known == "a2 d n":
    a2 = int(input("Second Term of AP: "))
    common_difference = d = int(input("Common Difference"))
    n = int(input("'nth' term of AP: "))
    a1 = a2 - d
    sum_n = (n / 2) * (2 * a1 + ((n - 1) * d))
    print(f"Sum of FIRST 'n' terms is {sum_n}")
elif known == "a2 d l":
    a2 = int(input("Second Term of AP: "))
    common_difference = d = int(input("Common Difference"))
    l = int(input("Last term of AP: "))
    a1 = a2 - d
    n = ((l - a1) / d) + 1
    sum_n = (n / 2) * (a1 + l)
    print(f"Sum of FIRST 'n' terms is {sum_n}")
elif known == "a2 l n":
    a2 = int(input("Second Term of AP: "))
    l = int(input("Last term of AP: "))
    n = int(input("'nth' term of AP: "))
    common_difference = d = (a2 - l) / (2 - n)
    a1 = a2 - d
    sum_n = (n / 2) * (a1 + l)
    print(f"Sum of FIRST 'n' terms is {sum_n}")
else:
    print("Enter Valid Value!   OR    Lack Of Information!")

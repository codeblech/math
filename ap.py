def arithmetic_progression_nth_term(a_1, a_2, n):
    d: int
    common_difference = d = a_2 - a_1
    n: int
    nth_term = a_1 + (n - 1) * d
    return f"nth term is '{nth_term}'"


print(arithmetic_progression_nth_term(a_1=1, a_2=3, n=3))



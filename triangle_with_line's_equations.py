def linear_equations_two_variables(a1, b1, constant1, a2, b2, constant2):
    # Making x-Coefficients Equal:
    # c- coefficient, m- multiplied
    _y1_m, constant1_m = b1 * a2, constant1 * a2
    _y2_m, constant2_m = b2 * a1, constant2 * a1
    y_c = _y1_m - _y2_m
    constant = constant1_m - constant2_m
    y = -constant / y_c
    x = (-constant1 - (b1 * y)) / a1
    return x, y


def triangle_equation_of_lines(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    point_a = linear_equations_two_variables(a1, b1, c1, a3, b3, c3)
    point_b = linear_equations_two_variables(a2, b2, c2, a1, b1, c1)
    point_c = linear_equations_two_variables(a3, b3, c3, a2, b2, c2)
    return f'''A: {point_a}
B: {point_b}
C: {point_c}'''


print(triangle_equation_of_lines(1, 1, 1, 1, 1, 1, 1, 1, 1))

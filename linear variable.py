# Give coefficients for equations of the form: ax + by + cz - constant = 0

def eliminate_z(a1, b1, c1, constant1, a2, b2, c2, constant2):      # This is a function helping 'linearthree' to eliminate one variable
    # m- multiplied
    a1_m, b1_m, c1_m, constant1_m = a1 * c2, b1 * c2, c1 * c2, constant1 * c2
    a2_m, b2_m, c2_m, constant2_m = a2 * c1, b2 * c1, c2 * c1, constant2 * c1

    # c- coefficient
    x_c = a1_m - a2_m
    y_c = b1_m - b2_m
    constant_c = constant1_m - constant2_m
    return x_c, y_c, constant_c


def linear_two(a1, b1, constant1, a2, b2, constant2):
    # Making x-Coefficients Equal:
    # c- coefficient, m- multiplied
    _y1_m, constant1_m = b1 * a2, constant1 * a2
    _y2_m, constant2_m = b2 * a1, constant2 * a1
    y_c = _y1_m - _y2_m
    constant = constant1_m - constant2_m
    y = -constant / y_c
    x = (-constant1 - (b1 * y)) / a1
    return x, y


def linear_three(a1, b1, c1, constant1, a2, b2, c2, constant2, a3, b3, _z3, constant3):
    # Eliminating z from 1st and 2nd Equation:
    x_1, y_1, constant_1 = eliminate_z(a1, b1, c1, constant1, a2, b2, c2, constant2)
    # Eliminating z from 1st and 3rd Equation:
    x_2, y_2, constant_2 = eliminate_z(a1, b1, c1, constant1, a3, b3, _z3, constant3)
    x, y = linear_two(x_1, y_1, constant_1, x_2, y_2, constant_2)
    z = -(constant1 + a1 * x + b1 * y) / c1
    return x, y, z


def quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    return x1, x2


x, y, z = linear_three(1, 1, 1, -1, 4, 2, 1, -5, 9, 3, 1, -12)
print(x, y, z, sep=',')
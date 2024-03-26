from math import sin, cos, asin, atan, degrees, radians


def cartpol(x_cartesian, y_cartesian):
    radius = (x_cartesian ** 2 + y_cartesian ** 2) ** 0.5
    angle = atan((y_cartesian / x_cartesian))
    return radius, angle


def poltcar(radius, angle):
    x_cartesian = radius * cos(radians(angle))
    y_cartesian = radius * sin(radians(angle))
    return x_cartesian, y_cartesian


def distfrm(x1, y1, x2, y2):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance


def measure_angle_using_coordinates(x1, y1, x2, y2, x3, y3):
    area = 1 / 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    angle = asin(2 * area / (distfrm(x1, y1, x2, y2) * distfrm(x1, y1, x3, y3)))
    return round(degrees(angle))


def pythagoras(perpendicular=0.0, base=0.0, hypotenuse=0.0):
    if hypotenuse == 0:
        hypotenuse = (perpendicular ** 2 + base ** 2) ** 0.5
    elif perpendicular == 0:
        perpendicular = (hypotenuse ** 2 - base ** 2) ** 0.5
    elif base == 0:
        base = (hypotenuse ** 2 - perpendicular ** 2) ** 0.5
    return perpendicular, base, hypotenuse
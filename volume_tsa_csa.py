from math import pi
print("This is a program to find Volume, length of Diagonal, TSA and CSA of 3D Shapes!")


def cube(side):
    volume = side ** 3
    tsa = 6 * side ** 2
    csa = 4 * side ** 2
    diagonal = side * (3 ** 0.5)
    return f'''Volume(v): {volume}
Total Surface Area(tsa): {tsa}
Curved Surface Area(csa): {csa}
Diagonal(d): {diagonal}'''


def cuboid(length, breadth, height):
    volume = length * breadth * height
    tsa = 2 * (length * breadth + breadth * height + length * height)
    csa = 2 * (length + breadth) * height
    diagonal = (length ** 2 + breadth ** 2 + height ** 2) ** 0.5
    return f'''Volume(v): {volume}
Total Surface Area(tsa): {tsa}
Curved Surface Area(csa): {csa}
Diagonal(d): {diagonal}'''


def cylinder(radius, height):
    volume = pi * radius ** 2 * height
    tsa = 2 * pi * radius * (height + radius)
    csa = 2 * pi * radius * height
    longest_rod = ((height ** 2) + (4 * radius ** 2)) ** 0.5
    return f'''Volume(v): {volume}
Total Surface Area(tsa): {tsa}
Curved Surface Area(csa): {csa}
Longest Rod: {longest_rod}'''


def cone(radius, height, slant_height):
    if radius == 0:
        radius = (slant_height ** 2 - height ** 2) ** 0.5
    elif height == 0:
        height = (slant_height ** 2 - radius ** 2) ** 0.5
    elif slant_height == 0:
        slant_height = (height ** 2 + radius ** 2) ** 0.5
    volume = 1 / 3 * (pi * (radius ** 2) * height)
    tsa = pi * radius * (slant_height + radius)
    csa = pi * radius * slant_height
    return f'''Volume:{volume}
Total Surface: {tsa}
Curved Surface Area: {csa}'''


def sphere(radius):
    volume = (4 * pi * radius ** 3) / 3
    tsa = 4 * pi * radius ** 2
    return f'''Volume(v): {volume}
Surface Area(tsa): {tsa}'''


def hemisphere(radius):
    volume = (2 * pi * radius ** 3) / 3
    tsa = 3 * pi * radius ** 2
    csa = 2 * pi * radius ** 2
    return f'''Volume(v): {volume}
Total Surface Area(tsa): {tsa}
Curved Surface Area(csa): {csa}'''


def frustum(radius_lower, radius_upper, height, slant_height):
    if height == 0:
        height = (slant_height ** 2 - (radius_lower - radius_upper) ** 2) ** 0.5
        print(f"Height: {height}")
    elif slant_height == 0:
        slant_height = (height ** 2 + (radius_upper - radius_lower) ** 2) ** 0.5
        print(f"Slant Height: {slant_height}")
    if slant_height == ((radius_upper - radius_lower) ** 2 + height ** 2) ** 0.5:
        volume = ((pi * height) / 3) * (radius_upper ** 2 + radius_lower ** 2 + radius_upper * radius_lower)
        csa = pi * (radius_upper + radius_lower) * slant_height
        tsa = csa + (pi * radius_upper ** 2) + (pi * radius_lower ** 2)
        return f'''Volume: {volume}
Total Surface Area: {tsa}
Curved Surface Area: {csa}'''
    else:
        return f'''Radius_lower, Radius_upper, slant_height and height do not relate to each other.
    Enter Valid Values!'''


def trigonometry_cone(height, radius):
    base_angle = round(math.atan(height / radius), 3)
    vertical_angle = 180 - 2 * base_angle
    return f'''Vertical Angle: {vertical_angle}
               Base Angles: {base_angle}'''


HEIGHT = 'Height: '
RADIUS = 'Radius: '
shape = input("Enter Shape Name: ").lower()
if shape == "cube":
    side = float(input("Side: "))
    print(cube(side))
elif shape == "cuboid":
    length = float(input("Length: "))
    breadth = float(input("Breadth: "))
    height = float(input(HEIGHT))
    print(cuboid(length, breadth, height))
elif shape == "cylinder":
    radius = float(input(RADIUS))
    height = float(input(HEIGHT))
    print(cylinder(radius, height))
elif shape == "cone":
    slant_height = float(input("Slant Height: "))
    height = float(input(HEIGHT))
    radius = float(input(RADIUS))
    print(cone(radius, height, slant_height))
elif shape == "sphere":
    radius = float(input(RADIUS))
    print(sphere(radius))
elif shape == "hemisphere":
    radius = float(input(RADIUS))
    print(hemisphere(radius))
elif shape == "frustum":
    radius_lower = float(input("Lower Radius: "))
    radius_upper = float(input("Upper Radius: "))
    slant_height = float(input("Slant Height: "))
    height = float(input(HEIGHT))
    print(frustum(radius_lower, radius_upper, height, slant_height))
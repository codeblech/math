# This is a program to find Everything!
# Shapes Available: Square, Rectangle, Parallelogram, Rhombus, Trapezium, Quadrilateral,
# Triangle, Circle, Kite''')

import math


def square(side):
    area = side ** 2
    perimeter = 4 * side
    diagonal = side * 2 ** 0.5
    return f'''Area(a): {area}
Perimeter(p): {perimeter}
Diagonal(d): {diagonal}'''


def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    diagonal = (length ** 2 + breadth ** 2) ** 0.5
    return f'''Area(a): {area}
Perimeter(p): {perimeter}
Diagonal(d): {diagonal}'''


def parallelogram(base, height):
    area = base * height
    return f"Area = {area}"


def rhombus_diagonal_method(diagonal1, diagonal2):
    half_d1 = diagonal1 / 2
    half_d2 = diagonal2 / 2
    side = ((half_d1 ** 2) + (half_d2 ** 2)) ** 0.5
    area = 0.5 * diagonal1 * diagonal2
    perimeter = 4 * side
    angle_a, angle_b, angle_c, angle_d = quadrilateral_angles(
        side, side, side, side, diagonal1)
    return f'''Area: {area}
Perimeter: {perimeter}
Side: {side}



Interior Angles: ∠A: {angle_a}°   ∠B: {angle_b}°   ∠C: {angle_c}°   ∠D: {angle_d}°'''


def rhombus_base_height_method(base, height):
    area = base * height
    perimeter = 4 * base
    return f'''Area: {area}
Perimeter: {perimeter}'''


def trapezium(b1, b2, h):
    area = 1 / 2 * ((b1 + b2) * h)
    return f"Area: {area}"


def triangle_base_height_method(base, height):
    area = 1 / 2 * base * height
    # If it is Isosceles Triangle, Using Pythagoras Theorem:
    isosceles_equal_sides = ((base / 2) ** 2 + (height ** 2)) ** 0.5
    angle_a = 2 * \
        triangle_interior_angles_3sides(
            height, isosceles_equal_sides, base / 2)[2]
    isosceles_equal_angles = triangle_interior_angles_3sides(
        height, isosceles_equal_sides, base / 2)[0]
    return f'''Area: {area}
If it is Isosceles Triangle:-  Equal Sides: {isosceles_equal_sides}
                               Interior Angles: {angle_a, isosceles_equal_angles, isosceles_equal_angles}'''


def triangle_herons_formula_method(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    heights = triangle_respective_heights(area, a, b, c)
    interior_angles = triangle_interior_angles_3sides(a, b, c)
    return f'''Area: {area}
Perimeter: {perimeter}
Respective Heights For Bases:  a: {heights[0]}   b: {heights[1]}   c: {heights[2]}
Interior Angles: ∠A: {interior_angles[0]}°   ∠B: {interior_angles[1]}°   ∠C: {interior_angles[2]}°'''


def triangle_side_angle_side_method(a, b, angle_c):
    area = (a * b * math.sin(angle_c)) / 2
    c, interior_angles = triangle_interior_angles_2sides_included_angle(
        a, b, angle_c)
    heights = triangle_respective_heights(area, a, b, c)
    perimeter = a + b + c
    return f'''Area: {area}
Perimeter: {perimeter}







Sides: c: {c}   a: {a}   b: {b}
Respective Heights For Bases: a: {heights[0]}   b: {heights[1]}   c: {heights[2]}
Interior Angles: ∠A: {interior_angles[0]}°   ∠B: {interior_angles[1]}°   ∠C: {math.degrees(angle_c)}°'''


def triangle_coordinates_method(x1, y1, x2, y2, x3, y3):
    global triangle_type
    area = 1 / 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    sides = triangle_length_of_sides_coordinates(x1, y1, x2, y2, x3, y3)
    perimeter = sum(sides)
    heights = triangle_respective_heights(
        area, a=sides[0], b=sides[1], c=sides[2])
    interior_angles = triangle_interior_angles_3sides(
        a=sides[0], b=sides[1], c=sides[2])
    equal_angles = []
    for angles in interior_angles:
        if angles not in equal_angles:
            equal_angles.append(angles)
    if len(equal_angles) == 3:
        triangle_type = "scalene"
    if len(equal_angles) == 2:
        triangle_type = "isosceles"
    if len(equal_angles) == 1:
        triangle_type = "equilateral"
    return f'''Triangle type: {triangle_type}
Area: {area} 
Sides: a: {sides[0]}   b: {sides[1]},   c: {sides[2]}
Perimeter: {perimeter}
Respective Heights For Bases: a: {heights[0]}   b: {heights[1]}   c: {heights[2]}
Interior Angles: ∠A: {interior_angles[0]}°   ∠B: {interior_angles[1]}°   ∠C: {interior_angles[2]}°'''


def triangle_equilateral(side):
    area = ((3 ** 0.5) * side ** 2) / 4
    perimeter = 3 * side
    height = 2 * area / side
    return f'''Area: {area}
Perimeter: {perimeter}
Heights: {height}
Interior Angles: 60°'''


def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return f'''Area(a): {area}
Circumference(c): {circumference}'''


def kite(d1, d2):
    area = 0.5 * d1 * d2
    return f"Area: {area}"


def quadrilateral_xy_method():
    global area
    a, b, c, d, d_ac, d_bd = quadrilateral_length_of_sides_coordinates(
        x1, y1, x2, y2, x3, y3, x4, y4)
    quad = quadrilateral_type(x1, y1, x2, y2, x3, y3, x4, y4)
    perimeter = a + b + c + d
    if quad != "No Quad Possible":
        angle_a, angle_b, angle_c, angle_d = quadrilateral_angles(
            a, b, c, d, d_ac)
        if quad == "quadrilateral":
            area = quadrilateral_simple_area(a, b, c, d, d_ac)
        if quad == "parallelogram":
            area = quadrilateral_simple_area(a, b, c, d, d_ac)
        if quad == "rhombus":
            area = rhombus_diagonal_method(d_ac, d_bd)[1]
        if quad == "rectangle":
            area = a * b
            angle_a, angle_b, angle_c, angle_d = 90, 90, 90, 90
        if quad == "square":
            area = a * a
            angle_a, angle_b, angle_c, angle_d = 90, 90, 90, 90
        if quad == "kite":
            area = (d_ac * d_bd) / 2
        return f'''Type Of Quadrilateral: {quad}
Area: {area}
Perimeter: {perimeter}
Sides: AB: {a}   BC: {b}   CD: {c}   AD: {d}   
Diagonals: AC: {d_ac}   BD: {d_bd}
Interior Angles: ∠A: {angle_a}°   ∠B: {angle_b}°   ∠C: {angle_c}°   ∠D: {angle_d}°'''
    else:
        return f"No Quad Possible"


def quadrilateral_diagonal_perpendicular_method(p1, p2, diagonal):
    area = (diagonal / 2) * (p1 + p2)
    return f"Area: {area}"


# _________________________________________________________________________________________________

def quadrilateral_type(x1, y1, x2, y2, x3, y3, x4, y4):
    a, b, c, d, d_ac, d_bd = quadrilateral_length_of_sides_coordinates(
        x1, y1, x2, y2, x3, y3, x4, y4)
    if a == c and b == d:
        quad = "parallelogram"
        if d_ac == d_bd:
            quad = "rectangle"
        if a == b == c == d:
            quad = "rhombus"
            if d_ac == d_bd:
                quad = "square"
    elif (a == b and c == d) or (b == c and d == a):
        quad = "kite"
    else:
        if triangle_herons_formula_method(a, b, d_ac) == 0 or triangle_herons_formula_method(b, c, d_bd) == 0 or \
                triangle_herons_formula_method(c, d, d_ac) == 0 or triangle_herons_formula_method(d, a, d_bd) == 0:
            quad = "No Quad Possible"
        else:
            quad = "quadrilateral"
    return quad


def quadrilateral_simple_area(a, b, c, d, d_ac):
    area = triangle_herons_formula_method(
        a, b, d_ac)[0] + triangle_herons_formula_method(c, d, d_ac)[0]
    return area


def quadrilateral_angles(a, b, c, d, d_ac):
    triangle_1_angle_a, triangle_1_angle_b, triangle_1_angle_d_ac = triangle_interior_angles_3sides(
        a, b, d_ac)
    triangle_2_angle_c, triangle_2_angle_d, triangle_2_angle_d_ac = triangle_interior_angles_3sides(
        c, d, d_ac)
    angle_a = triangle_1_angle_b + triangle_2_angle_c
    angle_b = triangle_1_angle_d_ac
    angle_c = triangle_1_angle_a + triangle_2_angle_d
    angle_d = 360 - (angle_a + angle_b + angle_c)
    return angle_a, angle_b, angle_c, angle_d


def quadrilateral_length_of_sides_coordinates(x1, y1, x2, y2, x3, y3, x4, y4):
    side_ab = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 3)
    side_bc = round(((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5, 3)
    side_cd = round(((x3 - x4) ** 2 + (y3 - y4) ** 2) ** 0.5, 3)
    side_ad = round(((x4 - x1) ** 2 + (y4 - y1) ** 2) ** 0.5, 3)
    diagonal_ac = round(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5, 3)
    diagonal_bd = round(((x4 - x2) ** 2 + (y4 - y2) ** 2) ** 0.5, 3)
    return side_ab, side_bc, side_cd, side_ad, diagonal_ac, diagonal_bd

# -------------------------------------------------------------------------------------------------


def triangle_respective_heights(area, a, b, c):
    height_for_a = 2 * area / a
    height_for_b = 2 * area / b
    height_for_c = 2 * area / c
    return height_for_a, height_for_b, height_for_c


def triangle_interior_angles_3sides(a, b, c):
    angle_a = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    angle_c = 180 - (angle_a + angle_b)
    return round(angle_a, 3), round(angle_b, 3), round(angle_c, 3)


def triangle_interior_angles_2sides_included_angle(a, b, angle_c):
    c = (a ** 2 + b ** 2 - (math.cos(angle_c) * 2 * a * b)) ** 0.5
    angle_a = round(math.degrees(
        math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))), 3)
    angle_b = round(180 - (angle_a + math.degrees(angle_c)), 3)
    return c, (angle_a, angle_b)


def triangle_length_of_sides_coordinates(x1, y1, x2, y2, x3, y3):
    side_ab = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 3)
    side_bc = round(((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5, 3)
    side_ac = round(((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5, 3)
    return side_ab, side_bc, side_ac

    shape_name = input("Enter Shape Name: ").lower()
    if shape_name == "square":
        side = float(input("Side: "))
        print(square(side))
    elif shape_name == "rectangle":
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        print(rectangle(length, breadth))
    elif shape_name == "parallelogram":
        base = float(input("Base: "))
        height = float(input("Height: "))
        print(parallelogram(base, height))
    elif shape_name == "rhombus":
        method = input("Method: Diagonals(d) / Base-Height(bh): ")
        if method == "d":
            d1 = float(input("Diagonal-1: "))
            d2 = float(input("Diagonal-2: "))
            print(rhombus_diagonal_method(d1, d2))
        elif method == "bh":
            base = float(input("Base: "))
            height = float(input("Height: "))
            print(rhombus_base_height_method(base, height))
    elif shape_name == "trapezium":
        h = float(input("Enter Height: "))
        b1 = float(input("Enter Base1: "))
        b2 = float(input("Enter Base2: "))
        print(trapezium(b1, b2, h))
    elif shape_name == "triangle":
        method = input(
            "Method: Base & Altitude(ba)/ Heron's Formula(3)/  SAS(sas)/ Coordinates(xy)/ Equilateral triangle(eq): ")
        if method == "ba":
            base = float(input("Base: "))
            height_ = float(input("Height: "))
            print(triangle_base_height_method(base, height_))
        elif method == "3":
            a = float(input("First Side(a): "))
            b = float(input("Second Side(b): "))
            c_ = float(input("Third Side(c): "))
            print(triangle_herons_formula_method(a, b, c_))
        elif method == "sas":
            a = float(input("First Side(a): "))
            b = float(input("Second Side(b): "))
            angle_c = math.radians(float(input("Included Angle{∠C°}: ")))
            print(triangle_side_angle_side_method(a, b, angle_c))
        elif method == "xy":
            x1, y1 = float(input("A(x- coordinate): ")
                           ), float(input("A(y- coordinate): "))
            x2, y2 = float(input("B(x- coordinate): ")
                           ), float(input("B(y- coordinate): "))
            x3, y3 = float(input("C(x- coordinate): ")
                           ), float(input("C(y- coordinate): "))
            print(triangle_coordinates_method(x1, y1, x2, y2, x3, y3))
        elif method == "eq":
            side = float(input("Side: "))
            print(triangle_equilateral(side))
    elif shape_name == "circle":
        radius = float(input("Radius: "))
        print(circle(radius))
    elif shape_name == "kite":
        d1 = float(input("Diagonal-1: "))
        d2 = float(input("Diagonal-2: "))
        print(kite(d1, d2))
    elif shape_name == "quadrilateral":
        method = input("Diagonal-Perpendicular(dp) / Coordinates(xy): ")
        if method == "dp":
            p1 = float(input("Perpendicular1: "))
            p2 = float(input("Perpendicular2: "))
            diagonal = float(input("Diagonal: "))
            print(quadrilateral_diagonal_perpendicular_method(diagonal, p1, p2))
        elif method == "xy":
            x1, y1 = float(input("A(x- coordinate): ")
                           ), float(input("A(y- coordinate): "))
            x2, y2 = float(input("B(x- coordinate): ")
                           ), float(input("B(y- coordinate): "))
            x3, y3 = float(input("C(x- coordinate): ")
                           ), float(input("C(y- coordinate): "))
            x4, y4 = float(input("D(x- coordinate): ")
                           ), float(input("D(y- coordinate): "))
            print(quadrilateral_xy_method())
    else:
        print("ENTER A SHAPE NAME THAT IS AVAILABLE.")

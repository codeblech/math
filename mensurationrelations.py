import math
math.pi = 22/7
shape = input("Cube / Cuboid / Rectangle / Square / Circle: ").lower()
while True:
    if shape == "cube":
        given = input("What value is known?  Volume(v) / Total Surface Area(tsa) / Curved Surface Area(csa): ").lower()
        if given == "v":
            volume = float(input("Volume: "))
            side = volume ** (1. / 3.)
            print(f"Side of Cube: {side}")
        elif given == "tsa":
            tsa = float(input("Total Surface Area: "))
            side = (tsa / 6) ** 0.5
            print(f"Side of Cube: {side}")
        elif given == "csa":
            csa = float(input("Curved Surface Area: "))
            side = (csa / 4) ** 0.5
            print(f"Side of Cube: {side}")
        else:
            print("Enter a valid value!")

    elif shape == "cuboid":
        volume = float(input("Volume: "))
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        height = float(input("Height: "))
        given = input('''What value is known?  Volume(v) / Total Surface Area(tsa) / Curved Surface Area(csa)"
/ Length(l) / Breadth(b) / Height(h): ''').lower()
        if given == "v l b" or given == "l v b" or given == "b v l" or given == "v b l " or given == "l b v" or given == "b l v":
            height = volume / (length * breadth)
            print(f"Height: {height}")
        elif given == "v l h" or given == "l v h" or given == "h v l" or given == "v h l " or given == "l h v" or given == "h l v":
            breadth = volume / (length * height)
            print(f"Breadth: {breadth}")
        elif given == "v h b" or given == "h v b" or given == "b v h" or given == "v b h " or given == "h b v" or given == "b h v":
            length = volume / (height * breadth)
            print(f"Length: {length}")
        else:
            print("Enter a valid value!")

    elif shape == "rectangle":
        perimeter = float(input("Perimeter: "))
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        area = float(input("Area: "))
        given = input("What value is known?  perimeter(p) / area(a) / length(l) / breadth(b): ").lower()
        if given == "p l" or given == "l p":
            breadth = (perimeter / 2) - length
            print(f"Breadth: {breadth}")
        elif given == "p b" or given == "b p":
            length = (perimeter / 2) - breadth
            print(f"Length: {length}")
        elif given == "a l" or given == "l a":
            breadth = area / length
            print(f"Breadth: {breadth}")
        elif given == "b a" or given == "a b":
            length = area / breadth
            print(f"Length: {length}")
        elif given == "a p" or given == "p a":
            a = 2
            b = -perimeter
            c = 2 * area
            discriminant = b ** 2 - 4 * a * c
            length1 = (-b + discriminant ** 0.5) / (2 * a)
            length2 = (-b - discriminant ** 0.5) / (2 * a)
            if length1 >= 1:
                breadth = area / length1
                print(
                    f'''Length: {length1} Breadth: {breadth}
Length: {breadth} Breadth: {length1} ''')
            elif length2 >= 1:
                breadth = area / length2
                print(f"Length: {length2} Breadth: {breadth}")
        else:
            print("Enter a valid value!")

    elif shape == "square":
        area = float(input("Area: "))
        perimeter = float(input("Perimeter: "))
        given = "What is known? Area(a) / Perimeter(p)"
        if given == "a":
            side = area ** 0.5
            diagonal = math.hypot(side, side)
            print(f"Side: {side}    Diagonal: {diagonal}")
        elif given == "p":
            side = perimeter / 4
            diagonal = math.hypot(side, side)
            print(f"Side: {side}    Diagonal: {diagonal}")
        else:
            print("Enter a valid value!")

    elif shape == "circle":
        radius = float(input("Radius: "))
        area = float(input("Area: "))
        circumference = float(input("Circumference: "))
        angle = (float(input("Angle: ")))
        arc_length = float(input("Arc Length: "))
        area_sector = float(input("Area of Sector: "))
        area_segment = float(input("Area of Segment: "))
        given = input('''What value is known?  Radius(r)/ Area(ar) / Circumference(c) / Angle-degrees(ang) / 
Arc Length(al) / Area of Sector(asec) / Area of segment(aseg)''')
        if given == "ar":
            radius = (area / math.pi) ** 0.5
            print(f"Radius: {radius}")
        elif given == "c":
            radius = circumference / (2 * math.pi)
            print(f"Radius: {radius}")
        elif given == "asec ang" or given == "ang asec":
            radius = ((area_sector * 360) / (math.pi * angle)) ** 0.5
            print(f"Radius: {radius}")
        elif given == "aseg ang" or given == "ang aseg":
            radius = (2 / (angle - math.sin(math.radians(angle)))) ** 0.5
            print(f"Radius: {radius}")
        elif given == "al":
            radius = arc_length * 180 / (math.pi * angle)
            print(f"Radius: {radius}")
        elif given == "asec r" or given == "r asec":
            angle = (area_sector * 360) / (math.pi * (radius ** 2))
            print(f"Angle: {angle}")
        elif given == "aseg r" or given == "r aseg":
            angle = (2 / (radius ** 2)) + math.sin(angle)
            print(f"Angle: {angle}")
        else:
            print("Enter a valid value!")

    else:
        print("Enter a valid response!")
        break




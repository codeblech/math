def centroid_of_triangle(x1, x2, x3, y1, y2, y3):
    centroid = (x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3
    print(f"Coordinates of Centroid: {centroid}")


x1, y1 = float(input("A(x- coordinate): ")), int(input("A(y- coordinate): "))
x2, y2 = float(input("B(x- coordinate): ")), int(input("A(y- coordinate): "))
x3, y3 = float(input("C(x- coordinate): ")), int(input("A(y- coordinate): "))

centroid_of_triangle(x1, x2, x3, y1, y2, y3)

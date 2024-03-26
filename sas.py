import math

if method == "sas":
    a = int(input("First Side: "))
    b = int(input("Second Side: "))
    angle = int(input("Included Angle: "))
    area = a * b * math.sin(angle) / 2

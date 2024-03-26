import math
math.pi = 22/7


def area(radius):
    area = math.pi * radius ** 2
    return f"Area: {area}"


def circumference(radius):
    circumference = 2 * math.pi * radius
    return f"Circumference: {circumference}"


def sector(radius, angle):
    area_sector = (math.pi * radius ** 2 * angle) / 360
    return f"Area of sector: {area_sector}"


def segment(radius, angle):
    area_segment = 0.5 * (angle - math.sin(angle)) * radius ** 2
    return f"Area of segment: {area_segment}"


def arc_length(radius, angle):
    length_arc = (2 * math.pi * radius * angle) / 360
    return f"Length of Arc: {length_arc}"


what = input("Area(a) / Circumference(c) / Area of Sector(sec) / Area of Segment(seg) / Length of Arc(arc): ")
radius = float(input("Radius: "))
if what == "sec" or what == "seg" or what == "arc":
    angle = float(input("Angle: "))
    if what == "a":
        print(area(radius))
    elif what == "c":
        print(circumference(radius))
    elif what == "sec":
        print(sector(radius, angle))
    elif what == "seg":
        print(segment(radius, angle))
    elif what == "arc":
        print(arc_length(radius, angle))
    else:
        print("Enter a valid response!")
# circular_segment_area(radius, angle, arc_length, chord_length, radius_minus_height, height_of_arced_portion, area)
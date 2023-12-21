import math


def intersection_line_line(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if det == 0:
        return None

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det

    return (px, py)


def intersection_line_segment(line, segment):
    x1, y1, x2, y2 = line
    x3, y3, x4, y4 = segment

    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if det == 0:
        return None

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det

    if min(x3, x4) <= px <= max(x3, x4) and min(y3, y4) <= py <= max(y3, y4):
        return (px, py)
    else:
        return None


def intersection_segment_segment(segment1, segment2):
    result1 = intersection_line_segment(segment1, segment2)
    result2 = intersection_line_segment(segment2, segment1)

    if result1 is not None and result2 is not None:
        return result1
    else:
        return None


def intersection_line_circle(line, circle):
    cx, cy, r = circle
    x1, y1, x2, y2 = line

    a = (x2 - x1) ** 2 + (y2 - y1) ** 2
    b = 2 * ((x2 - x1) * (x1 - cx) + (y2 - y1) * (y1 - cy))
    c = x1 ** 2 + y1 ** 2 + cx ** 2 + cy ** 2 - 2 * (x1 * cx + y1 * cy) - r ** 2

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None

    elif discriminant == 0:
        t = -b / (2 * a)
        px = x1 + t * (x2 - x1)
        py = y1 + t * (y2 - y1)
        return (px, py)
    else:

        t1 = (-b + math.sqrt(discriminant)) / (2 * a)
        t2 = (-b - math.sqrt(discriminant)) / (2 * a)
        px1 = x1 + t1 * (x2 - x1)
        py1 = y1 + t1 * (y2 - y1)
        px2 = x1 + t2 * (x2 - x1)
        py2 = y1 + t2 * (y2 - y1)
        return [(px1, py1), (px2, py2)]


def intersection_segment_circle(segment, circle):
    line_result = intersection_line_circle(segment, circle)

    if line_result is not None:
        if isinstance(line_result, tuple):
            if min(segment[0], segment[2]) <= line_result[0] <= max(segment[0], segment[2]) and \
                    min(segment[1], segment[3]) <= line_result[1] <= max(segment[1], segment[3]):
                return line_result
        elif isinstance(line_result, list):
            valid_results = []
            for point in line_result:
                if min(segment[0], segment[2]) <= point[0] <= max(segment[0], segment[2]) and \
                        min(segment[1], segment[3]) <= point[1] <= max(segment[1], segment[3]):
                    valid_results.append(point)
            return valid_results if valid_results else None

    return None


def intersection_circle_circle(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2

    # Расстояние между центрами окружностей
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if distance > r1 + r2 or distance < abs(r1 - r2):
        return None

    a = (r1 ** 2 - r2 ** 2 + distance ** 2) / (2 * distance)
    h = math.sqrt(r1 ** 2 - a ** 2)

    px1 = x1 + a * (x2 - x1) / distance + h * (y2 - y1) / distance
    py1 = y1 + a * (y2 - y1) / distance - h * (x2 - x1) / distance
    px2 = x1 + a * (x2 - x1) / distance - h * (y2 - y1) / distance
    py2 = y1 + a * (y2 - y1) / distance + h * (x2 - x1) / distance

    return [(px1, py1), (px2, py2)]


def create_line(point1, point2):
    return (*point1, *point2)


def create_segment(point1, point2):
    return (*point1, *point2)


def create_circle(center, radius):
    return (*center, radius)


point1 = (1, 0)
point2 = (1, 20)
point3 = (20, 1)
point4 = (2, 2)
point5 = (2, 4)
point6 = (5, 3)
point7 = (4, 2)
point8 = (7, 3)
point9 = (8, 4)
point10 = (12, 2)

# задание треугольника (большой)
segment1 = create_segment(point1, point2)
segment2 = create_segment(point2, point3)
segment3 = create_segment(point1, point3)

# задание треугольника (малый)
segment4 = create_segment(point4, point5)
segment5 = create_segment(point4, point6)
segment6 = create_segment(point6, point5)

# задание четырёхугольникаъ
segment7 = create_segment(point7, point8)
segment8 = create_segment(point8, point9)
segment9 = create_segment(point9, point10)
segment10 = create_segment(point10, point7)

# Нахождение точек пересечения
i1= intersection_segment_segment(segment4, segment1)
i2 = intersection_segment_segment(segment5, segment1)
i3 = intersection_segment_segment(segment6, segment1)
i4 = intersection_segment_segment(segment7, segment1)
i5 = intersection_segment_segment(segment8, segment1)
i6 = intersection_segment_segment(segment9, segment1)
i7 = intersection_segment_segment(segment10, segment1)


if i1 == i2 == i3 == i4 == i5 == i6 == i7 == None:
    print(point1)
    print(point2)
    print(point3)
    print(point4)
    print(point5)
    print(point6)
    print(point7)
    print(point8)
    print(point9)
    print(point10)

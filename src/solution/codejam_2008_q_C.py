
import math
import numpy
import sys

def square(x):
    return math.pow(x, 2)

def get_opposite_len(radius, x):
    return math.sqrt(square(radius) - square(x))

def get_wrong_pie_area(radius, x):
    # Return area right of vertical line
    angle = math.acos(x / radius)
    pie_area = square(radius) * angle / 2
    y = get_opposite_len(radius, x)
    return pie_area - (x * y / 2)

def get_curve_triangle_area(radius, x, y):
    border_x = get_opposite_len(radius, y)
    border_y = get_opposite_len(radius, x)

    #return (border_y - y) * (border_x - x) / 2

    wrong_pie_small = get_wrong_pie_area(radius, border_y)
    wrong_pie_large = get_wrong_pie_area(radius, y)

    rectangle = x * (border_y - y)

    return wrong_pie_large - wrong_pie_small - rectangle

def get_circle_square_intersection(radius, x, y, square_size):
    # x, y denotes bottom-left corner of gap square
    
    def is_inside(x, y):
        #print("is_inside ", (x), (y), (radius), square(x) + square(y), square(radius))
        return square(x) + square(y) < square(radius)

    #print ("args", radius, x, y, square_size)

    

    if (not is_inside(x, y)):
        return 0
    
    elif (is_inside(x + square_size, y + square_size)):
        return square(square_size)

    else:
        offset_area = 0

        if (is_inside(x, y + square_size)):
            new_x = get_opposite_len(radius, y + square_size)
            offset_area += square_size * (new_x - x)
        else:
            new_x = x

        if (is_inside(x + square_size, y)):
            #print("b")
            new_y = get_opposite_len(radius, x + square_size)
            offset_area += (x + square_size - new_x) * (new_y - y)
        else:
            new_y = y

        return offset_area + get_curve_triangle_area(radius, new_x, new_y)

def solve(input, output):
    def get_int():
        return int(input.readline().strip())

    def get_string():
        return input.readline().strip()

    def solve_case():
        fly_r, racket_outer_r, racket_thickness, string_r, gap = [float(x) for x in get_string().split(" ")]
        racket_inner_r = racket_outer_r - racket_thickness - fly_r
        
        # Consider only 1/4 of the circle of racket (1st quarter where x >= 0 and y >= 0)
        total_area = 0.25 * math.pi *  racket_outer_r * racket_outer_r

        # Repeating pattern, which has square hole in its center
        unit_square_size = gap - 2 * fly_r
        if (unit_square_size < 0):
            return 1

        interval = gap + 2 * string_r

        # We will calculate area of all gaps
        total_gap_area = 0
        
        # x, y denotes bottom-left corner of gap square
        first_square_position = string_r + fly_r

        for x in numpy.arange(first_square_position, racket_inner_r, interval):
            right = x + unit_square_size
            top_y = get_opposite_len(right)
            num_squares = (top_y - fly_r - string_r) // interval
            last_y = interval * num_squares


            total_gap_area += get_circle_square_intersection(racket_inner_r, x, last_y, unit_square_size)

        answer = 1 - (total_gap_area / total_area)
        print("Line", total_area, total_gap_area, answer)
        return answer

    num_cases = get_int()
    for i in range(num_cases):        
        output.write("Case #{}: {:.12f}\n".format(i + 1, solve_case()))

def test():
    test_cases = [
        (1, 0, 0, 0.5),
        (1, 0.0, 0.0, 0.7),
        (1, 0.0, 0.0, 1)
    ]
    for test_case in test_cases:
        print(f"Test case: {test_case}, result {get_circle_square_intersection(*test_case)}")
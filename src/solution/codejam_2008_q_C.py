
import math
import numpy

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

def get_triangle_area_of_circle(radius, x, y, square_size):
    # x, y denotes bottom-left corner of gap square
    
    def is_strict_inside(x, y):
        print(x, y)
        return square(x) + square(y) < square(radius)

    def is_inclusive_inside(x, y):
        return square(x) + square(y) <= square(radius)


    print (radius, x, y, square_size)

    if (not is_strict_inside(x, y)):
        return 0
    
    elif (is_inclusive_inside(x + square_size, y + square_size)):
        return square(square_size)

    elif (is_strict_inside(x, y + square_size)):
        new_x = get_opposite_len(radius, y + square_size)
        offset_area = square_size * (new_x - x)
        print("a", y + square_size)
        return get_triangle_area_of_circle(radius, new_x, y, square_size)

    elif (is_strict_inside(x + square_size, y)):
        #print("b")
        return get_triangle_area_of_circle(radius, y, x, square_size)

    else:
        border_y = get_opposite_len(radius, x)

        wrong_pie_small = get_wrong_pie_area(radius, border_y)
        wrong_pie_large = get_wrong_pie_area(radius, y)

        rectangle = x * (border_y - y)

        return wrong_pie_large - wrong_pie_small - rectangle

def solve(input, output):
    def get_int():
        return int(input.readline().strip())

    def get_string():
        return input.readline().strip()

    def solve_case():
        fly_r, racket_outer_r, racket_thickness, string_r, gap = [float(x) for x in get_string().split(" ")]
        racket_inner_r = racket_outer_r - racket_thickness

        # Consider only 1/4 of the circle of racket (1st quarter where x >= 0 and y >= 0)
        total_area = 0.25 * math.pi *  racket_outer_r * racket_outer_r

        # Repeating pattern, which has square hole in its center
        unit_square_size = gap + 2 * string_r

        # We will calculate area of all gaps
        total_gap_area = 0
        
        print("Line", racket_inner_r, unit_square_size)
        # x, y denotes bottom-left corner of gap square
        for x in numpy.arange(0, racket_inner_r, unit_square_size):
            for y in numpy.arange(0, racket_inner_r, unit_square_size):
               # print("Line", racket_inner_r, x, y, unit_square_size)
                get_triangle_area_of_circle(racket_inner_r, x, y, unit_square_size)

        return f"{0.9999:.6f}"

    num_cases = get_int()
    for i in range(num_cases):        
        output.write("Case #{}: {}\n".format(i + 1, solve_case()))

def test():
    test_cases = [
        (1, 0, 0, 0.5),
        (1, 0.5, 0.5, 0.5)
    ]
    for test_case in test_cases:
        print(f"Test case: {test_case}, result {get_triangle_area_of_circle(*test_case)}")
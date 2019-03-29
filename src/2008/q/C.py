import math
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
    border_y = get_opposite_len(radius, x)

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
            new_y = get_opposite_len(radius, x + square_size)
            offset_area += (x + square_size - new_x) * (new_y - y)
        else:
            new_y = y

        return offset_area + get_curve_triangle_area(radius, new_x, new_y)

def solve():
    def get_int():
        return int(sys.stdin.readline().strip())

    def get_string():
        return sys.stdin.readline().strip()

    def solve_case():
        fly_r, racket_outer_r, racket_thickness, string_r, gap = \
            [float(x) for x in get_string().split(" ")]
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

        x = first_square_position

        fast_mode = True
        #fast_mode = False

        while x < racket_inner_r:
            if (fast_mode):
                right = x + unit_square_size
                if right > racket_inner_r:
                    right = racket_inner_r

                top_y = get_opposite_len(racket_inner_r, right)
                first_top_y = string_r + fly_r + unit_square_size
                first_bottom_y = string_r + fly_r

                num_squares = (top_y - first_top_y) // interval + 1
                
                #print(right, top_y, num_squares)
                total_gap_area += square(unit_square_size) * num_squares
                
                bottom_y = first_bottom_y + interval * num_squares
                while bottom_y < get_opposite_len(racket_inner_r, x):
                    total_gap_area += get_circle_square_intersection(
                        racket_inner_r, x, bottom_y, unit_square_size)
                    bottom_y += interval
            else:
                y = first_square_position
                while y < racket_inner_r:
                    total_gap_area += get_circle_square_intersection(
                        racket_inner_r, x, y, unit_square_size)

                    y += interval

            x += interval

        answer = 1 - (total_gap_area / total_area)
        return answer

    num_cases = get_int()
    for i in range(num_cases):   
        sys.stdout.write("Case #{}: {:.6f}\n".format(i + 1, solve_case()))

solve()
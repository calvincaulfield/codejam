
import math

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

        for x in range(0, racket_inner_r, unit_square_size):


        
        return f"{0.9999:.6f}"

    num_cases = get_int()
    for i in range(num_cases):        
        output.write("Case #{}: {}\n".format(i + 1, solve_case()))

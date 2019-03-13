
def solve(input, output):
    def get_int():
        return int(input.readline().strip())

    def get_string():
        return input.readline().strip()

    def solve_case():

        fly_r, racket_outer_r, racket_thickness, string_r, gap = 1, 2, 3, 4, 5
        return 0
        
    num_cases = get_int()
    for i in range(num_cases):        
        output.write("Case #{}: {}\n".format(i + 1, solve_case()))

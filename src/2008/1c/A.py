import sys

def solve():
    def get_int():
        return int(sys.stdin.readline().strip())

    def get_string():
        return sys.stdin.readline().strip()

    def get_ints():
        return [int(x) for x in get_string().split(" ")] 
    
    def solve_case():
        _, num_buttons, _ = get_ints()
        frequencies = get_ints()
        frequencies.sort()
        frequencies.reverse()

        total_cost = 0

        for i, frequency in enumerate(frequencies):
            total_cost += frequency * (i // num_buttons + 1)
        return total_cost

    num_cases = get_int()
    for i in range(num_cases):        
        sys.stdout.write("Case #{}: {}\n".format(i + 1, solve_case()))

solve()
def solve(input, output):

    def get_int():
        return int(input.readline().strip())

    def get_ints():
        return [int(x) for x in input.readline().strip().split(" ")]

    def solve_case():
        n, m, X, Y, Z = get_ints()
        A = []
        speed_list = []

        for i in range(m):
            A.append(get_int())

        for i in range(n):
            speed_list.append(A[i % m])
            A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

        speed_list.sort()
        number_to_order = {}
        index = 0
        for i, speed in enumerate(speed_list):
            number_to_order[speed] = index
            if (i < len(speed_list) - 1 and speed_list[i + 1] == speed):
                pass
            else:
                index += 1

        for i, speed in enumerate(speed_list):
            speed_list[i] = number_to_order[speed]

        return 0

    num_cases = get_int()
    for i in range(num_cases):        
        output.write("Case #{}: {}\n".format(i + 1, solve_case()))


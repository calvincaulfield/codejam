import sys

def solve():

    def get_int():
        return int(sys.stdin.readline().strip())

    def get_ints():
        return [int(x) for x in sys.stdin.readline().strip().split(" ")]

    def solve_case():
        n, m, X, Y, Z = get_ints()
        A = []
        speed_list = []
        
        mode = 1000000007

        for i in range(m):
            A.append(get_int())

        for i in range(n):
            speed_list.append(A[i % m])
            A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z
        sorted_speed_list = list(speed_list)
        sorted_speed_list.sort()

        number_to_order = {}
        index = 0
        for i, speed in enumerate(sorted_speed_list):
            number_to_order[speed] = index
            if (i < len(sorted_speed_list) - 1 and sorted_speed_list[i + 1] == speed):
                pass
            else:
                index += 1

        # speed_list's values are now integers 0 ~ n-1 (maybe with duplicats)
        for i, speed in enumerate(speed_list):
            speed_list[i] = number_to_order[speed]
        # record[i] means # of increasing sub-sequences with last element <= i
        record = [0] * n
        for order in speed_list:
            # Single point sequence
            new_possibilities = 1
            if (order > 0):
                new_possibilities += record[order - 1]
            for i in range(order, n):
                record[i] = (record[i] + new_possibilities) % mode
        print(record[-1])
        return record[-1] % mode

    num_cases = get_int()
    for i in range(num_cases):        
        sys.stdout.write("Case #{}: {}\n".format(i + 1, solve_case()))

#solve()
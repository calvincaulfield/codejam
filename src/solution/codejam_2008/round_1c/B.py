
def solve(input, output):

    mode = 2 * 3 * 5 * 7

    def get_int():
        return int(input.readline().strip())

    def get_string():
        return input.readline().strip()

    def get_empty_list():
        return [0] * mode

    def list_for_number(number):
        new_list = get_empty_list()
        new_list[number % mode] = 1
        return new_list

    def add_number_to_list(number, inlist):
        new_list = get_empty_list()
        for i in range(mode):
            new_list[(i + number) % mode] = inlist[i]
        return new_list

    def get_minus_list(inlist):
        new_list = get_empty_list()
        for i in range(mode):
            new_list[-i % mode] = inlist[i]
        return new_list

    def add_list(original, plus):
        for i in range(mode):
            original[i] += plus[i]
        return original

    def solve_case():
        line = get_string()

        record = {}

        def get_freq_mode_list(number_string):
            if (number_string in record):
                return record[number_string]

            if (len(number_string) == 1):
                answer = list_for_number(int(number_string))                
            else:
                total = get_empty_list()

                # There is at least one operator
                # len_leftmost means # chars before first operator from left
                for len_leftmost in range(1, len(number_string)):
                    number = int(number_string[:len_leftmost])
                    list_for_remaining = get_freq_mode_list(number_string[len_leftmost:])

                    add_list(total, add_number_to_list(number, list_for_remaining))
                    add_list(total, add_number_to_list(number, get_minus_list(list_for_remaining)))

                # No operator at all
                add_list(total, list_for_number(int(number_string)))
                answer = total

            record[number_string] = answer
            return answer

        result = get_freq_mode_list(line)
        num_ugly_nums = 0
        for i in range(mode):
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                num_ugly_nums += result[i]  

        return num_ugly_nums

    num_cases = get_int()
    for i in range(num_cases):        
        output.write("Case #{}: {}\n".format(i + 1, solve_case()))


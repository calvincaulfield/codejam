
def solve(input, output):
    def get_int():
        return int(input.readline().strip())

    def get_string():
        return input.readline().strip()

    def solve_case(num):
        servers = {}
        num_used_server = 0
        num_servers = get_int()
        num_server_change = 0

        for _ in range(num_servers):
            servers[get_string()] = False
        
        num_search_keywords = get_int()
        for _ in range(num_search_keywords):
            keyword = get_string()
            if (servers[keyword]):
                pass
            else:                
                if (num_used_server + 1 == num_servers):
                    # We need to change server now, before processing this keyword (though we don't know which one)
                    num_server_change += 1

                    # Start new cycle
                    for x in servers:
                        servers[x] = False
                    num_used_server = 0

                num_used_server += 1
                servers[keyword] = True

        output.write("Case #{}: {}\n".format(num, num_server_change))

    num_cases = get_int()
    for i in range(num_cases):
        solve_case(i + 1)

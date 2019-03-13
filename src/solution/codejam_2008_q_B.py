
def solve(input, output):
    def get_int():
        return int(input.readline().strip())

    def get_string():
        return input.readline().strip()

    def solve_case():
        # All time units are minute
        turn_around_time = get_int()
        num_a_to_b, num_b_to_a = [int(x) for x in get_string().split(" ")]

        # Departure time includes turnaround time
        a_departures = []
        a_arrivals = []
        b_departures = []
        b_arrivals = []
        a_min = 0
        b_min = 0

        def process_timetable(num, departure_station, arrival_station):
            for _ in range(num):
                time_pair = [x for x in get_string().split(" ")]
                departure, arrival = [60 * int(x.split(":")[0]) + int(x.split(":")[1]) for x in time_pair]
                departure_station.append(departure)
                arrival_station.append(arrival + turn_around_time)

        def get_max_debt(departures, arrivals):
            current = 0
            minimum = 0
            all_list = [(x, "departure") for x in departures] + [(x, "arrival") for x in arrivals]
            all_list.sort()
            for entry in all_list:
                if (entry[1] == "departure"):
                    current -= 1
                    if (current < minimum):
                        minimum = current
                else:
                    current += 1
            return -minimum

        process_timetable(num_a_to_b, a_departures, b_arrivals)
        process_timetable(num_b_to_a, b_departures, a_arrivals)

        return (get_max_debt(a_departures, a_arrivals), get_max_debt(b_departures, b_arrivals), )
        #print(a_departures, a_arrivals)

    num_cases = get_int()
    for i in range(num_cases):        
        x, y = solve_case()
        output.write("Case #{}: {} {}\n".format(i + 1, x, y))

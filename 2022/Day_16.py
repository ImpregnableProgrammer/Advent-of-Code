def first_part(valves): # have 30 minutes max
    tunnels = dict()
    # Parse input and populate dictionary
    for valve in valves:
        valve = valve.split(' ')
        tunnels[valve[1]] = {
            "rate": int(valve[4].split('=')[1].replace(';', '')),
            "valves": [v.replace(',', '') for v in valve[9:]]
        }
    print(tunnels)
    paths = [("AA", tuple(), ("AA",), 30, 0)]
    max = 0
    while len(paths):
        valve, opened, path, time, pressure = paths.pop(0)
        # print(valve, edges, opened, '\n')
        if pressure > max:
            max = pressure
            print(max, opened, path)
        time -= 1 # either opened `valve` or moved to next one
        for v in tunnels[valve]["valves"]:
            if v in opened or (valve, v) not in zip(path, path[1:]):
                closed = (v, opened, path + (v,), time, pressure)
                paths.append(closed)
                if valve not in opened and time > 0 and tunnels[valve]["rate"] > 0:
                    # open `valve` and move to next valve `v`
                    open = (v, opened + (valve,), path + (v,), time - 1, 
                            pressure + tunnels[valve]["rate"] * time)
                    paths.append(open)
    return max

# corect path: AA, DD, CC, BB, AA, II, JJ, II, AA, DD, EE, FF, GG, HH, GG, FF, EE, DD, CC
Sample = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''.split('\n')
Input = open("Inputs/Day_16.txt").read().split('\n')
print(first_part(Sample))
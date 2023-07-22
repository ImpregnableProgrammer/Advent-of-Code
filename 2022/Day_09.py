# Not done!!
def first_part(moves):
    head = tail = (0, 0)
    adj = lambda h, t: t in ((h[0]+dx, h[1]+dy) for dy in range(-1, 2) for dx in range(-1, 2))
    for move in moves:
        move = move.split(" ")
        dir, dist = (move[0], int(move[1]))
        for _ in range(dist):
            dx, dy = (1 if dir == "R" else -1 if dir == "L" else 0, \
                1 if dir == "D" else -1 if dir == "U" else 0)
            head = (head[0] + dx, head[1] + dy)
            if not adj(head, tail):
                if head[0] == tail[0]:
                    tail = (tail[0] + dx, tail[1])
                elif head[1] == tail[1]:
                    tail = (tail[0], tail[1] + dy)
                else:
                    


Input = open("Inputs/Day_09.txt").read().split("\n")[:-1]
print(first_part(Input))
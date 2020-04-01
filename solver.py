import rubik

def shortest_path(start, end):
    """
    For Question 1, using BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """

    L = [[start, []]]

    visited = {start}

    mov = None

    while len(L) != 0:
        cur = L[0]
        L = L[1:]
        if cur[0] == end:
            mov = cur[1]
            break
        for twist in rubik.quarter_twists:
            x = (rubik.perm_apply(twist, cur[0]), cur[1] + [rubik.quarter_twists_names[twist]])
            if x[0] not in visited:
                visited.add(x[0])
                L.append(x)

    print(mov)

def shortest_path_optmized(start, end):
    """
    For Question 2, using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    raise NotImplementedError

start = (6, 7, 8, 0, 1, 2, 9, 10, 11, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
end = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)

shortest_path(start, end)
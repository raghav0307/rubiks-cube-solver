import rubik
import Queue
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

def reversal_name(s):
    if(s=="F"):
        return "Fi"
    elif(s=="Fi"):
        return "F"
    elif(s=="Li"):
        return "L"
    elif(s=="L"):
        return "Li"
    elif(s=="U"):
        return "Ui"
    else:
        return "U"

def shortest_path_optmized(start, end):
    """
    For Question 2, using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    q_front = Queue.Queue()
    q_front.put([start,[]])
    visited_front = {start:[]}

    q_back = Queue.Queue()
    q_back.put([end,[]])
    visited_back  = {end:[]}

    if start == end : 
        print([])
        return 

    while not q_back.empty() or not q_front.empty():

        if not q_front.empty():

            cur_front = q_front.get()

            for twist in rubik.quarter_twists:

                x = (rubik.perm_apply(twist, cur_front[0]), cur_front[1] + [rubik.quarter_twists_names[twist]])
                
                if x[0] in visited_back:
                    print(x[1] + visited_back[x[0]][::-1])
                    return 

                if x[0] not in visited_front:
                    visited_front[x[0]] = x[1][:]
                    if(len(x[1])<=7):
                        q_front.put(x)

        if not q_back.empty():

            cur_back = q_back.get()

            for twist in rubik.quarter_twists:
                x = (rubik.perm_apply(twist, cur_back[0]), cur_back[1] + [reversal_name(rubik.quarter_twists_names[twist])])

                if x[0] in visited_front:
                    print(visited_front[x[0]] + x[1][::-1])
                    return 

                if x[0] not in visited_back:
                    visited_back[x[0]] = x[1][:]
                    if(len(x[1])<=7):
                        q_back.put(x)
    print("None")




#length 4
start = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
end= (18, 19, 20, 13, 14, 12, 7, 8, 6, 0, 1, 2, 9, 10, 11, 15, 16, 17, 4, 5, 3, 21, 22, 23)
shortest_path_optmized(start, end)
shortest_path(start,end)
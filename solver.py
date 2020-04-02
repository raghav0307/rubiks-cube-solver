import rubik
import Queue
import random
def shortest_path(start, end):
    """
    For Question 1, using BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves.

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    L = Queue.Queue()
    L.put([start, []])

    visited = {start}
    mov = None

    while not L.empty():
        cur = L.get()
        if cur[0] == end:
            mov = cur[1]
            break
        for twist in rubik.quarter_twists:
            x = (rubik.perm_apply(twist, cur[0]), cur[1] + [rubik.quarter_twists_names[twist]])
            if x[0] not in visited:
                visited.add(x[0])
                L.put(x)

    print(mov)
    return mov

def reversal_name(s):
    r = ""
    if s == "F" :
        r = "Fi"
    elif s == "Fi" :
        r = "F"
    elif s == "Li":
        r = "L"
    elif s == "L" :
        r = "Li"
    elif s == "U":
        r = "Ui"
    else:
        r = "U"
    return r

def shortest_path_optmized(start, end):
    """
    For Question 2, using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    q_front = Queue.Queue()
    q_front.put([start, []])
    visited_front = {start : []}

    q_back = Queue.Queue()
    q_back.put([end, []])
    visited_back  = {end: [] }

    if start == end : 
        print([])
        return []

    while not q_back.empty() or not q_front.empty():

        if not q_front.empty():

            cur_front = q_front.get()

            for twist in rubik.quarter_twists:

                x = (rubik.perm_apply(twist, cur_front[0]), cur_front[1] + [rubik.quarter_twists_names[twist]])
                
                if x[0] in visited_back:
                    print(x[1] + visited_back[x[0]][::-1])
                    return x[1] + visited_back[x[0]][::-1]

                if x[0] not in visited_front:
                    visited_front[x[0]] = x[1][:]
                    if len(x[1]) <= 7 :
                        q_front.put(x)

        if not q_back.empty():

            cur_back = q_back.get()

            for twist in rubik.quarter_twists:
                x = (rubik.perm_apply(twist, cur_back[0]), cur_back[1] + [reversal_name(rubik.quarter_twists_names[twist])])

                if x[0] in visited_front:
                    print(visited_front[x[0]] +  x[1][::-1])
                    return visited_front[x[0]] +  x[1][::-1]

                if x[0] not in visited_back:
                    visited_back[x[0]] = x[1][:]
                    if len(x[1]) <= 7 :
                        q_back.put(x)
    print("None")

def test(x):
    l = [rubik.L,rubik.F,rubik.Fi,rubik.Li,rubik.Ui]
    t= {"L":rubik.L,"F":rubik.F,"Fi":rubik.Fi,"Li":rubik.Li,"Ui":rubik.Ui,"U":rubik.U}
    start = (6, 7, 8, 0, 1, 2, 9, 10, 11, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
    end  = (6, 7, 8, 0, 1, 2, 9, 10, 11, 3, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
    
    for i in range(x):
        end = rubik.perm_apply(end,l[random.randrange(0,5)])
    
    ans1= shortest_path_optmized(start,end)
    current = start
    for move in ans1:
        current = rubik.perm_apply(t[move], current)
    if(current!=end):
        print(start,end,"Optimised failed")
        exit()
    else:
        print("Optimised ok")

    #bruteforce will take large time otherwise
    if(len(ans1)>6):
        return
    ans2= shortest_path(start,end)
    current = start
    for move in ans2:
        current = rubik.perm_apply(t[move], current)
    if(current!=end):
        print(start,end,"Bruteforce failed")
        exit()
    else:
        print("Bruteforce ok")

def test_suite():
    for i in range(int(input("Enter number of testcase "))):
        test(random.randrange(7,12))#larger random number means high chances of longer path


test_suite()
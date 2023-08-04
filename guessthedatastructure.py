import sys
from collections import deque
import queue as Q

def stack(actions, values):
    s = []
    for i in range(len(actions)):
        if actions[i] == 1:
            s.append(values[i])
        elif len(s) == 0:
            return False
        elif s.pop() != values[i]:
            return False
    return True
            
def queue(actions, values):
    q = deque()
    for i in range(len(actions)):
        if actions[i] == 1:
            q.append(values[i])
        elif len(q) == 0:
            return False
        elif q.popleft() != values[i]:
            return False
    return True

def priority_queue(actions, values):
    pq = Q.PriorityQueue()
    for i in range(len(actions)):
        if actions[i] == 1:
            pq.put((-values[i], values[i]))
        elif pq.empty():
            return False
        elif pq.get()[1] != values[i]:
                return False
    return True

for line in sys.stdin:
    n = int(line)
    actions = []
    values = []
    for i in range(n):
        action, val = list(map(int, input().split()))
        actions.append(action)
        values.append(val)
    #print(actions, values)

    s = stack(actions, values)
    q = queue(actions, values)
    pq = priority_queue(actions, values)
    
    if not s and not q and not pq:
        print("impossible")
    elif s and not q and not pq:
        print("stack")
    elif not s and q and not pq:
        print("queue")
    elif not s and not q and pq:
        print("priority queue")
    else:
        print("not sure")

    

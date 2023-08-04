# data structures

n = int(input())

while n != 0:
    first = []
    second = []
    
    # get values
    for i in range(n):
        first.append(int(input()))
    for i in range(n):
        second.append(int(input()))
        
    # create sorted versions of the lists
    firstS = first.copy()
    secondS = second.copy()
    
    firstS.sort()
    secondS.sort()
    
    # Create correspondence function as a dictionary
    correspondence = dict(list(zip(firstS, secondS)))
    
    # for the order of firsts, print each corresponding value
    for current in first:
        print(correspondence[current])

    n = int(input())
    print()

n = int(input())

while n != 0:

    foods = {}
    
    for i in range(n):
        name, *food = input().split()

        for f in food:
            if not f in foods:
                foods[f] = set()
            foods[f].add(name)
        
        #print(name, food)


    keys = list(foods.keys())
    keys.sort()
        
    for key in keys:
        names = list(foods[key])
        names.sort()
        print(key, ' '.join(names))

    print()
        
    n = int(input())


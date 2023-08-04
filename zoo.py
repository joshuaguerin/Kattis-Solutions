
n = int(input())
iterations = 1

while n != 0:
    animals = {}
    
    for i in range(n):
        line = input().split()
        animal = line[-1].lower()
        if animal in animals:
            animals[animal] += 1
        else:
            animals[animal] = 1

    keys = sorted(animals.keys())

    print("List ", iterations, ":", sep='')
    
    for key in keys:
        print(key, '|', animals[key])
    
    n = int(input())
    iterations += 1

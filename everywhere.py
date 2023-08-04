tests = int(input())

for i in range(tests):
    cities = set([])
    num_cities = int(input())
    for j in range(num_cities):
        current = input()
        cities.add(current)
    print(len(cities))

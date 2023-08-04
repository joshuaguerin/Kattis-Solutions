n = int(input())

building = set()

# Run simulation
for i in range(n):
    (action, person) = input().split()
    if action == "entry":
        print(person, "entered", end='')
        if person in building:
            print(" (ANOMALY)")
        else:
            print()
            building.add(person)
    else:
        print(person, "exited", end='')
        if not person in building:
            print(" (ANOMALY)")
        else:
            print()
            building.remove(person)

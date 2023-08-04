n = int(input())

for i in range(n):
    (name, start, birth, courses) = input().split()
    
    birth = int(birth[:4])
    start = int(start[:4])
    courses = int(courses)
    
    
    if start >= 2010:
        print(name, "eligible")
    elif birth >= 1991:
        print(name, "eligible")
    elif courses >= 41:
        print(name, "ineligible")
    else:
        print(name, "coach petitions")

# easy, string processing, brute force, counting

line = input()

i = 1

while line != "END":
    # generate "white" pixel strings
    dots = line.split('*')[1:-1]
    
    # not optimal, but should be fine here
    if len(set(dots)) == 1 or len(set(dots)) == 0:
        print(i, "EVEN")
    else:
        print(i, "NOT EVEN")
        
    line = input()
    i += 1


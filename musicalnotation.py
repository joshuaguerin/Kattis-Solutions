n = int(input()) # unused
notes = input().split()

output = []

# letters in staff in order
letters= "GFEDCBAgfedcba"
# each map becomes a column in the output
staff = {"G":" ", "F":"-", "E":" ", "D":"-", "C":" ", "B":"-", "A":" ", "g":"-", "f":" ", "e":"-", "d":" ", "c":" ", "b":" ", "a":"-"}

# add first column (letter labels)
output.append(["G: ", "F: ", "E: ", "D: ", "C: ", "B: ", "A: ", "g: ", "f: ", "e: ", "d: ", "c: ", "b: ", "a: "])

# process each note
for note in notes:
    # get note duration
    duration = 1
    if len(note) > 1:
        duration = int(note[1])

    # repeat duration times
    for i in range(duration):
        s = staff.copy()
        # add note at appropriate location
        s[note[0]] = "*"
        new = []
        for l in letters:
            new.append(s[l])
        output.append(new)
        
    # add space between notes
    output.append(list(" - - - - -   -"))

# remove last lines
output.pop()

# output each line, one row at a time
for i in range(len(output[0])):
    for j in range(len(output)):
        print(output[j][i], end="")
    print()



n = int(input())

for i in range(n):
    recording = input()
    recording = " " + recording + " "
    sounds = []

    # read in test cases
    line = input()
    while line != "what does the fox say?":
        word = line.split()[2]
        
        sounds.append(" " + word + " ")
        
        line = input()

    # check if there are replacements
    replace = False
    for word in sounds:
        replace = replace or word in recording

    # Keep doing replacements while replacements can be made
    while replace:
        for word in sounds:
            recording = recording.replace(word, " ")

        replace = False
            
        for word in sounds:
            replace = replace or word in recording

    print(recording.strip())

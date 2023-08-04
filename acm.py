line = input()

wrong = {}
solved = 0
total_time = 0

while line != "-1":  
    minutes, problem, status = line.split()

    # Accumulate time for wrong answers
    if status == "wrong":
        if problem in wrong:
            wrong[problem] += 20
        else:
            wrong[problem] = 20
    else:
        # Accumulate in solved problems
        solved += 1
        total_time += int(minutes)

        # Add accumulated errors
        if problem in wrong:
            total_time += wrong[problem]
    
    line = input()


print(solved, total_time)

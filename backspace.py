# strings, efficiency

line = list(input())

to_delete = 0
to_print = []

for i in range(len(line)-1, -1, -1):
    if line[i] == '<':
        to_delete += 1
    elif to_delete > 0:
        to_delete -= 1
    else:
        to_print.append(line[i])
        
print(''.join(to_print[::-1]))

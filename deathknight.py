# easy, string, substring

n = int(input())

won = 0

for i in range(n):
    line = input()
    
    if line.find('CD') == -1:
        won += 1

print(won)

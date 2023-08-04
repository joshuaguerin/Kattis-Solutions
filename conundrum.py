cypher = input()
per = "PER" * (len(cypher)//3)

differ = 0
for i in range(len(cypher)):
    if cypher[i] != per[i]:
        differ += 1
print(differ)



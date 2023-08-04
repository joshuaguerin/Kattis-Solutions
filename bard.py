# easy, set, union

n = int(input())
e = int(input())

songs = [set() for i in range(e)]
knows = [set() for i in range(n+1)]

# accumulate info on who was present each night
for i in range(e):
    night_total = set(list(map(int, input().split()))[1:])
    songs[i] = night_total

# accumulate song knowledge
for i in range(e):
    # the bard was there, add day to the total of everyone present
    if 1 in songs[i]:
        for p in songs[i]:
            knows[p].add(i)
    # bard was not there, everyone gets each other's songs
    else:
        # gather a list of songs for everyone present
        all_songs = set()
        for p in songs[i]:
            all_songs = all_songs | knows[p]
        for p in songs[i]:
            knows[p] = knows[p] | all_songs

# print out everyone who has the same songs as the bard
for i in range(len(knows)):
    if len(knows[1]) == len(knows[i]):
        print(i)



    

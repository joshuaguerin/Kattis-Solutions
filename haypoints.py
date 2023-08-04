# data structures, dictionary, text processing

(words, descriptions) = list(map(int, input().split()))

hay_dict = {}

# Generate hay dictionary
for i in range(words):
    (word, amount) = input().split()
    amount = int(amount)
    hay_dict[word] = amount

# Create totals for each description
for i in range(descriptions):
    amount = 0
    
    line = input()
    
    while line != '.':
        line = line.split()
        for word in line:
            if word in hay_dict:
                amount += hay_dict[word]
        line = input()

    print(amount)



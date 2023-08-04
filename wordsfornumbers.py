# string processing, text substitution

import sys

translate = {"10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", "15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen", "19":"nineteen"}

tenslate = {"2":"twenty", "3":"thirty", "4":"forty", "5":"fifty", "6":"sixty", "7":"seventy", "8":"eighty", "9":"ninety"}

oneslate = {"1":"-one", "2":"-two", "3":"-three", "4":"-four", "5":"-five", "6":"-six", "7":"-seven", "8":"-eight", "9":"-nine", "0":""}


def wordify(num):
    if num == "0":
        return "zero"
    if len(num) == 1:
        return oneslate[num][1:]
    elif len(num) == 2 and num[0]== '1':
        return translate[num]
    elif len(num) == 2:
        return tenslate[num[0]] + oneslate[num[1]]
        
# required because of "read until eof"
for line in sys.stdin:
    line = line.split()
    
    for i in range(len(line)):
        try:
            int(line[i])
            num = wordify(line[i])
            if i != 0:
                print(num, end=' ')
            else:
                print(num[0].upper(), num[1:], sep='', end=' ')
        except:
            print(line[i], end=' ')

    print()


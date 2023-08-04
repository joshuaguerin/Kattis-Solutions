A
bases = list("0123456789abcdefghijklmnopqrstuvwxyz0")

# brute-force the one case
def try_unary(x, op, y, z):
    if all(list(map(lambda x:x=="1", x))) and all(list(map(lambda x:x=="1", y))) and all(list(map(lambda x:x=="1", z))):
        return eval(str(len(x)) + op + str(len(y))) == len(z)

# integer cast with base conversion + eval == awesome
def try_base(x, op, y, z, base):
    try:
        return eval(str(int(x, base)) + op + str(int(y, base)))==int(z, base)
    except:
        return False

n = int(input())
for i in range(n):
    (x, op, y, eq, z) = input().split()

    valid = ""

    if try_unary(x, op, y, z):
        valid = "1"
        
    for base in range(2, 37):
        
        if try_base(x, op, y, z, base):
            valid = valid + bases[base]
    
    if valid != "":
        print(valid)
    else:
        print("invalid")
B


rot_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

def rot(string, rotation):
    new = ""
    for c in string:
        new = new + rot_str[(rot_str.find(c)+rotation) % len(rot_str)]
    return new[::-1]

line = input()

while line != "0":
    (rotation, string) = line.split()
    rotation = int(rotation)

    print(rot(string, rotation))
    
    line = input()

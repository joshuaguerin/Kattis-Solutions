# easy, geometry, circle, circumference

r = float(input()) / 2
w = float(input())
n = int(input())

c = 2 * 3.14159 * r

if c / w >= n:
    print("YES")
else:
    print("NO")

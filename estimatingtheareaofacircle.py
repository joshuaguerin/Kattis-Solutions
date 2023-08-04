from math import pi

r, m, c = input().split()
r = float(r)
m = float(m)
c = float(c)

while r != 0 and m != 0 and c != 0:
    # Compute the MC Pi estimate
    pi_est = 4 * (c/m)
    # Print the actual, estimated areas
    print(pi * r**2, pi_est * r**2)
    
    r, m, c = input().split()
    r = float(r)
    m = float(m)
    c = float(c)
    

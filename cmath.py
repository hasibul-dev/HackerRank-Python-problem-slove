import cmath

z = complex(input().strip())

r = abs(z)
phi = cmath.phase(z)

print(r)
print(phi)

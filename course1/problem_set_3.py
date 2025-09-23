from cmath import sin, cos, exp

z1 = 3 + 4j
z2 = complex(5, 12)
print(z1, z2)
print(z1.real, z2.imag)
print(z1.conjugate())
print(z1 + z2, z1 * z2, z1 / z2)
print(abs(z1), sin(z1), cos(z1), exp(z1))
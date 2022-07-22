from math import sqrt

entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

delta = pow(B, 2) - (4 * A * C)
R1 = None
R2 = None

if A == 0 or delta < 0:
    print('Impossivel calcular')
else:
    R1 = ((-1 * B) + sqrt(delta)) / (2 * A)
    R2 = ((-1 * B) - sqrt(delta)) / (2 * A)

    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')

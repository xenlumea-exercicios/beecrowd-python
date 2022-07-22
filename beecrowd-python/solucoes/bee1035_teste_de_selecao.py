entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])
D = float(entrada[3])

teste_maior = (B > C) and (D > A)  # B for maior do que C e se D for maior do que A
teste_soma = (C + D) > (A + B)  # e a soma de C com D for maior que a soma de A e B
teste_positivo = (C > 0) and (D > 0)  # C e D, ambos, forem positivos e
teste_par = (A % 2) == 0  # se a variável A for par escrever

if teste_maior and teste_soma and teste_positivo and teste_par:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

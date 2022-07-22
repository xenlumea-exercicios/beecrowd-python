entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])
D = float(entrada[3])

media = (A * 2 + B * 3 + C * 4 + D * 1) / (2 + 3 + 4 + 1)

print(f'Media: {media:.1f}')

if media >= 5 and media <= 6.9:

    print('Aluno em exame.')
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame}")
    media = (media + nota_exame) / 2

    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {media:.1f}')

elif media >= 7:
    print('Aluno aprovado.')
else:
    print('Aluno reprovado.')

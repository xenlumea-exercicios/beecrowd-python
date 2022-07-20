valor = int(input())

sobrou = valor

qtd_notas_de_100 = sobrou // 100
sobrou = sobrou % 100

qtd_notas_de_50 = sobrou // 50
sobrou = sobrou % 50

qtd_notas_de_20 = sobrou // 20
sobrou = sobrou % 20

qtd_notas_de_10 = sobrou // 10
sobrou = sobrou % 10

qtd_notas_de_5 = sobrou // 5
sobrou = sobrou % 5

qtd_notas_de_2 = sobrou // 2
sobrou = sobrou % 2

qtd_notas_de_1 = sobrou // 1

print(valor)
print(f'{qtd_notas_de_100} nota(s) de R$ 100,00')
print(f'{qtd_notas_de_50} nota(s) de R$ 50,00')
print(f'{qtd_notas_de_20} nota(s) de R$ 20,00')
print(f'{qtd_notas_de_10} nota(s) de R$ 10,00')
print(f'{qtd_notas_de_5} nota(s) de R$ 5,00')
print(f'{qtd_notas_de_2} nota(s) de R$ 2,00')
print(f'{qtd_notas_de_1} nota(s) de R$ 1,00')

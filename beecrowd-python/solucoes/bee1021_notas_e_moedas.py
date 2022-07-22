valor = float(input())

parte_inteira = valor // 1
parte_decimal = valor - parte_inteira

qtd_notas_de_100 = int(parte_inteira // 100)
parte_inteira = int(parte_inteira % 100)

qtd_notas_de_50 = int(parte_inteira // 50)
parte_inteira = int(parte_inteira % 50)

qtd_notas_de_20 = int(parte_inteira // 20)
parte_inteira = int(parte_inteira % 20)

qtd_notas_de_10 = int(parte_inteira // 10)
parte_inteira = int(parte_inteira % 10)

qtd_notas_de_5 = int(parte_inteira // 5)
parte_inteira = int(parte_inteira % 5)

qtd_notas_de_2 = int(parte_inteira // 2)
parte_inteira = int(parte_inteira % 2)

qtd_moedas_de_1 = int(parte_inteira // 1)

parte_decimal = int(parte_decimal * 100)

qtd_moedas_de_50_cent = int(parte_decimal // 50)
parte_decimal = int(parte_decimal % 50)

qtd_moedas_de_25_cent = int(parte_decimal // 25)
parte_decimal = int(parte_decimal % 25)

qtd_moedas_de_10_cent = int(parte_decimal // 10)
parte_decimal = int(parte_decimal % 10)

qtd_moedas_de_5_cent = int(parte_decimal // 5)

qtd_moedas_de_1_cent = int(parte_decimal % 5)

print('NOTAS:')
print(f'{qtd_notas_de_100} nota(s) de R$ 100.00')
print(f'{qtd_notas_de_50} nota(s) de R$ 50.00')
print(f'{qtd_notas_de_20} nota(s) de R$ 20.00')
print(f'{qtd_notas_de_10} nota(s) de R$ 10.00')
print(f'{qtd_notas_de_5} nota(s) de R$ 5.00')
print(f'{qtd_notas_de_2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{qtd_moedas_de_1} moeda(s) de R$ 1.00')
print(f'{qtd_moedas_de_50_cent} moeda(s) de R$ 0.50')
print(f'{qtd_moedas_de_25_cent} moeda(s) de R$ 0.25')
print(f'{qtd_moedas_de_10_cent} moeda(s) de R$ 0.10')
print(f'{qtd_moedas_de_5_cent} moeda(s) de R$ 0.05')
print(f'{qtd_moedas_de_1_cent} moeda(s) de R$ 0.01')

nome_vendedor = str(input())
salario_fixo = float(input())
total_vendas = float(input())

comissao_vendas = total_vendas * (15 / 100)

total_a_receber = comissao_vendas + salario_fixo

print(f"TOTAL = R$ {total_a_receber:.2f}")

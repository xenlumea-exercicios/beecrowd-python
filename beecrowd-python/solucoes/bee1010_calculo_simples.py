input_peca1 = input().split()
input_peca2 = input().split()

codigo_peca1 = input_peca1[0]
qtd_peca1 = int(input_peca1[1])
valor_unitario_peca1 = float(input_peca1[2])

codigo_peca2 = input_peca2[0]
qtd_peca2 = int(input_peca2[1])
valor_unitario_peca2 = float(input_peca2[2])

total_peca1 = qtd_peca1 * valor_unitario_peca1
total_peca2 = qtd_peca2 * valor_unitario_peca2

valor_total = total_peca1 + total_peca2

print(f"VALOR A PAGAR: R$ {valor_total:.2f}")

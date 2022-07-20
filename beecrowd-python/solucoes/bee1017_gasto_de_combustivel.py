horas = int(input())
velocidade_media = float(input())

distancia = horas * velocidade_media
rendimento = 12  # 12 KM/L

litros_gastos = distancia / rendimento

print(f'{litros_gastos:.3f}')

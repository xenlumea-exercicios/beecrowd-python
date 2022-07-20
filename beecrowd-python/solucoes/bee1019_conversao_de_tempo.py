evento_em_segundos = int(input())

horas = evento_em_segundos // (60 * 60)
sobrou = evento_em_segundos % (60 * 60)

minutos = sobrou // 60
segundos = sobrou % 60

print(f'{horas}:{minutos}:{segundos}')

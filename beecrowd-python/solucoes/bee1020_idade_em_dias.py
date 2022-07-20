idade_em_dias = int(input())

anos = idade_em_dias // 365
sobrou = idade_em_dias % 365

meses = sobrou // 30
dias = sobrou % 30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')

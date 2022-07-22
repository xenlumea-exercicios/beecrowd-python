entrada = float(input())

intervalo = None

if entrada >= 0 and entrada <= 25:
    intervalo = 'Intervalo [0,25]'
elif entrada > 25 and entrada <= 50:
    intervalo = 'Intervalo (25,50]'
elif entrada > 50 and entrada <= 75:
    intervalo = 'Intervalo (50,75]'
elif entrada > 75 and entrada <= 100:
    intervalo = 'Intervalo (75,100]'
else:
    intervalo = 'Fora de intervalo'
print(f'{intervalo}')

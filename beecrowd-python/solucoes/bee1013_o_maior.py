valores = input().split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

MaiorAB = (a + b + abs(a - b)) / 2
MaiorABC = 0

if c < MaiorAB:
    MaiorABC = int(MaiorAB)
else:
    MaiorABC = int(c)

print(f'{MaiorABC} eh o maior')

def dividendo(a, b):
    x = a
    r = 1
    for i in range(a, 0, -1):
        i += b - x
        r = r * i
    return r

def divisor(a):
    for i in range(a-1, 1, -1):
        a = a * i
    return a

total = 20
resultados = 1
combinaciones = int(dividendo(resultados, total) / divisor(resultados))

print(combinaciones)
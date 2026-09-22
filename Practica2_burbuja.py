calificaciones = [8.5, 9.2, 7.0, 10.0, 6.5, 8.8, 9.5, 7.8, 6.0, 9.0, 8.2, 7.3, 8.9, 9.7, 6.8]
ascendente = calificaciones.copy()
n = len(ascendente)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if ascendente[j] > ascendente[j + 1]:
            ascendente[j], ascendente[j + 1] = ascendente[j + 1], ascendente[j]
            swapped = True
    if not swapped:
        break

print("Orden Ascendente:", ascendente)
descendente = calificaciones.copy()
n = len(descendente)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if descendente[j] < descendente[j + 1]:
            descendente[j], descendente[j + 1] = descendente[j + 1], descendente[j]
            swapped = True
    if not swapped:
        break

print("Orden Descendente:", descendente)
stevila = [5, 2, 8, 3]

# Izpis vseh števil
print(stevila)

stevila.sort()
print("Števila smo uredili.")

# Izpis urejenih števil
print(stevila)

# Izpis števila na mestu 1
print(stevila[1])

# Izpis števila vseh elementov
print("Število vseh elementov je " + str(len(stevila)))

stevila.append(7)
stevila.remove(3)
del stevila[0]

print("Spremenjen seznam:")
print(stevila)

print("Vsi elementi prek for zanke")
for stevilo in stevila:
    print("Sedaj je stevilo enako " + str(stevilo))

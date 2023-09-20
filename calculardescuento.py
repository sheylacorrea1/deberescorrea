def calcular_descuento(precio, descuento=.10):
    valor_descuento = precio * descuento
    precio_total=precio-valor_descuento
    return precio_total

total = calcular_descuento(90)
print(f"El precio total es de ${total}")


total = calcular_descuento(200, 0.20)
print(f"El precio total es de ${total}")

p = float(input('Precio del producto:'))
np = p * 5/100
r = p - np
print('Descuento aplicado {:.2f}'.format(np))
print('El precio del producto con 5% de descuento es {:.2f}'.format(r))
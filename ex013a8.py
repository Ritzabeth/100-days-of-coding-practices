salário = float(input('Escriba su salario actual: '))
salário_aumento= salário*15/100
nuevo_salário= salário+salário_aumento
print('Su salário aumentó 15%, lo que representa {:.2f} de aumento. Su nuevo salário será {:.2f}'.format(salário_aumento,nuevo_salário))

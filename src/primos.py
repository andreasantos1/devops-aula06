
centesimo = 100
qtd_primos = 2
numero = 3
primos = '2,'

while qtd_primos < centesimo:
    eh_primo = 1
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = 0
            break
    if eh_primo:
        primos = primos + str(numero) + ','
        qtd_primos += 1
        if qtd_primos % 10 == 0:
            primos = primos + ' -> ' + str(qtd_primos) + ' números primos' + '\n'
    numero += 1
print(primos)

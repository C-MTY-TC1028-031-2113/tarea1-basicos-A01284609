def main():
    precio = 13
    interes = 0.075
    saldoanterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = float(input("Dame el número de cheques: "))
    sf1 = float((saldoanterior + ingresos - egresos) - (precio * cheques))
    sf2 = sf1 - (sf1*interes)
    print("El saldo final de la cuenta es: " + str(sf2))

if __name__ == '__main__':
    main()

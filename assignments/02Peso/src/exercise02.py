def main():
    Pi = float(input("Dame el peso inicial: "))
    Pf = float(input("Dame el peso final: "))
    Mes = int(input("Dame la cantidad de meses: "))
    bajar = float((Pi-Pf)/Mes)
    print("Lo que debes bajar por mes es: " + str(bajar))
    



if __name__ == '__main__':
    main()

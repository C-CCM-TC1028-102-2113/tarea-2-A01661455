def main():
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    indi=peso/altura**2
    if indi<20:
        print("PESO BAJO")
    elif 20<=indi<25:
        print("NORMAL")
    elif 25<=indi<30:
        print("SOBREPESO")
    elif 30<=indi<40:
        print("OBESIDAD")
    else:
        print("OBESIDAD MORBIDA")
if __name__ == '__main__':
    main()

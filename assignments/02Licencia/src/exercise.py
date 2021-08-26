
def main():
    edad=int(input("Ingresa tu edad: "))
    if edad>=18:
        id=input("¿Tienes identificación oficial? (s/n)")
        if "s" in id:
            print("Trámite de licencia concedido")
        elif "n" in id:
             print("No cumples requisitos")
        else:
         print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")
    #Escribe tu código debajo de esta línea

    pass


if __name__ == '__main__':
    main()

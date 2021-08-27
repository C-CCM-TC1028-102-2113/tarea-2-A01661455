def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x<y and x<z:
        print(x) 
    elif x<y and x>z:
        print(z)
    else:
        print(y)
    
    if y<x and y<z:
        print(y) 
    elif y<x and y>z:
        print(z)
    else:
        print(x)

    if z<y and z<x:
        print(z) 
    elif z<x and z>y:
        print(y)
    else:
        print(x)
        
if __name__ == '__main__':
    main()

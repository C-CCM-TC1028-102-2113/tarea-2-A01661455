def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x<y and x<z and y<z:
        print(x,y,z) 

    elif y<x and y<z and x>z:
        print(y,z,x) 
    
    elif z<y and z<x and y>x:
        print(z,x,y) 
    
if __name__ == '__main__':
    main()


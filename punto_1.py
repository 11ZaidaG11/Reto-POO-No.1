def operation(num_a:int, num_b:int, sign:str):
    match sign:
        case "+": # Suma
            num_a + num_b
        case "-": # Resta
            num_a - num_b
        case "*": # Multiplicacion
            num_a * num_b
        case "/": # Division
            num_a / num_b
        case _:
            "Opción no disponible"

    
if __name__ == "__main__":
    num_a = int(input("Ingrese un numero: "))
    num_b = int(input("Ingrese otro numero: "))
    print("Ingrese:\n + para suma\n" \
    "- para resta\n" \
    "* para multiplicación\n" \
    "/ para división\n")
    sign = str(input)
    result = operation(num_a, num_b, sign)
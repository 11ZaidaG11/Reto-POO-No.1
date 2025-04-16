"""
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, 
según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado 
para la operación. entrada: (1,2,"+"), salida (3).

"""
def operation():
    match user:
        case "+": # Suma
        case "-": # Resta
        case "*": # Multiplicacion
        case "/": # Division
        case _:

    
if __name__ == "__main__":
    user = int(input("Ingrese 2 numeros separados por coma"))
    result = operation()
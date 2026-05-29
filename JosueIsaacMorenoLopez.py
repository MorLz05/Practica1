def sumar_tres_numeros(a, b, c):
    """
    Función que suma tres números
    
    Parámetros:
    a, b, c: números a sumar
    
    Retorna:
    La suma de los tres números
    """
    return a + b + c

# Ejemplo de uso
print("=== SUMADORA DE 3 NÚMEROS ===")

# Solicitar los números
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Tercer número: "))

# Calcular usando la función
resultado = sumar_tres_numeros(num1, num2, num3)

# Mostrar resultado
print(f"\nResultado: {num1} + {num2} + {num3} = {resultado}")
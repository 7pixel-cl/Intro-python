def calcular_utilidades(precio, usuarios, gastos):
    """
    Calcula las utilidades de un proyecto.

    Args:
        precio (float): Precio de suscripción.
        usuarios (int): Número de usuarios.
        gastos (float): Gastos totales.

    Returns:
        float: Las utilidades calculadas.
    """
    return precio * usuarios - gastos

def main():
    # Solicitar datos al usuario
    precio = float(input("Ingrese el precio de suscripción: "))
    usuarios = int(input("Ingrese el número de usuarios: "))
    gastos = float(input("Ingrese los gastos totales: "))

    # Calcular utilidades
    utilidades = calcular_utilidades(precio, usuarios, gastos)

    # Mostrar el resultado
    print(f"Las utilidades del proyecto son: {utilidades:.2f}")

if __name__ == "__main__":
    main()
def calcular_utilidades_doble(precio, usuarios_normales, usuarios_premium, gastos):
    """
    Calcula las utilidades considerando usuarios normales y premium.

    Args:
        precio (float): Precio de suscripción para usuarios normales.
        usuarios_normales (int): Número de usuarios normales.
        usuarios_premium (int): Número de usuarios premium.
        gastos (float): Gastos totales.

    Returns:
        float: Las utilidades calculadas.
    """
    # Precio para usuarios premium es un 50% mayor
    precio_premium = precio * 1.5
    return (precio * usuarios_normales + precio_premium * usuarios_premium) - gastos

def main():
    # Solicitar datos al usuario
    precio = float(input("Ingrese el precio de suscripción para usuarios normales: "))
    usuarios_normales = int(input("Ingrese el número de usuarios normales: "))
    usuarios_premium = int(input("Ingrese el número de usuarios premium: "))
    gastos = float(input("Ingrese los gastos totales: "))

    # Calcular utilidades
    utilidades = calcular_utilidades_doble(precio, usuarios_normales, usuarios_premium, gastos)

    # Mostrar el resultado
    print(f"Las utilidades del proyecto son: {utilidades:.2f}")

if __name__ == "__main__":
    main()

def calcular_razon_utilidades(precio, usuarios, gastos, utilidades_anterior):
    """
    Calcula la razón entre las utilidades actuales y las del año anterior.

    Args:
        precio (float): Precio de suscripción.
        usuarios (int): Número de usuarios.
        gastos (float): Gastos totales.
        utilidades_anterior (float): Utilidades del año anterior.

    Returns:
        float: Razón entre las utilidades actuales y las del año anterior.
    """
    utilidades_actual = precio * usuarios - gastos
    return utilidades_actual / utilidades_anterior

def main():
    # Solicitar datos al usuario
    precio = float(input("Ingrese el precio de suscripción: "))
    usuarios = int(input("Ingrese el número de usuarios: "))
    gastos = float(input("Ingrese los gastos totales: "))
    utilidades_anterior = float(input("Ingrese las utilidades del año anterior: "))

    # Calcular razón de utilidades
    razon = calcular_razon_utilidades(precio, usuarios, gastos, utilidades_anterior)

    # Mostrar el resultado
    print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.2f}")

if __name__ == "__main__":
    main()

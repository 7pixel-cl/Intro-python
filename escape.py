import math

def calcular_velocidad_escape(g, r):
    """
    Calcula la velocidad de escape.

    Args:
        g (float): La constante gravitacional en [m/s^2].
        r (float): El radio en kilómetros.

    Returns:
        float: La velocidad de escape en [m/s].
    """
    # Convertir el radio de kilómetros a metros
    r_metros = r * 1000
    # Calcular la velocidad de escape
    v_escape = math.sqrt(2 * g * r_metros)
    return v_escape

def main():
    """
    Función principal que solicita los valores al usuario, calcula la velocidad de escape y muestra el resultado.
    """
    # Solicitar los valores al usuario
    radio = float(input("Ingrese el radio en kilómetros: "))
    g = float(input("Ingrese la constante gravitacional g en [m/s^2]: "))
    
    # Calcular la velocidad de escape
    velocidad_escape = calcular_velocidad_escape(g, radio)
    
    # Mostrar el resultado
    print(f"La velocidad de escape es {velocidad_escape:.1f} [m/s]")

if __name__ == "__main__":
    main()
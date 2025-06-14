# evaluaciones.py

# Traemos nuestra clase Pizza desde el archivo pizza.py.
# ¡Aquí es donde usaremos nuestra "máquina" de hacer pizzas!
from pizza import Pizza

# --- Requerimiento 5a ---
# ¡Vamos a imprimir los atributos de clase sin siquiera crear una pizza todavía!
# Estos son como los ajustes predeterminados para TODAS las pizzas.
print("--- Atributos de Clase de Pizza ---")
print(f"Precio de todas las pizzas: ${Pizza.precio}")
print(f"Tamaño de todas las pizzas: {Pizza.tamano}")
print("-" * 30)

# --- Requerimiento 5b ---
# Ahora, usemos ese increíble método estático 'validar_elemento' para verificar algo.
# No necesitamos un objeto pizza para hacer esto, ¡súper conveniente!
print("\n--- Validación de Elemento (sin instancia) ---")
elemento_a_validar = "salsa de tomate"
lista_ejemplo = ["salsa de tomate", "salsa bbq"]
print(f"¿'{elemento_a_validar}' está en {lista_ejemplo}? {Pizza.validar_elemento(elemento_a_validar, lista_ejemplo)}")
print("-" * 30)

# --- Menú Principal con opción de salir ---
print("\n¡Bienvenido al sistema de pedidos de Pizza!")
while True:
    print("\n--- Menú Principal ---")
    print("1. Ordenar una Pizza")
    print("2. Salir del Programa")

    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == '1':
        # --- Requerimiento 5c & 5d ---
        # Time to create our very own pizza instance!
        print("\n--- Creando una Instancia de Pizza y Haciendo un Pedido ---")
        mi_pizza = Pizza()
        mi_pizza.hacer_pedido() # Esto le pedirá información al usuario.

        # After the user has entered their choices, let's see what they picked and if it's a valid pizza.
        print("\n--- Detalles de tu Pizza ---")
        print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
        print(f"Ingredientes vegetales: {mi_pizza.ingredientes_vegetales[0]}, {mi_pizza.ingredientes_vegetales[1]}")
        print(f"Tipo de masa: {mi_pizza.tipo_masa}")
        print(f"¿Es tu pizza válida? {mi_pizza.valida}")
        print("-" * 30)

    elif opcion == '2':
        print("\nSaliendo del programa. ¡Hasta pronto!")
        break # Esto rompe el bucle while y termina el programa.
    else:
        print("Opción no válida. Por favor, selecciona 1 o 2.")

# --- Requerimiento 5e (Se ejecutará una vez que el bucle principal haya terminado, si no se salió antes) ---
# Esta parte está diseñada para mostrar un error, como se esperaba en el desafío original.
# Se ejecutará *después* de que el usuario elija salir o de que se complete una orden.
# Es importante notar que si el usuario ordena y luego el programa termina, este error aparecerá al final.
# Si el usuario sale directamente sin ordenar, este error también aparecerá al final.
print("\n--- Intentando acceder a 'valida' como atributo de clase (esperamos un error) ---")
try:
    print(f"¿La clase Pizza es válida? {Pizza.valida}")
except AttributeError as e:
    print(f"¡Oops! Como esperábamos, se generó un error: {e}")
    print("Esto ocurre porque 'valida' es un atributo de *instancia*, no de clase.")
    print("Cada pizza individual tiene su propio estado de validez, no la clase en general.")
print("-" * 30)

print("\n¡Desafío completado! ¡Espero que disfrutes tu pizza (o al menos el código de tu pizza)! 😊")
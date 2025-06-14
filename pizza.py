
from ingredientes import vegetales, proteicos, masas

class Pizza:
    # Atributos de clase 
    # Cada pizza que hagamos tendrá este precio y tamaño por defecto
    precio = 10000
    tamano = "familiar"

    # Este atributo nos dirá si una pizza en particular es válida o no.
    # Lo ponemos en 'False' por defecto y lo cambiaremos si la pizza cumple con los requisitos.
    valida = False

    def __init__(self):
        # Atributos de instancia (estos son únicos para cada pizza que crees)
        self.ingrediente_proteico = None
        self.ingredientes_vegetales = []
        self.tipo_masa = None

    # ¡Este es un método estático! Es como una función de utilidad para nuestra clase Pizza.
    # Podemos usarlo sin necesidad de crear un objeto pizza primero.
    @staticmethod
    def validar_elemento(elemento, lista_posibles):
        # Estamos verificando si el 'elemento' (como un ingrediente) está en nuestra 'lista_posibles'.
        # Es una verificación simple para asegurarnos de que elijas algo que realmente tenemos.
        return elemento in lista_posibles

    # ¡Este método es para que puedas hacer tu pedido de pizza!
    # Te pedirá tus elecciones y luego verificará si son válidas.
    def hacer_pedido(self):
        # Vamos a pedir el ingrediente proteico y asegurar que sea válido.
        # Repetiremos hasta que el usuario ingrese una opción correcta.
        while True:
            self.ingrediente_proteico = input("Ingresa el ingrediente proteico (pollo, vacuno, carne vegetal): ").lower()
            if Pizza.validar_elemento(self.ingrediente_proteico, proteicos):
                break # Si es válido, salimos del bucle.
            else:
                print("¡Error! Ingrediente proteico no válido. Por favor, intenta de nuevo.")

        # Ahora pediremos el primer ingrediente vegetal y lo validaremos.
        while True:
            vegetal1 = input("Ingresa el primer ingrediente vegetal (tomate, aceitunas, champiñones): ").lower()
            if Pizza.validar_elemento(vegetal1, vegetales):
                self.ingredientes_vegetales.append(vegetal1)
                break # Si es válido, salimos del bucle.
            else:
                print("¡Error! Ingrediente vegetal no válido. Por favor, intenta de nuevo.")

        # Y ahora el segundo ingrediente vegetal, también con validación.
        while True:
            vegetal2 = input("Ingresa el segundo ingrediente vegetal (tomate, aceitunas, champiñones): ").lower()
            if Pizza.validar_elemento(vegetal2, vegetales):
                self.ingredientes_vegetales.append(vegetal2)
                break # Si es válido, salimos del bucle.
            else:
                print("¡Error! Ingrediente vegetal no válido. Por favor, intenta de nuevo.")

        # Finalmente, la masa, con su respectiva validación.
        while True:
            self.tipo_masa = input("Ingresa el tipo de masa (tradicional, delgada): ").lower()
            if Pizza.validar_elemento(self.tipo_masa, masas):
                break # Si es válido, salimos del bucle.
            else:
                print("¡Error! Tipo de masa no válido. Por favor, intenta de nuevo.")

        # Una vez que todos los inputs son válidos, la pizza es válida.
        # No necesitamos el bloque 'if/else' grande de antes porque los bucles ya aseguraron la validez.
        self.valida = True 
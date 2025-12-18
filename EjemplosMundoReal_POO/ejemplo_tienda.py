# Ejemplo básico de Programación Orientada a Objetos
# Caso del mundo real: una tienda sencilla


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def comprar(self, producto):
        print(self.nombre, "compró", producto.nombre)
        print("Precio:", producto.precio)


# Creación de objetos
producto1 = Producto("Cuaderno", 2.50)
cliente1 = Cliente("Andrés")

# Interacción entre objetos
cliente1.comprar(producto1)

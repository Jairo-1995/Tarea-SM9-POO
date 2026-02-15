# servicios/inventario.py
from modelos.producto import Producto

class Inventario:
    def __init__(self):
        self._productos = []  # Lista para almacenar productos

    def añadir_producto(self, id, nombre, cantidad, precio):
        # Validar que el ID no esté repetido
        for producto in self._productos:
            if producto.get_id() == id:
                print(f"Error: Ya existe un producto con ID {id}.")
                return False
        # Crear y añadir el producto
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self._productos.append(nuevo_producto)
        print(f"Producto '{nombre}' añadido exitosamente.")
        return True

    def eliminar_producto(self, id):
        for producto in self._productos:
            if producto.get_id() == id:
                self._productos.remove(producto)
                print(f"Producto con ID {id} eliminado.")
                return True
        print(f"Error: No se encontró un producto con ID {id}.")
        return False

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        for producto in self._productos:
            if producto.get_id() == id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print(f"Producto con ID {id} actualizado.")
                return True
        print(f"Error: No se encontró un producto con ID {id}.")
        return False

    def buscar_productos(self, nombre_parcial):
        resultados = []
        for producto in self._productos:
            if nombre_parcial.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        if resultados:
            print("Producto encontrado:")
            for prod in resultados:
                print(prod)
        else:
            print(f"No se encontraron productos con '{nombre_parcial}' en el nombre.")
        return resultados

    def mostrar_inventario(self):
        if not self._productos:
            print("---El inventario está vacío.---")
        else:
            print("---Inventario completo de productos Amazónicos---")
            for producto in self._productos:
                print(producto)


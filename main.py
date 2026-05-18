import funciones_supermercado
#sistema de Gestión de Productos de Supermercado
#Una cadena de supermercados necesita desarrollar un sistema básico en Python para
#administrar productos y controlar el inventario de una sucursal. El programa deberá ejecutarse
#completamente por consola y permitir registrar productos, realizar consultas, ordenar
#información y efectuar cálculos básicos relacionados con el stock y el valor del inventario

#Requerimientos del sistema
#El programa deberá permitir almacenar la siguiente información de cada producto:
#• Código del producto
#• Nombre del producto
#• Precio
#• Cantidad en stock

#1) Cargar producto
#Solicitar código, nombre, precio y stock. Validar código no repetido, precio mayor a cero y
#stock no negativo.
#2) Mostrar productos
#Mostrar todos los productos cargados de forma clara y ordenada.
#3) Buscar producto por código
#Buscar manualmente recorriendo la estructura de datos utilizada.
#4) Ordenar productos por precio
#Ordenar manualmente utilizando un algoritmo de ordenamiento.
#5) Mostrar producto con menor stock
#Determinar manualmente cuál es el producto con menor cantidad disponible.
#6) Calcular valor total del inventario
#Calcular el valor total del inventario considerando precio por stock.





print("supermecado pyhon MARKET")

#El programa deberá permitir almacenar la siguiente información de cada producto:
#• Código del producto
#• Nombre del producto
#• Precio
#• Cantidad en stock
codigo = []
nombre = []
precio = []
cantidad_stock = []
while True:
    print("1-cargar productos")
    print("2-mostrar productos")
    print("3-buscar producto por codigo")
    print("4-ordenar producto por precio")
    print("5-mostrar producto con menor stock")
    print("6-calcular valor total del inventario")
    print("7-salir")
    opcion = int(input("ingrese una opcion : "))
    
    match opcion: 
        case 1:
            funciones_supermercado.cargar_productos(codigo,nombre,precio,cantidad_stock)
        case 2 :
            funciones_supermercado.mostrar_productos(codigo,nombre,precio,cantidad_stock)
        case 3 :
            funciones_supermercado.buscar_producto(codigo,nombre,precio,cantidad_stock)
        case 4:
            funciones_supermercado.ordernar_productos(codigo,nombre,precio,cantidad_stock)
        case 5:
            funciones_supermercado.ordenar_stock(codigo,nombre,precio,cantidad_stock)
        case 6:
            funciones_supermercado.calcula_valor_total(codigo,nombre,precio,cantidad_stock)
        case 7:
            print("[RESULTADO ESPERADO]")
            print("Saliendo del sistema...")
            break
        case _:
            print("Opcion invalida. Intente nuevamente.")
        
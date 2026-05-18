#El programa deberá permitir almacenar la siguiente información de cada producto:
#• Código del producto
#• Nombre del producto
#• Precio
#• Cantidad en stock
#1) Cargar producto
#Solicitar código, nombre, precio y stock. Validar código no repetido, precio mayor a cero y
#stock no negativo.
def cargar_productos(codigos :list , nombres:list ,precios:list , cantidad_stocks:list):
    while True:
        
        codigo = int(input("ingrese el codigo del producto: "))
        repetido = False
        for i in range(len(codigos)):
            if codigos[i] == codigo:
                repetido = True
                break
        if repetido == False:
            print("el codigo esta repetido")
        else: 
            break
        codigos.append(codigo)

    nombre = input("ingrese el nombre del producto: ")
    nombres.append(nombre)
    
    while True:
        
        precio = int(input("ingrese el precio del producto: "))
        if precio > 0:
            break
        else:
            print("el precio debe ser mayo a cero")
    precios.append(precio)
    
    
    while True:
        cantidad_stock = int(input("ingrese la cantidad de stock del producto: "))
        if cantidad_stock >= 0 :
            break
        else:
            print("el stock no puede ser negativo")
    cantidad_stocks.append(cantidad_stock)
    
#2) Mostrar productos
#Mostrar todos los productos cargados de forma clara y ordenada
def mostrar_productos(codigos :list , nombres:list ,precios:list , cantidad_stocks:list):

    if len(codigos) == 0:
        print("no hay ningun producto cargado")
    else:
        for i in range(len(codigos)):
            print("")
            print(codigos[i])
            print(nombres[i])
            print(precios[i])
            print(cantidad_stocks[i])

#3) Buscar producto por código
#Buscar manualmente recorriendo la estructura de datos utilizada.
            
def buscar_producto(codigos :list , nombres:list ,precios:list , cantidad_stocks:list):
    if len(codigos) == 0:
        print("no hay productos con este codigo")
    else:
        buscado_producto = int(input("ingrese el codigo del producto a buscar"))
        producto_encontrado = False
        for i in range(len(codigos)):
            if codigos[i] == buscado_producto:
                print("producto encontrado")
                print(codigos[i])
                print(nombres[i])
                print(precios[i])
                print(cantidad_stocks[i])
                producto_encontrado = True
                break
        if producto_encontrado == False:
            print("ese producto no se encuentra")
    

#5) Mostrar producto con menor stock


def ordenar_stock(codigos :list , nombres:list ,precios:list , cantidad_stocks:list):
    if len(codigos) == 0 :
        print("no hay porductos registrados")
    else:
        menor =cantidad_stocks[0]
        posicion_menor = 0
        for i in range(1,len(cantidad_stocks)):
            if cantidad_stocks[i] < menor:
                menor =  cantidad_stocks[i]
                posicion_menor = 1
                
                print("producto de menor stock")
                print(f"{nombres[posicion_menor]} -> {cantidad_stocks[posicion_menor]}")

#6) Calcular valor total del inventario
#Calcular el valor total del inventario considerando precio por stock.


def calcula_valor_total(codigos :list , nombres:list ,precios:list , cantidad_stocks:list):
    if len(codigos) == 0:
        print("no hay ningun producto cargado")
    else:
        valor_total = 0
        for i in range(len(codigos)):
            subtotal = precios[i] * cantidad_stocks[i]
            print(f"{precios[i]} * {cantidad_stocks[i]}")
            valor_total = valor_total + (precios[i] * cantidad_stocks[i])
        print(valor_total)
            

#4) Ordenar productos por precio
#Ordenar manualmente utilizando un algoritmo de ordenamiento.
def ordernar_productos(codigos :list , nombres:list ,precios:list , cantidad_stocks:list):
    if len(codigos) == 0:
        print("no hay ningun producto para ordenar")
    else:
        largo = len(precios)
        for i in range(largo - 1):
            for j in range(largo - 1 -i):
                if precios[i] > precios[j+1]:
                    precio_proctos = precios[i]
                    precios[j] = precios[j+1]
                    precios[j+1] = precio_proctos

                    precio_codigo = codigos[i]
                    codigos[j] = codigos[j+1]
                    codigos[j+1] = precio_codigo

                    precio_nombre = nombres[i]
                    nombres[j] = nombres[j+1]
                    nombres[j+1] = precio_nombre 
                    
                    precio_stock = cantidad_stocks[i]
                    cantidad_stocks[j] =cantidad_stocks[j+1]
                    cantidad_stocks[j+1] = precio_stock
                    
                    



    
categorias = ("alimentos", "aseo", "tecnologia", "ropa")
inventario = []
categorias_con_stock = set()

def registrar_producto():
    codigo = input('codigo del producto: ')
    nombre = input("nombre del producto: ")
    producto = {
      "codigo":codigo,
        "nombre": nombre,
        "categoria":categoria,
      "precio": precio,
        "stock":stock
    }

    inventario.append(producto)
    categorias_con_stock.add(categoria)
    print("producto guardado")


def buscar_producto():
  codigo = input("codigo del producto: ")
  for p in inventario:
      if p["codigo"]==codigo:
          print(p)

def listar_por_categoria():
    categoria = input('categoria: ')
    for p in inventario:
            if p["categoria"] == categoria:
                print(p)

def ver_categorias():
    print(categorias_con_stock)

def alertas_stock():
    for p in inventario:
      if p["stock"] < 5:
        print("stock bajo:", p["nombre"], p['stock'])


def valor_total():
    total = 0
    for p in inventario:
        total = total + p["precio"]*p["stock"]
    print('valor total:', total)


def menu():
    while True:
        print("1 registrar")
        print("2 buscar")
        print('3 listar por categoria')
        print("4 ver categorias con stock")
        print("5 alertas de stock")
        print("6 valor total")
        print("0 salir")

        opcion = input("opcion: ")

        match opcion:
            case "1":
                registrar_producto()
            case "2":
              buscar_producto()
            case "3":
                listar_por_categoria()
            case "4":
                ver_categorias()
            case "5":
              alertas_stock()
            case "6":
                valor_total()
            case "0":
                break

menu()
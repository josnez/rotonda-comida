from main                             import app, db
from models.especialidad              import Especialidad
from models.restaurante               import Restaurante
from models.menu                      import Menu
from models.categoria                 import Categoria
from models.producto                  import Producto
from models.producto_menu             import Producto_Menu
from models.ingrediente               import Ingrediente
from models.producto_menu_ingrediente import Producto_Ingrediente
from models.cliente                   import Cliente
from models.carro_compra              import Carro_Compra
from models.pedido                    import Pedido
from models.menu_pedido               import Menu_Pedido

app.app_context().push()
db.create_all()

# creacion de especialidades
especialidad1 = Especialidad("Jugos")
especialidad2 = Especialidad("Postres")
db.session.add_all([especialidad1, especialidad2])
db.session.commit()

# creacion de restaurantes
restaurante1  = Restaurante("Las delicias", especialidad1.cod_especialidad)
restaurante2  = Restaurante("Las empanadas", especialidad2.cod_especialidad)
db.session.add_all([restaurante1, restaurante2])
db.session.commit()

# creacion de categorias
entradas        = Categoria("Entradas")
platos_fuertes  = Categoria("Platos Fuertes")
postres         = Categoria("Postres")
bebidas         = Categoria("Bebidas")
acompanamientos = Categoria("Acompañamientos")
db.session.add_all([entradas, platos_fuertes, postres, bebidas, acompanamientos])
db.session.commit()

# creacion de menus
menu1 = Menu("Barato", 10000, restaurante1.cod_restaurante) # Menu 1 restaurante 1
menu2 = Menu("Medio", 15000, restaurante1.cod_restaurante) # Menu 2 restaurante 1
menu3 = Menu("Barato", 15000, restaurante2.cod_restaurante) # Menu 1 restaurante 2
menu4 = Menu("Medio", 20000, restaurante2.cod_restaurante) # Menu 2 restaurante 2
db.session.add_all([menu1, menu2, menu3, menu4])
db.session.commit()

# creacion de productos
vino_tinto       = Producto("Vino tinto", 10000, entradas.cod_categoria)
limonada         = Producto("Limonada", 5000, bebidas.cod_categoria)
jugo_leche       = Producto("Jugo en leche", 7000, bebidas.cod_categoria)
arroz_huevo      = Producto("Arroz con huevo", 15000, platos_fuertes.cod_categoria)
bandeja_paisa    = Producto("Bandeja Paisa", 30000, platos_fuertes.cod_categoria)
helado_chocolate = Producto("Helado de chocolate", 20000, postres.cod_categoria)
te_helado        = Producto("Helado de chocolate", 18000, postres.cod_categoria)
db.session.add_all([vino_tinto, limonada, jugo_leche, arroz_huevo, bandeja_paisa, helado_chocolate, te_helado])
db.session.commit()

# creacion de producto_menu
producto_menu1 = Producto_Menu(limonada.cod_producto, menu1.cod_menu)
producto_menu2 = Producto_Menu(arroz_huevo.cod_producto, menu1.cod_menu)
producto_menu3 = Producto_Menu(te_helado.cod_producto, menu1.cod_menu)

producto_menu4 = Producto_Menu(vino_tinto.cod_producto, menu4.cod_menu)
producto_menu5 = Producto_Menu(jugo_leche.cod_producto, menu4.cod_menu)
producto_menu6 = Producto_Menu(bandeja_paisa.cod_producto, menu4.cod_menu)
producto_menu7 = Producto_Menu(helado_chocolate.cod_producto, menu4.cod_menu)

producto_menu8 = Producto_Menu(jugo_leche.cod_producto, menu3.cod_menu)
producto_menu9 = Producto_Menu(arroz_huevo.cod_producto, menu3.cod_menu)
producto_menu10 = Producto_Menu(te_helado.cod_producto, menu3.cod_menu)
db.session.add_all([producto_menu1, producto_menu2, producto_menu3, producto_menu4, producto_menu5, 
                    producto_menu6, producto_menu7, producto_menu8, producto_menu9, producto_menu10])
db.session.commit()

# creacion de ingredientes
ingrediente1 = Ingrediente("Anillos de cebolla")
ingrediente2 = Ingrediente("Queso")
ingrediente3 = Ingrediente("Papas a la francesa")
ingrediente4 = Ingrediente("Platano")
ingrediente5 = Ingrediente("Jamon")
db.session.add_all([ingrediente1, ingrediente2, ingrediente3, ingrediente4, ingrediente5])
db.session.commit()

# asignacion de ingredientes a productos
prod_ingre1 = Producto_Ingrediente(producto_menu2.cod_producto_menu, ingrediente1.cod_ingrediente)
prod_ingre2 = Producto_Ingrediente(producto_menu2.cod_producto_menu, ingrediente4.cod_ingrediente)

prod_ingre3 = Producto_Ingrediente(producto_menu6.cod_producto_menu, ingrediente3.cod_ingrediente)
prod_ingre4 = Producto_Ingrediente(producto_menu6.cod_producto_menu, ingrediente4.cod_ingrediente)
prod_ingre5 = Producto_Ingrediente(producto_menu6.cod_producto_menu, ingrediente5.cod_ingrediente)
db.session.add_all([prod_ingre1, prod_ingre2, prod_ingre3, prod_ingre4, prod_ingre5])
db.session.commit()

# creacion de clientes
cliente1 = Cliente("Andres", "Gonzales", "Calle 21 # 12 - 34")
cliente2 = Cliente("Maria", "Jimenez", "Calle 34 # 18 - 32")
cliente3 = Cliente("Patricia", "Nieto", "Calle 107 # 34 - 16")
db.session.add_all([cliente1, cliente2, cliente3])
db.session.commit()

# creacion de carritos de compra
carrito1 = Carro_Compra(50000, cliente1.cod_cliente)
carrito2 = Carro_Compra(60000, cliente2.cod_cliente)
carrito3 = Carro_Compra(70000, cliente3.cod_cliente)
db.session.add_all([carrito1, carrito2, carrito3])
db.session.commit()

# creacion de pedidos
pedido1 = Pedido(50000, carrito1.cod_carro_compra)
pedido2 = Pedido(60000, carrito2.cod_carro_compra)
pedido3 = Pedido(70000, carrito3.cod_carro_compra)
db.session.add_all([pedido1, pedido2, pedido3])
db.session.commit()

# asignacion de menus a pedidos
menu_pedido1 = Menu_Pedido(menu1.cod_menu, pedido1.cod_pedido)
menu_pedido2 = Menu_Pedido(menu3.cod_menu, pedido2.cod_pedido)
menu_pedido3 = Menu_Pedido(menu4.cod_menu, pedido3.cod_pedido)
db.session.add_all([menu_pedido1, menu_pedido2, menu_pedido3])
db.session.commit()
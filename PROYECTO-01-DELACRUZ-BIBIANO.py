from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import pandas as pd
import os
import matplotlib.pyplot as plt


sales = pd.DataFrame(lifestore_sales, 
                     columns=['id_sale', 'id_product', 'score', 'date', 'refund'])
product = pd.DataFrame(lifestore_products, 
                        columns=['id_product', 'name', 'price', 'category', 'stock'])
search = pd.DataFrame(lifestore_searches,
                      columns=['id_search', 'id_product'])

sales_product = pd.merge(sales, product, how="inner" , on='id_product')
search_product = pd.merge(search, product, how="inner", on='id_product')


dia_mes_año = sales_product["date"].str.split('/', expand=True)
dia_mes_año.columns = ['Día', 'Mes','Año']
col_mes = pd.concat([sales_product, dia_mes_año], axis=1)

sin_devolucion = col_mes["refund"] != 1
sin_devolucion = col_mes[sin_devolucion]

    
mayores_ventas = sin_devolucion.name.value_counts() 
mayores_ventas = mayores_ventas.sort_values(ascending=False)[:5] 
mayores_ventas = pd.DataFrame(mayores_ventas).reset_index()
mayores_ventas = mayores_ventas.rename(columns={"name":"Ventas", "index":"Producto"}) 


mayores_busquedas = search_product.name.value_counts() 
mayores_busquedas = mayores_busquedas.sort_values(ascending=False)[:10] 
mayores_busquedas = pd.DataFrame(mayores_busquedas).reset_index()
mayores_busquedas = mayores_busquedas.rename(columns={"index":"Producto", "name":"Busquedas"}) 


cat_procesadores = sin_devolucion[sin_devolucion.category == "procesadores"]
cat_procesadores = cat_procesadores.name.value_counts().sort_values(ascending=True)[:5]
cat_procesadores = pd.DataFrame(cat_procesadores).reset_index().rename(columns={"index":"Producto", "name":"Ventas"})
cat_discos_duros = sin_devolucion[sin_devolucion.category == "discos duros"]
cat_discos_duros = cat_discos_duros.name.value_counts().sort_values(ascending=True)[:5]
cat_discos_duros = pd.DataFrame(cat_discos_duros).reset_index().rename(columns={"index":"Producto", "name":"Ventas"})
cat_tarjetas_madre = sin_devolucion[sin_devolucion.category == "tarjetas madre"]
cat_tarjetas_madre = cat_tarjetas_madre.name.value_counts().sort_values(ascending=True)[:5]
cat_tarjetas_madre = pd.DataFrame(cat_tarjetas_madre).reset_index().rename(columns={"index":"Producto", "name":"Ventas"})
cat_tarjetas_video = sin_devolucion[sin_devolucion.category == "tarjetas de video"]
cat_tarjetas_video = cat_tarjetas_video.name.value_counts().sort_values(ascending=True)[:5]
cat_tarjetas_video = pd.DataFrame(cat_tarjetas_video).reset_index().rename(columns={"index":"Producto", "name":"Ventas"})
cat_audifonos = sin_devolucion[sin_devolucion.category == "audifonos"]
cat_audifonos = cat_audifonos.name.value_counts().sort_values(ascending=True)[:5]
cat_audifonos = pd.DataFrame(cat_audifonos).reset_index().rename(columns={"index":"Producto", "name":"Ventas"})


busquedas_procesadores = search_product[search_product.category == "procesadores"]
busquedas_procesadores = busquedas_procesadores.name.value_counts().sort_values(ascending=True)[:10]
busquedas_procesadores = pd.DataFrame(busquedas_procesadores).reset_index().rename(columns={"index":"Producto", "name":"Busquedas"})
busquedas_discos_duros = search_product[search_product.category == "discos duros"]
busquedas_discos_duros = busquedas_discos_duros.name.value_counts().sort_values(ascending=True)[:10]
busquedas_discos_duros = pd.DataFrame(busquedas_discos_duros).reset_index().rename(columns={"index":"Producto", "name":"Busquedas"})
busquedas_tarjetas_madre = search_product[search_product.category == "tarjetas madre"]
busquedas_tarjetas_madre = busquedas_tarjetas_madre.name.value_counts().sort_values(ascending=True)[:10]
busquedas_tarjetas_madre = pd.DataFrame(busquedas_tarjetas_madre).reset_index().rename(columns={"index":"Producto", "name":"Busquedas"})
busquedas_tarjetas_video = search_product[search_product.category == "tarjetas de video"]
busquedas_tarjetas_video = busquedas_tarjetas_video.name.value_counts().sort_values(ascending=True)[:10]
busquedas_tarjetas_video = pd.DataFrame(busquedas_tarjetas_video).reset_index().rename(columns={"index":"Producto", "name":"Busquedas"})
busquedas_audifonos = search_product[search_product.category == "audifonos"]
busquedas_audifonos = busquedas_audifonos.name.value_counts().sort_values(ascending=True)[:10]
busquedas_audifonos = pd.DataFrame(busquedas_audifonos).reset_index().rename(columns={"index":"Producto", "name":"Busquedas"})



mayores_resenas = sales_product.groupby("name")["score"].mean()
mayores_resenas = mayores_resenas.sort_values(ascending=False)
mayores_resenas = mayores_resenas[:5]
mayores_resenas = pd.DataFrame(mayores_resenas).reset_index()
mayores_resenas = mayores_resenas.rename(columns={"name":"Producto", "score":"Reseña Prom"})

menores_resenas = sales_product.groupby("name")["score"].mean()
menores_resenas = menores_resenas.sort_values(ascending=True)
menores_resenas = menores_resenas[:5]
menores_resenas = pd.DataFrame(menores_resenas).reset_index()
menores_resenas = menores_resenas.rename(columns={"name":"Producto", "score":"Reseña Prom"})
menores_resenas = menores_resenas.round(2)


media_mensual = sin_devolucion.groupby("Mes")["price"].mean()
media_mensual = pd.DataFrame(media_mensual).reset_index()
media_mensual = media_mensual.rename(columns={"price":"Total Ventas"})
media_mensual = media_mensual.round(2)
media_mensual['Mes'] = media_mensual['Mes'].map({'01':'Enero',
                             '02':'Febrero',
                             '03':'Marzo',
                             '04':'Abril',
                             '05':'Mayo',
                             '06':'Junio',
                             '07':'Julio',
                             '08':'Agosto'},
                             na_action=None)


ventas_totales = sin_devolucion["price"].sum()


ventas_mensuales = sin_devolucion.Mes.value_counts(ascending=True)
ventas_mensuales = ventas_mensuales.sort_values(ascending=False)
ventas_mensuales = pd.DataFrame(ventas_mensuales).reset_index()
ventas_mensuales.columns = ["Mes", "Ventas"]
ventas_mensuales['Mes'] = ventas_mensuales['Mes'].map({'01':'Enero',
                             '02':'Febrero',
                             '03':'Marzo',
                             '04':'Abril',
                             '05':'Mayo',
                             '06':'Junio',
                             '07':'Julio',
                             '08':'Agosto'},
                             na_action=None)
ventas_mensuales = ventas_mensuales[:5]


print("Bienvenido al sistema \nIngrese sus Datos")
i=0
while i<3:
        usuario = input("Usuario: ")
        i=i +1
        if usuario == "emtech":
            clave=input("Contraseña: ")
            if clave == "12345":
                  print("Bienvenido de nuevo \n")
                  break
            else:
                  print("Clave Incorrecta \n")
                  if    i==3:
                        print("Agotaste los intentos, hasta pronto")
                        break
        else:
            print("Usuario Incorrecto \n")
            if i==3:
                print("Agotaste los intentos, hasta pronto")
                quit()

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls')
	print ("Este programa fue diseñado para generar reportes de venta \n\nListado de reportes disponibles: \n")
	print ("""\t1 - Productos con mayores ventas
\t2 - Productos con Mayores Busquedas
\t3 - Productos con Menores Ventas por Categoria
\t4 - Productos con Menores Busquedas por Categoria
\t5 - Productos con Mejor Reseña
\t6 - Productos con Peor Reseña
\t7 - Total de Ingresos Anuales
\t8 - Promedio de Ventas Mensuales
\t9 - Meses con Más Ventas 
\t0 - Salir del Programa """)
               
def submenu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls')
	print ("Elige una categoria: ")
	print ("""\t1 - Audifonos
\t2 - Discos Duros
\t3 - Procesadores
\t4 - Tarjetas Madre
\t5 - Tarjetas de Video
\t0 - Volver al Menú Principal """)


tecla = "\nPulse una tecla para continuar"

while True:
	# Mostramos el menu
    menu()
 	
    opcionMenu = input("Ingresa el número del reporte que deseas consultar: ")
    if opcionMenu=="1":
        print (mayores_ventas)
        mayores_ventas["Producto"] = mayores_ventas["Producto"].str.split(",").str.get(0)
        plt.pie(mayores_ventas["Ventas"], labels=mayores_ventas["Producto"], autopct='%1.1f%%',
        shadow=True, startangle=90)
        plt.axis('equal')
        plt.title("Productos con mayores ventas")
        plt.savefig('mayores_ventas.png')
        plt.show()
        input(tecla)
    elif opcionMenu=="2":
        print (mayores_busquedas)
        mayores_busquedas["Producto"] = mayores_busquedas["Producto"].str.split(",").str.get(0)
        plt.pie(mayores_busquedas["Busquedas"], labels=mayores_busquedas["Producto"], autopct='%1.1f%%',
        shadow=True, startangle=90)
        plt.axis('equal')
        plt.title("Productos con mayores busquedas")
        plt.savefig('mayores_busquedas.png')
        plt.show()
        input(tecla)
    elif opcionMenu=="3":
        submenu()
        opcionSubmenu = input("Elige una categoria: ")
        if opcionSubmenu=="1":
            print (cat_audifonos)
            input(tecla)
        elif opcionSubmenu=="2":
            print (cat_discos_duros)
            input(tecla)
        elif opcionSubmenu=="3":
            print (cat_procesadores)
            input(tecla)
        elif opcionSubmenu=="4":
            print (cat_tarjetas_madre)
            input(tecla)
        elif opcionSubmenu=="5":
            print (cat_tarjetas_video)
            input(tecla)
        elif opcionSubmenu=="0":
            menu()
    elif opcionMenu=="4":
        submenu()
        opcionSubmenu = input("Elige una categoria: ")
        if opcionSubmenu=="1":
            print (busquedas_audifonos)
            input(tecla)
        elif opcionSubmenu=="2":
            print (busquedas_discos_duros)
            input(tecla)
        elif opcionSubmenu=="3":
            print (busquedas_procesadores)
            input(tecla)
        elif opcionSubmenu=="4":
            print (busquedas_tarjetas_madre)
            input(tecla)
        elif opcionSubmenu=="5":
            print (busquedas_tarjetas_video)
            input(tecla)
        elif opcionSubmenu=="0":
            menu()
        else:
            print ()
            input("\nNo has pulsado ninguna opción correcta...\nPulsa una tecla para continuar")
    elif opcionMenu=="5":
        print("Estos son los 5 productos con mejor reseña: \n")
        print (mayores_resenas)
        input(tecla)
    elif opcionMenu=="6":
        print("Estos son los 5 productos con peor reseña: \n")
        print (menores_resenas)
        input(tecla)
    elif opcionMenu=="7":
        print ("Este año se generó un ingreso total de: $", ventas_totales)
        input(tecla)
    elif opcionMenu=="8":
        print (media_mensual)
        fig, ax = plt.subplots()
        ax.set_ylabel('Ventas ($)')
        ax.set_title('Ingresos Promedio Mensuales')
        plt.bar(media_mensual["Mes"], media_mensual["Total Ventas"])
        plt.savefig('media_mensual.png')
        plt.show()
        input(tecla)
    elif opcionMenu=="9":
        print(ventas_mensuales)
        plt.pie(ventas_mensuales["Ventas"], labels=ventas_mensuales["Mes"], autopct='%1.1f%%',
        shadow=True, startangle=90)
        plt.axis('equal')
        plt.title("Meses con Más Ventas")
        plt.savefig('meses_mas_ventas.png')
        plt.show()
        input(tecla)
    elif opcionMenu=="0":
        print("\nHasta pronto! ")
        break
    else:
        input("\nNo has pulsado ninguna opción correcta...\nPulsa una tecla para continuar")


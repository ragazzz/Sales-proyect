from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    def create(self):
        validar=Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(20,5);print(green_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Agregar cliente'+' '*27+'██')
        gotoxy(22,7);print("Cédula: ")
        dni=validar.cedula('Cédula inválida.', 30, 7)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if client:
            gotoxy(45,7);print("Cédula ya registrada")
            time.sleep(2)
            return
        else:
            gotoxy(22,8); name = input('Ingrese nombre: ')
            gotoxy(22,9); last_name = input('Ingrese apellido: ')
            gotoxy(22,10); ans = input('Tiene tarjeta? (s/n): ')
            client=RegularClient(name,last_name,dni, True if ans == 's' else False)
            json_file = JsonFile(path+'/archivos/clients.json')
            clients = json_file.read()
            data = client.getJson()
            clients.append(data)
            json_file = JsonFile(path+'/archivos/clients.json')
            json_file.save(clients)
            gotoxy(22,11);print('Cliente guardado!')
            time.sleep(2)
            return

    def update(self):
        validar=Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(20,5);print(yellow_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Actualizar Cliente'+' '*24+'██')
        gotoxy(22,7);print("Cédula: ")
        dni=validar.cedula('Cédula inválida.', 30, 7)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(45,7);print("Cliente no existe")
            time.sleep(2)
            return
        else:
            client=client[0]
            cli = RegularClient(client['nombre'],client['apellido'],client['dni'],True if client['valor']==0.1 else False)
            json_file = JsonFile(path+'/archivos/clients.json')
            clients1 = json_file.read()
            gotoxy(22,8);ans = input(f'Desea actualizar la información de {cli.first_name} {cli.last_name}? (s/n) ')
            if ans != 's':
                gotoxy(22,10);print('Cancelando operación...')
                time.sleep(2)
                return
            data1 = cli.getJson()
            clients1.remove(data1)
            json_file = JsonFile(path+'/archivos/clients.json')
            json_file.save(clients1)
            gotoxy(22, 9);cli.first_name = input('Nuevo nombre: ')
            gotoxy(22, 10);cli.last_name = input('Nuevo apellido: ')
            data2 = cli.getJson()
            json_file = JsonFile(path+'/archivos/clients.json')
            clients2 = json_file.read()
            clients2.append(data2)
            json_file.save(clients2)
            gotoxy(22,13);print('Cliente actualizado satisfactoriamente!')
            time.sleep(2)
            return



        
    def delete(self):
        validar=Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(20,5);print(red_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Eliminar Cliente'+' '*26+'██')
        gotoxy(22,7);print("Cédula: ")
        dni=validar.cedula('Cédula inválida.', 30, 7)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(45,7);print("Cliente no existe")
            time.sleep(2)
            return
        else:
            client=client[0]
            cli = RegularClient(client['nombre'],client['apellido'],client['dni'],True if client['valor']==0.1 else False)
            json_file = JsonFile(path+'/archivos/clients.json')
            clients = json_file.read()
            data = cli.getJson()
            gotoxy(22,8);ans=input(f'Está seguro de eliminar el cliente: {cli.first_name} {cli.last_name}?(s/n) ')
            if ans == 's':
                clients.remove(data)
                json_file = JsonFile(path+'/archivos/clients.json')
                json_file.save(clients)
                gotoxy(22,9);print('Cliente eliminado satisfactoriamente')
            else:
                gotoxy(22,9);print('Eliminación cancelada')
            time.sleep(2)
            return

    def consult(self):
        validar=Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(20,5);print(blue_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Buscar Cliente'+' '*28+'██')
        gotoxy(22,7);print('Presione B si desea buscar un cliente o Enter para mostrar todos')
        gotoxy(22,8);ans = input()
        if ans:
            gotoxy(22,9);print("Cédula: ")
            dni=validar.cedula('Cédula inválida.', 30, 9)
            json_file = JsonFile(path+'/archivos/clients.json')
            client = json_file.find("dni",dni)
            if not client:
                gotoxy(45,9);print("Cliente no existe")
                time.sleep(2)
                return
            client=client[0]
            cli = RegularClient(client['nombre'],client['apellido'],client['dni'],True if client['valor']==0.1 else False)
            gotoxy(22,10);cli.show()
            time.sleep(1)
            gotoxy(22,30);input('(Presiona enter para salir)')
            time.sleep(1)
            return
        else:
            json_file = JsonFile(path+'/archivos/clients.json')
            clients = json_file.read()
            gotoxy(22,8);print(green_color+'Cédula')
            gotoxy(37,8);print('Nombre')
            gotoxy(50,8);print('Apellido')
            gotoxy(80,8);print('Descuento'+blue_color)
            for i in range(len(clients)):
                gotoxy(22,10+i);print(f"{clients[i]['dni']}")
                gotoxy(37,10+i);print(f"{clients[i]['nombre']}")
                gotoxy(50,10+i);print(f"{clients[i]['apellido']}")
                gotoxy(80,10+i);print(f"{int(clients[i]['valor']*100)}%") 
            time.sleep(1)
            gotoxy(22,30);input('(Presiona enter para salir)')
            time.sleep(1)
            return


class CrudProducts(ICrud):
    def create(self):
        validar=Valida()
        borrarPantalla()
        json_file = JsonFile(path+'/archivos/products.json')
        print('\033c', end='')
        gotoxy(20,5);print(green_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Agregar producto'+' '*26+'██')
        gotoxy(20,7);print('██'+' '*66+'██')
        gotoxy(22,8);description = input('Descripción: ')
        gotoxy(22,9);print('Precio: ')
        price = validar.solo_decimales(red_color+'Ingrese un número decimal!'+green_color, 31,9)
        gotoxy(22,10);print('Stock: ')
        stock = validar.solo_numeros(red_color+'Ingrese un número entero!'+green_color,30,10)
        prod = Product(description,price,stock)
        json_file = JsonFile(path+'/archivos/products.json')
        products = json_file.read()
        last_id = products[-1]['id']+1
        data = prod.getJson()
        data['id'] = last_id
        products.append(data)
        json_file = JsonFile(path+'/archivos/products.json')
        json_file.save(products)
        gotoxy(22,15);print('Producto guardado exitosamente!')
        time.sleep(2)
        return
    
    def update(self):
        validar=Valida()
        borrarPantalla()
        json_file = JsonFile(path+'/archivos/products.json')
        print('\033c', end='')
        gotoxy(20,5);print(yellow_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Editar Producto'+' '*27+'██')
        gotoxy(22,7);print('ID del producto: ')
        id=validar.solo_numeros(red_color+'Ingrese un número entero'+yellow_color,40,7)
        product = json_file.find('id',id)
        if not product:
            gotoxy(45,7);print("Producto no existe")
            time.sleep(2)
            return
        product=product[0]
        pro = Product(product['id'],product['descripcion'],product['precio'],product['stock'])
        gotoxy(22,8);ans = input(f'Desea actualizar la información del producto: {pro.descrip}? (s/n) ')
        if ans != 's':
            gotoxy(22,10);print('Cancelando operación...')
            time.sleep(2)
            return
        json_file = JsonFile(path+'/archivos/products.json')
        products1=json_file.read()
        data1=pro.getJson()
        products1.remove(data1)
        json_file.save(products1)
        gotoxy(22,9);pro.descrip = input('Nueva descripción: ')
        gotoxy(22,10);print('Nuevo precio: ')
        pro.preci = validar.solo_decimales(red_color+'Ingrese un número decimal!'+green_color,37,10)
        gotoxy(22,11);print('Nuevo stock: ')
        pro.stock = validar.solo_numeros(red_color+'Ingrese un número entero!'+green_color,36,11)
        products2 = json_file.read()
        last_id = products2[-1]['id']+1
        data2 = pro.getJson()
        data2['id'] = last_id
        products2.append(data2)
        json_file.save(products2)
        gotoxy(22,16);print(f'Producto editado con el id: {last_id}')
        time.sleep(2)
        return

    def delete(self):
        validar=Valida()
        borrarPantalla()
        json_file = JsonFile(path+'/archivos/products.json')
        print('\033c', end='')
        gotoxy(20,5);print(red_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Eliminar Producto'+' '*25+'██')
        gotoxy(22,7);print('ID del producto: ')
        id=validar.solo_numeros(red_color+'Ingrese un número entero'+yellow_color,40,7)
        product = json_file.find('id',id)
        if not product:
            gotoxy(45,7);print('Producto no existe')
            time.sleep(2)
            return
        product=product[0]
        pro = Product(product['id'],product['descripcion'],product['precio'],product['stock'])
        products = json_file.read()
        gotoxy(22,8);ans = input(f'Está seguro de eliminar el producto: {pro.descrip}? (s/n) ')
        if ans != 's':
            gotoxy(22,10);print('Cancelando operación...')
            time.sleep(2)
            return
        data = pro.getJson()
        products.remove(data)
        json_file.save(products)
        gotoxy(22,15); print('Eliminación exitosa')
        time.sleep(2)
        return
    
    def consult(self):
        validar=Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(20,5);print(blue_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Consultar Producto'+' '*24+'██')
        gotoxy(22,7);print('Presione B si desea buscar un producto o Enter para mostrar todos')
        gotoxy(22,8);ans = input()
        if ans:
            gotoxy(22,9);print("ID del producto: ")
            id=validar.solo_numeros('Ingrese solo número enteros', 40, 9)
            json_file = JsonFile(path+'/archivos/products.json')
            product = json_file.find("id",id)
            if not product:
                gotoxy(45,9);print("Producto no existe")
                time.sleep(2)
                return
            product=product[0]
            pro = Product(product['id'],product['descripcion'],product['precio'],product['stock'])
            gotoxy(22,10);pro.show()
            time.sleep(1)
            gotoxy(22,30);input('(Presiona enter para salir)')
            time.sleep(1)
            return
        else:
            json_file = JsonFile(path+'/archivos/products.json')
            products = json_file.read()
            gotoxy(22,8);print(green_color+'ID')
            gotoxy(37,8);print('Descripción')
            gotoxy(70,8);print('Precio')
            gotoxy(80,8);print('Stock'+blue_color)
            for i in range(len(products)):
                gotoxy(22,10+i);print(f"{products[i]['id']}")
                gotoxy(37,10+i);print(f"{products[i]['descripcion']}")
                gotoxy(70,10+i);print(f"$ {products[i]['precio']:.2f}")
                gotoxy(80,10+i);print(f"{products[i]['stock']}") 
            time.sleep(1)
            gotoxy(22,30);input('(Presiona enter para salir)')
            return

class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cédula:")
        dni=validar.cedula('Cédula inválida.', 23, 6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe")
            time.sleep(2)
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(green_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea")
        gotoxy(12,9);print("Id_Articulo")
        gotoxy(24,9);print("Descripcion")
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line);
            id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print("Producto no existe")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:
                prods=prods[0]
                product = Product(prods['id'],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(blue_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            if not invoices:
                data = sale.getJson()
                data['factura'] = 1
                invoices.append(data)
                json_file.save(invoices)
                return
            ult_invoices = invoices[-1]["factura"]+1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print("🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(2)    
    
    def update(self):
        pass


    def delete(self):
        validar=Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(20,5);print(red_color+'█'*70)
        gotoxy(20,6);print('██'+' '*24+'Eliminar Factura'+' '*26+'██')
        gotoxy(22,7);print("Número de factura: ")
        id=validar.solo_numeros(red_color+'Solo números!', 42, 7)
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoice = json_file.find('factura',int(id))
        if not invoice:
            gotoxy(45,7);print("La factura no existe")
            time.sleep(2)
            return
        gotoxy(22,8);ans=input(f'Está seguro de eliminar la factura {id}?(s/n) ')
        if ans == 's':
            invoices = json_file.read()
            invoices.remove(invoice[0])
            json_file.save(invoices)
            gotoxy(22,9);print('Factura eliminada')
        else:
            gotoxy(22,9);print('Eliminación cancelada')
        time.sleep(2)
        return
        
    
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Venta"+" "*35+"██")
        gotoxy(2,4);invoice= input("Ingrese Factura: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.find("factura",invoice)
            if not invoices:
                print('La facura no existe')
                time.sleep(2)
                return
            print(f"Impresion de la Factura#{invoice}")
            invoices = invoices[0]
            print('Fecha          Cliente               Cantidad de Productos    Total')
            print(blue_color+f"{invoices['Fecha']}     {invoices['cliente']}                    {len(invoices['detalle'])}             $ {invoices['total']:.2f}"+green_color)
        else:
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            if invoices:
                print("Consulta de Facturas")
                for fac in invoices:
                    print(f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}")
            else:
                print('No hay facturas para mostrar')
        x=input("presione una tecla para continuar...")    

#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu(cyan_color+"💸 Menu Facturación",[blue_color+"1) Clientes","2) Productos","3) Ventas",red_color+"4) Salir"+reset_color],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()
            clients = CrudClients()  
            menu_clients = Menu(yellow_color+"Menu Cientes",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                clients.create()
            elif opc1 == "2":
                clients.update()
            elif opc1 == "3":
                clients.delete()
            elif opc1 == "4":
                clients.consult()
            print("Regresando al menu Clientes...")
            # time.sleep(2)            
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()
            products = CrudProducts()
            menu_products = Menu("Menu Productos",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                products.create()
            elif opc2 == "2":
                products.update()
            elif opc2 == "3":
                products.delete()
            elif opc2 == "4":
                products.consult()
    elif opc == "3":
        opc3 =''
        while opc3 !='4':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Consultar","3) Eliminar","4) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
                
            elif opc3 == "2":
                sales.consult()
            
            elif opc3 == '3':
                sales.delete()
     
    print("Regresando al menu Principal...")
    # time.sleep(2)            

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()


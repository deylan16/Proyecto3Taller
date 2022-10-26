from pydoc import cli
from LectorDeArchivos import *
#Variables con la informacion de los archivos
pasillos = CargarPasillos()
productosPasillo = CargarProductospasillo(pasillos)
marcasProductos = CargarMarcaproductos(productosPasillo)
inventarios = CargarInventario()
clientes = CargarClientes()
Administradores =  CargarAdministradores()
Vendedores = CargarVendedores()
#######################
######para reportes######
registroTienda = []
RegistroTodasCompras = []
consecutivo = 0
ListaProductos = []
pasillosComprados = []
PasilloProductosComprados = []
MarcasCompradas = []
ClientesMontoComprados = []
ProductoCantidaCargados = []
ClientesFacturados = []
FacturaMontoRealizadas = []
cedulaFacturas = []
ultimosDosProductosInsertado = []
ultimoProductoModificado = []
#########################
#para descuentos
cantidadDescuento = 3
porcentajeDescuento = 5
#########################


#Muestra una lista acomodada para que se vea como matriz
def mostrarLista(lista):
    i =0
    while(i < len(lista)):
        print(lista[i])
        i += 1

#indica la primera  fila en que aparece un dato
#lista es la matriz a buscar
#dato es el que desea buscar 
#indice es la columna qie tiene buscar
def buscaEnLista(lista,dato,indice):
    i =0
    while(i < len(lista)):
        if(lista[i][indice] == dato):
            return i
        i += 1
    return -1

#indica la todas las  fila en que aparece un dato
#lista es la matriz a buscar
#dato es el que desea buscar 
#indice es la columna qie tiene buscar
def buscaEnLista2(lista,dato,indice):
    i =0
   
    listaR = []
    
    
    while(i < len(lista)):
        
        if(lista[i][indice] == dato):
            listaR +=[i]
        i += 1
    return listaR

#verifica si un strin solo continene numneros
def verificaNumero(n):
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    for i in range(len(n)):
        if (not(n[i] in numeros)):
            return False
    return True

#indica si un producto es de la canasta basica
def tiene13(codMarca):
    posicion = buscaEnLista(inventarios,codMarca,2)
    
    if(inventarios[posicion][5] == "0"):
        return True
    else:
        return False

#indica el elmentos que mas se repite
def moda(lista):
    frecuencia = {}

    for valor in lista:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1

    masFrecuentes = max(frecuencia.values())

    modas = [key for key, valor in frecuencia.items()
                      if valor == masFrecuentes]

    return modas 

#indica el elemento que menos se repite
def modaInversa(lista):
    frecuencia = {}

    for valor in lista:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1

    menosFrecuentes = min(frecuencia.values())

    modas = [key for key, valor in frecuencia.items()
                      if valor == menosFrecuentes]

    return modas

#retorna una lista con las filas que continene la llave
#lista es la matriz a buscar
#llave  es el dato que desea buscar 
#indice es la columna qie tiene buscar
def Hagalista(lista,llave,indice):
    result = []
    for i in lista:
        
        if(i[indice] == llave):
            result += [i]
    return result

##################################################################
#funciones menu Administrador
#Para insertar

#Retorna -1 si el codigo de pasillo existe
#Retorna -2 si el codigo pasiilo no es un numero
def InsertarPasillo(CodPasillo,Nombre):
    global pasillos
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)!=[]:
        return -1
    else:
        nuevoPasillo = [CodPasillo,Nombre]
        pasillos += [nuevoPasillo]
        return nuevoPasillo
        
#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto existe   
def Productonuevo(CodPasillo,CodProducto,Nombre):
    global pasillos,productosPasillo
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CodProducto,1)
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)==[]:
        return -1
    elif not(verificaNumero(CodProducto)):
        return -4
    elif (listaCodigoProducto)!=[]:
        return -3
    else:
        nuevoProducto = [CodPasillo,CodProducto,Nombre]
        productosPasillo += [nuevoProducto]
        return nuevoProducto
    
#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto no existe   
#Retorna -5 si el codigo de marca existe
#Retorna -6 si el codigo de maca no es un numero
#Retorna -7 si la contidad en gondola no es un numero
#Retorna -8 si el precio no es un numero           
def Marcanueva(CodPasillo,CodProducto,CodMarca,Nombre,CantidadGondola,Precio):
    global pasillos,productosPasillo,marcasProductos
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CodProducto,1)
    listaCodigoMarcas=buscaEnLista2(marcasProductos,CodMarca,2)
                
                
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)==[]:
        return -1
    elif not(verificaNumero(CodProducto)):
        return -4
    elif (listaCodigoProducto)==[]:
        return -3
    elif not(verificaNumero(CodMarca)):
        return -6
    elif (listaCodigoMarcas)!=[]:
        return -5
    elif not(verificaNumero(CantidadGondola)):
        return -7
    elif not(verificaNumero(Precio)):
        return -8
    else:
        nuevaMarca = [CodPasillo,CodProducto,CodMarca,Nombre,CantidadGondola,Precio]
        marcasProductos += [nuevaMarca]
        return nuevaMarca

#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto no existe   
#Retorna -5 si el codigo de marca existe
#Retorna -6 si el codigo de maca no es un numero
#Retorna -7 si la contidad en stock no es un numero
#Retorna -8 si el codigo canasta no es un 1  un 0   
def InsertarInventario(CodPasillo,CodProducto,CodMarca,Nombre,CantidadStock,CodigoCanasta ):
    global pasillos,productosPasillo,inventarios,ultimosDosProductosInsertado
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CodProducto,1)
    listaCodigoInventario=buscaEnLista2(inventarios,CodMarca,2)
                
                
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)==[]:
        return -1
    elif not(verificaNumero(CodProducto)):
        return -4
    elif (listaCodigoProducto)==[]:
        return -3
    elif not(verificaNumero(CodMarca)):
        return -6
    elif (listaCodigoInventario)!=[]:
        return -5
    elif not(verificaNumero(CantidadStock)):
        return -7
    elif not(CodigoCanasta in ["0","1"]):
        return -8
    else:
        nuevaMarca = [CodPasillo,CodProducto,CodMarca,Nombre,CantidadStock,CodigoCanasta]
        inventarios += [nuevaMarca]
        ultimo = [CodPasillo,CodProducto,CodMarca]
        ultimosDosProductosInsertado += ultimo
        if len(ultimosDosProductosInsertado) > 2:
            ultimosDosProductosInsertado = ultimosDosProductosInsertado[-2]
        return nuevaMarca

#Retorna -1 si la cedula existe
#Retorna -2 la cedula no es un numero    
def RegistrarClientes(Cedula,Nombre,Telefono,Correo):
    global clientes
    listaCedula=buscaEnLista2(clientes,Cedula,0)
    if not(verificaNumero(Cedula)):
        return -2
    elif (listaCedula)!=[]:
        return -1
    else:
        nuevoCliente = [Cedula,Nombre,Telefono,Correo]
        clientes += [nuevoCliente]
        return nuevoCliente
        
#Retorna -1 si el codigo adminstrador existe
#Retorna -2 el codigo adminstrador no es un numero      
def RegistrarAdministradores(CodAdministrador,Nombre):
    global Administradores
    listaCodigoAdministrador=buscaEnLista2(Administradores,CodAdministrador,0)
    if not(verificaNumero(CodAdministrador)):
        return -2
    elif (listaCodigoAdministrador)!=[]:
        return -1
    else:
        nuevoAdministrador = [CodAdministrador,Nombre]
        Administradores += [nuevoAdministrador]
        return nuevoAdministrador
    
#Retorna -1 si el codigo vendedor existe
#Retorna -2 el codigo vendedor no es un numero   
def RegistrarVendedores(CodVendedor,Nombre):
    global Vendedores
    listaCodigoVendedorr=buscaEnLista2(Vendedores,CodVendedor,0)
    if not(verificaNumero(CodVendedor)):
        return -2
    elif (listaCodigoVendedorr)!=[]:
        return -1
    else:
        nuevoVendedor = [CodVendedor,Nombre]
        Vendedores += [nuevoVendedor]
        return nuevoVendedor
    
#############
##ParaEliminar

#Retorna -1 si no exite pasiilo con esas datos

def EliminarPasillo(CodPasillo,Nombre):
    global pasillos
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    listaCodigoPasilloFila=Hagalista(pasillos,CodPasillo,0)
    result = -1
    i = 0
    for n in listaCodigoPasilloFila:
        if (n == [CodPasillo,Nombre]):
            pasillos.pop(listaCodigoPasillo[i])
            result = [CodPasillo,Nombre]
        i += 1
    if result != -1:
        listaCodigoProducto=buscaEnLista2(productosPasillo,CodPasillo,0)
        for j in listaCodigoProducto:
            productosPasillo.pop(j)
        listaCodigoMarcas=buscaEnLista2(marcasProductos,CodPasillo,0)
        for m in listaCodigoMarcas:
            marcasProductos.pop(m)
        listaCodigoInventario=buscaEnLista2(inventarios,CodPasillo,0)
        for k in listaCodigoInventario:
            inventarios.pop(k)
    return result
    

#Retorna -1 si no exite producto con esas datos   
def EliminarProducto (CodPasillo,CodProducto,Nombre):
    global pasillos,productosPasillo
    listaCodigoProducto=buscaEnLista2(productosPasillo,CodProducto,1)
    listaCodigoProductoFila=Hagalista(productosPasillo,CodProducto,1)
    result = -1
    i = 0
    for n in listaCodigoProductoFila:
        if (n == [CodPasillo,CodProducto,Nombre]):
            productosPasillo.pop(listaCodigoProducto[i])
            result = [CodPasillo,CodProducto,Nombre]
        i += 1
    if result != -1:
        
        listaCodigoMarcas=buscaEnLista2(marcasProductos,CodProducto,1)
        for m in listaCodigoMarcas:
            marcasProductos.pop(m)
        listaCodigoInventario=buscaEnLista2(inventarios,CodProducto,1)
        for k in listaCodigoInventario:
            inventarios.pop(k)
    return result

#Retorna -1 si  marca no existe
def EliminarMarca (CodPasillo,CodProducto,CodMarca,Nombre,CantidadGondola,Precio):
    global pasillos,productosPasillo
    listaCodigoMarca=buscaEnLista2(marcasProductos,CodMarca,2)
    listaCodigoMarcaFila=Hagalista(marcasProductos,CodMarca,2)
    result = -1
    i = 0
    for n in listaCodigoMarcaFila:
        if (n == [CodPasillo,CodProducto,CodMarca,Nombre,CantidadGondola,Precio]):
            marcasProductos.pop(listaCodigoMarca[i])
            result = [CodPasillo,CodProducto,CodMarca,Nombre,CantidadGondola,Precio]
        i += 1
    if result != -1:
        listaCodigoInventario=buscaEnLista2(inventarios,CodMarca,2)
        for k in listaCodigoInventario:
            inventarios.pop(k)
    return result

#Retorna -1 si  marca no existe
def EliminarInventario(CodPasillo,CodProducto,CodMarca,Nombre,CantidadStock,CodigoCanasta):
    global pasillos,productosPasillo
    listaCodigoMarca=buscaEnLista2(inventarios,CodMarca,2)
    listaCodigoMarcaFila=Hagalista(inventarios,CodMarca,2)
    result = -1
    i = 0
    for n in listaCodigoMarcaFila:
        if (n == [CodPasillo,CodProducto,CodMarca,Nombre,CantidadStock,CodigoCanasta]):
            inventarios.pop(listaCodigoMarca[i])
            result = [CodPasillo,CodProducto,CodMarca,Nombre,CantidadStock,CodigoCanasta]
        i += 1
    if result != -1:
        listaCodigoInventario=buscaEnLista2(marcasProductos,CodMarca,2)
        for k in listaCodigoInventario:
            marcasProductos.pop(k)
    return result

#Retorna -1 si  cecula no existe
def Eliminarclientes(Cedula,Nombre,Telefono,Correo):
    listaCodigoCedula=buscaEnLista2(clientes,Cedula,0)
    listaCodigoCedulaFila=Hagalista(clientes,Cedula,0)
    result = -1
    i = 0
    for n in listaCodigoCedulaFila:
        if (n == [Cedula,Nombre,Telefono,Correo]):
            clientes.pop(listaCodigoCedula[i])
            result = [Cedula,Nombre,Telefono,Correo]
        i += 1
    
    return result
#Retorna -1 si  codigo administrador no existe
def Eliminaradministradores(CodAdministrador,Nombre):
    listaCodigoCodAdmin=buscaEnLista2(Administradores,CodAdministrador,0)
    listaCodigoCodAdminFila=Hagalista(Administradores,CodAdministrador,0)
    result = -1
    i = 0
    for n in listaCodigoCodAdminFila:
        if (n == [CodAdministrador,Nombre]):
            Administradores.pop(listaCodigoCodAdmin[i])
            result = [CodAdministrador,Nombre]
        i += 1
    
    return result
   
#Retorna -1 si  codigo vendedor no existe 
def Eliminarvendedores(CodVendedor,Nombre):
    listaCodigoCodVendedor=buscaEnLista2(Vendedores,CodVendedor,0)
    listaCodigoCodVendedorFila=Hagalista(Vendedores,CodVendedor,0)
    result = -1
    i = 0
    for n in listaCodigoCodVendedorFila:
        if (n == [CodVendedor,Nombre]):
            Vendedores.pop(listaCodigoCodVendedor[i])
            result = [CodVendedor,Nombre]
        i += 1
    
    return result
##################
#Para Modificar

#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero
def ModificarPasillo(CodPasillo,Nombre):
    global pasillos
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)==[]:
        return -1
    else:
        nuevoPasillo = [CodPasillo,Nombre]
        pasillos[listaCodigoPasillo[0]] = nuevoPasillo
        return nuevoPasillo
    
#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto no existe   
def ModificarProducto(CodPasillo,CodProducto,Nombre):
    global pasillos,productosPasillo,ultimoProductoModificado
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CodProducto,1)
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)==[]:
        return -1
    elif not(verificaNumero(CodProducto)):
        return -4
    elif (listaCodigoProducto)==[]:
        return -3
    else:
        nuevoProducto = [CodPasillo,CodProducto,Nombre]
        productosPasillo[listaCodigoProducto[0]] = nuevoProducto
        ultimoProductoModificado = nuevoProducto
        return nuevoProducto

#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto no existe   
#Retorna -5 si el codigo de marca  no existe
#Retorna -6 si el codigo de maca no es un numero
#Retorna -7 si la contidad en gondola no es un numero
#Retorna -8 si el precio no es un numero           
def ModificarMarca(CodPasillo,CodProducto,CodMarca,Nombre,CantidadGondola,Precio):
    global pasillos,productosPasillo,marcasProductos
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CodProducto,1)
    listaCodigoMarcas=buscaEnLista2(marcasProductos,CodMarca,2)
                
                
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)==[]:
        return -1
    elif not(verificaNumero(CodProducto)):
        return -4
    elif (listaCodigoProducto)==[]:
        return -3
    elif not(verificaNumero(CodMarca)):
        return -6
    elif (listaCodigoMarcas)==[]:
        return -5
    elif not(verificaNumero(CantidadGondola)):
        return -7
    elif not(verificaNumero(Precio)):
        return -8
    else:
        nuevaMarca = [CodPasillo,CodProducto,CodMarca,Nombre,CantidadGondola,Precio]
        marcasProductos[listaCodigoMarcas[0]] = nuevaMarca
        return nuevaMarca

#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto no existe   
#Retorna -5 si el codigo de marca no existe
#Retorna -6 si el codigo de maca no es un numero
#Retorna -7 si la contidad en stock no es un numero
#Retorna -8 si el codigo canasta no es un 1  un 0   
def ModificarInventario(CodPasillo,CodProducto,CodMarca,Nombre,CantidadStock,CodigoCanasta ):
    global pasillos,productosPasillo,inventarios
    listaCodigoPasillo=buscaEnLista2(pasillos,CodPasillo,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CodProducto,1)
    listaCodigoInventario=buscaEnLista2(inventarios,CodMarca,2)
                
                
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)==[]:
        return -1
    elif not(verificaNumero(CodProducto)):
        return -4
    elif (listaCodigoProducto)==[]:
        return -3
    elif not(verificaNumero(CodMarca)):
        return -6
    elif (listaCodigoInventario)==[]:
        return -5
    elif not(verificaNumero(CantidadStock)):
        return -7
    elif not(CodigoCanasta in ["0","1"]):
        return -8
    else:
        nuevaMarca = [CodPasillo,CodProducto,CodMarca,Nombre,CantidadStock,CodigoCanasta]
        inventarios[listaCodigoInventario[0]] = nuevaMarca
        return nuevaMarca

#Retorna -1 si la cedula no existe
#Retorna -2 la cedula no es un numero    
def ModificarClientes(Cedula,Nombre,Telefono,Correo):
    global clientes
    listaCedula=buscaEnLista2(clientes,Cedula,0)
    if not(verificaNumero(Cedula)):
        return -2
    elif (listaCedula)==[]:
        return -1
    else:
        nuevoCliente = [Cedula,Nombre,Telefono,Correo]
        clientes[listaCedula[0]] = nuevoCliente
        return nuevoCliente
        
#Retorna -1 si el codigo adminstrador si existe
#Retorna -2 el codigo adminstrador no es un numero      
def ModificarAdministradores(CodAdministrador,Nombre):
    global Administradores
    listaCodigoAdministrador=buscaEnLista2(Administradores,CodAdministrador,0)
    if not(verificaNumero(CodAdministrador)):
        return -2
    elif (listaCodigoAdministrador)==[]:
        return -1
    else:
        nuevoAdministrador = [CodAdministrador,Nombre]
        Administradores[listaCodigoAdministrador[0]] = nuevoAdministrador
        return nuevoAdministrador
    
#Retorna -1 si el codigo vendedor no existe
#Retorna -2 el codigo vendedor no es un numero   
def ModificarVendedores(CodVendedor,Nombre):
    global Vendedores
    listaCodigoVendedorr=buscaEnLista2(Vendedores,CodVendedor,0)
    if not(verificaNumero(CodVendedor)):
        return -2
    elif (listaCodigoVendedorr)==[]:
        return -1
    else:
        nuevoVendedor = [CodVendedor,Nombre]
        Vendedores[listaCodigoVendedorr[0]] = nuevoVendedor
        return nuevoVendedor

###################################################
#Retorna -1 si la informacion no coincide
def consultarPrecio(codigoPasillo,codigoProducto,codigoMarca):
    result = -1
    for i in marcasProductos:
        if [i[0],i[1],i[2]] == [codigoPasillo,codigoProducto,codigoMarca]:
            result = i[5]
    return result

#Retorna la cantidad de facturas necesarios y el procentaje
def ConsultarDescuento():
    return [cantidadDescuento,porcentajeDescuento]

#Retorna -1 si ña cantidad nueva no es un numero
#Retorna -2 si el porcentaje nueva no es un numero
def ModificarDescuento(cantidadNueva,porcentajeNuevo):
    global cantidadDescuento,porcentajeDescuento
    if not verificaNumero(cantidadNueva):
        return -1
    elif not verificaNumero(porcentajeNuevo):
        return -2
    else:
        cantidadDescuento = cantidadNueva
        porcentajeDescuento = porcentajeNuevo
        return 0

#Retorna la cantidad de facturas que tiene una cedula
def cantidadFacturas(cedula):
    contador  = 0
    for i in ClientesFacturados:
        if cedula == ClientesFacturados[0]:
                contador += 1
    return contador

#Retorna si una cedula tiene descuento
def descuento(cedula):
    contador  = 0
    for i in ClientesFacturados:
        if cedula == ClientesFacturados[0]:
                contador += 1
    if contador >= cantidadDescuento:
        return True
    else:
        return False    

#Retorna -1 si no hat facturas pendientes
#Retorna 0 si se facturo algo
def facturar():
    print("----------------------------------")
    print("Se esta factaurando")
    print("----------------------------------")
    global registroTienda,ListaProductos,RegistroTodasCompras,pasillosComprados,PasilloProductosComprados,MarcasCompradas,ClientesMontoComprados
    global ProductoCantidaCargados,ClientesFacturados,FacturaMontoRealizadas
    if(len(registroTienda) != 0):
        facturando = registroTienda[0]
        factura = open("Archivos/"+facturando[0]+(str)(cantidadFacturas(facturando[0])) +".txt", "w")
        i = 0

        nombre = buscaEnLista(clientes,facturando[0],0)
        factura.write("Consecutivo Factura: #"+ (str)(cantidadFacturas(facturando[0])) + "\n")
        factura.write("\n")
        factura.write("Cedula:"+ facturando[0] + "\n")
        factura.write("Nombre:"+ clientes[nombre][1] + "\n")
        factura.write("Telefono:"+ clientes[nombre][2] + "\n")
        factura.write("\n")
        factura.write("Producto\tCantidad\tPrecio Unitario\ttotal\n")
        
        
        #factura.write("Marca:CantidadxPrecio+= total" + "\n")
        #factura.write("\n")
        precioTotal = 0
        while (i< len(facturando[1])):
            cantidad = facturando[1][i][4] 
            precio = facturando[1][i][5]
            producto = facturando[1][i][3]
            string = ""+producto+"\t"+cantidad+"\n"+precio
            ListaProductos += [[facturando[1][i][2],facturando[1][i][4]]]
            productoMarca1 = buscaEnLista(marcasProductos,facturando[1][i][2],2)
            print(marcasProductos[productoMarca1][4] )
            marcasProductos[productoMarca1][4] = (str)((int)(marcasProductos[productoMarca1][4])-(int)(facturando[1][i][4]))
            print(marcasProductos[productoMarca1][4] )
            #####para #######
            productoComprando = facturando[1][i]

            pasillosComprados += [productoComprando[0]]
            for j in range((int)(facturando[1][i][4])):
                PasilloProductosComprados += [[productoComprando[0],productoComprando[3]]]
            MarcasCompradas += [productoComprando[2]]
            
            
            #################
            if (tiene13(facturando[1][i][2]) ):
                string += "+ 13% \t "
                total = ((int)(facturando[1][i][4])*(int)(facturando[1][i][5]))* 1.13
                string += (str)(total)
                precioTotal += total
            else:
                
                total = ((int)(facturando[1][i][4])*(int)(facturando[1][i][5]))
                string += (str)(total)
                precioTotal += total
            
            factura.write(string + "\n")

            i+= 1
        factura.write("\n")
        factura.write("Total:"+ (str)(precioTotal) + "\n")
        if(descuento(facturando[0])):
            factura.write("Descuento:"+ (str)(porcentajeDescuento) + "%\n")
            factura.write("Total a Pagar:"+ (str)(precioTotal-(precioTotal *(porcentajeDescuento/100))) + "\n")
        else:
            factura.write("Descuento:"+ (str)(0) + "%\n")
            factura.write("Total a Pagar:"+ (str)(precioTotal) + "\n")
        


        #######para reportes#####
        indiceClienteMonto = buscaEnLista(ClientesMontoComprados,facturando[0],0)
        if(indiceClienteMonto != -1):
            ClientesMontoComprados[indiceClienteMonto][1] = ClientesMontoComprados[indiceClienteMonto][1] + precioTotal
        else:
            ClientesMontoComprados += [[facturando[0],precioTotal]]
        ClientesFacturados += [facturando[0]]
        #print(ClientesMontoComprados)
        FacturaMontoRealizadas += [[facturando[0]+(str)(consecutivo),precioTotal]]
        #########################
        factura.close()
        RegistroTodasCompras += registroTienda[0]
        registroTienda = registroTienda[1:]
        
        return 0
    else:
        print("No hay facturas pendientes")  
        return -1 
 
#retorna los clientes que mas facturaron
def montosFactutados(lista):
    monto = 0
    resultado = []
    for n in lista:
        if((int)(n[1]) > monto):
            monto = (int)(n[1])
            resultado = [n]
        elif((int)(n[1]) == monto):
            
            resultado += [n]
    return resultado   
#retorna los clientes que menos facturaron
def montosFactutadosmenos(lista):
    monto = montosFactutados(lista)[0][1]
    resultado = []
    for n in lista:
        if((int)(n[1]) < monto):
            monto = (int)(n[1])
            resultado = [n]
        elif((int)(n[1]) == monto):
            
            resultado += [n]
    return resultado
########################################
#Reportes

#1.Pasillo mas visitado
#Retorna -1 si no se ha facturador nada
def PasilloMasVisitado():
    if RegistroTodasCompras==[]:
        return -1
    else:
        return moda(pasillosComprados)
#2.Pasillo menos visitado
#Retorna -1 si no se ha facturador nada
def PasilloMenosVisitado():
    if RegistroTodasCompras==[]:
        return -1
    else:
        return (modaInversa(pasillosComprados))

#3.Productos por pasillo mas vendido
#Retorna -1 si no se ha facturador nada
#Retorna -2 si no existe el pasillo
def ProductosPorPasilloMasVendido(CodPasillo):
    if RegistroTodasCompras==[]:
        return -1
    elif buscaEnLista(pasillos,CodPasillo,0)== -1:
        return -2
    else:
        return (moda(Hagalista(PasilloProductosComprados,CodPasillo,0)))
        
#4.Marcas mas vendidas
#Retorna -1 si no se ha facturador nada
def MarcasMasVendidas():
    if RegistroTodasCompras==[]:
        return -1
    else:
        return (moda(MarcasCompradas))
#5.Cliente que mas compro
#Retorna -1 si no se ha facturador nada
def ClienteQueMasCompro():
    if RegistroTodasCompras==[]:
        return -1
    else:
        return (montosFactutados(ClientesMontoComprados))
#6.Cliente que menos compro
#Retorna -1 si no se ha facturador nada
def ClienteQueMenosCompro():
    if RegistroTodasCompras==[]:
        return -1
    else:
        return (montosFactutadosmenos(ClientesMontoComprados))
#7.Producto que mas se cargo en las Gondolas
def ProductoQueMasSeCargoEnLasGondolas():
    return montosFactutados(ProductoCantidaCargados)
#8.Cliente que mas facturo
#Retorna -1 si no se ha facturador nada
def ClienteQueMasFacturo():
    if RegistroTodasCompras==[]:
        return -1
    else:
        return (moda(ClientesFacturados))
#9.Marcas de un producto
#Retorna -1 si no se ha facturador nada
#Retorna -2 si no existe el producto
def MarcasDeUnProducto(CodProducto):
    if RegistroTodasCompras==[]:
        return -1
    elif buscaEnLista(productosPasillo,CodProducto,1)== -1:
        return -2
    else:
        return (Hagalista(marcasProductos,CodProducto,1))
    
#10.Factura de mayor monto
#Retorna -1 si no se ha facturador nada
def FacturaDeMayorMonto():
    if RegistroTodasCompras==[]:
        return -1
    else:
        return montosFactutados(FacturaMontoRealizadas)
        
#11.Productos de un pasillo
#Retorna -1 si el pasillo no existe
def ProductosDeUnPasillo(CodPasillo):
    if buscaEnLista(pasillos,CodPasillo,0)== -1:
        return -1
    else:
        return ((Hagalista(productosPasillo,CodPasillo,0)))
#12.Clientes del supermercado
def ClientesDelSupermercado():
    return clientes
#13.Pasillos del supermercado
def PasillosDelSupermercado():
    return pasillos
#14.Inventario del supermercado
def InventarioDelSupermercado():
    return inventarios

#15.UltimosDosProductosInsertadosAlInventario
def UltimosDosProductosInsertadosAlInventario():
    return ultimosDosProductosInsertado
#16.ultimoProductoModificado
def ultimoProductoModificado():
    return ultimoProductoModificado
#17.PromedioPreciosDeUnProducto();
def PromedioPreciosDeUnProducto():
    result = []
    for i in productosPasillo:
        productos = Hagalista(marcasProductos,i[1],1)
        if productos != []:
            suma = 0
            for n in productos:
                suma+= int(n[5])
            result += [i,suma/len(productos)]
        else:
            result += [i,0]
    return result
        



#########################
#comprar
CedulaClienteActual = "1234567";   
productoscomprados = []

#agrega producto al carrito
#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto no existe   
#Retorna -5 si el codigo de marca  no existe
#Retorna -6 si el codigo de maca no es un numero  
#Retorna -7 si la cantidad a comprar no es un numero
#Retorna -8 si la cantidad a comprar es mayor a la cantidad en gondola
def comprando(CodPasillo,CodProducto,CodMarca,CantidadComprar):
    
    global pasillos,productosPasillo,marcasProductos,productoscomprados
    listaCodigoPasillo =Hagalista(marcasProductos,CodPasillo,0)
    listaCodigoPasilloCodigoProducto = Hagalista(listaCodigoPasillo,CodProducto,1)
    listaCodigoPasilloCodigoMarca = Hagalista(listaCodigoPasilloCodigoProducto,CodMarca,2)
                
                
                
    if not(verificaNumero(CodPasillo)):
        return -2
    elif (listaCodigoPasillo)==[]:
        return -1
    elif not(verificaNumero(CodProducto)):
        return -4
    elif (listaCodigoPasilloCodigoProducto)==[]:
        return -3
    elif not(verificaNumero(CodMarca)):
        return -6
    elif (listaCodigoPasilloCodigoMarca)==[]:
        return -5
    
    
    ######
    elif not verificaNumero(CantidadComprar):
        return -7
    
    elif int(CantidadComprar) > int(listaCodigoPasilloCodigoMarca[0][4]):
        return -8
    
    else:
        productoscomprados += [[listaCodigoPasilloCodigoMarca[0][0],listaCodigoPasilloCodigoMarca[0][1],listaCodigoPasilloCodigoMarca[0][2],listaCodigoPasilloCodigoMarca[0][3],CantidadComprar,listaCodigoPasilloCodigoMarca[0][5]]]                   
        return productoscomprados

#Retorna -1 si no se ha comprado nada  
#Retorna -2 si no esta el producto
def EliminarProductoCarrito(CodPasillo,CodProducto,CodMarca):
    if productoscomprados == []:
        return -1
    else:
        contador = 0
        for i in productoscomprados:
            if [i[0],i[1],i[2]] == [CodPasillo,CodProducto,CodMarca]:
                productoscomprados.pop(contador)
                return i 
            contador += 1
        return -2   
#agrega carrito a facturar  
#Retorna -1 si no se ha comprado nada  
def Comprar(cedula):
    global registroTienda,productoscomprados
    if productoscomprados == []:
        return -1
    else:
        
        listaCompraCliente = [cedula]
        #productoscomprados = []
        #productoscomprados += productoscomprados 
        listaCompraCliente += [productoscomprados]
        registroTienda += [listaCompraCliente]
        productoscomprados = []
print(marcasProductos)
print("*************\n")
print(PromedioPreciosDeUnProducto())        



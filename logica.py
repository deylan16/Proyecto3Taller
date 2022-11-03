from pydoc import cli
from LectorDeArchivos import *
#Importación de librerías
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
def mostrarNuevoPasillo(lista):
    listaStr = ["Código Pasillo: ", "Nombre: "]
    totalStr = ""
    for i in range(len(lista)):
        if(i == len(lista)-1):
            totalStr += listaStr[i]+lista[i]
        else:
            totalStr += listaStr[i]+lista[i]+"\n"
            
    return totalStr   

def ModificarPasillo(CodPasillo,Nombre):
    global pasillos
    CDP=CodPasillo.get()
    Nom=Nombre.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    if not(verificaNumero(CDP)):
        return messagebox.showinfo("Error en el codigo de pasillo","El Codigo ingresado no existe")
    elif (listaCodigoPasillo)==[]:
        return messagebox.showinfo("Error en el codigo de pasillo","El Codigo ingresado no existe")
    else:
        nuevoPasillo = [CDP,Nom]
        pasillos[listaCodigoPasillo[0]] = nuevoPasillo
        totalInfo=mostrarNuevoPasillo(nuevoPasillo)
        return messagebox.showinfo("Pasillo Modificado", totalInfo)
        
    
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
            string = ""+producto+"\t"+cantidad+"\t\t"+precio+"\t\t\t"
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
    Clientes = clientes
    with open('Reporte-Clientes.txt','w') as reporte:
        for i in Clientes:
            reporte.write(i[0]+" "+i[1]+" "+i[2]+" "+i[3]+'\n')
        return messagebox.showinfo("Reporte Creado","El reporte se creo correctamente")
            
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
cedulaActual = ""
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
    print(productoscomprados)
    if productoscomprados == []:
        return -1
    else:
        
        listaCompraCliente = [cedula]
        #productoscomprados = []
        #productoscomprados += productoscomprados 
        listaCompraCliente += [productoscomprados]
        registroTienda += [listaCompraCliente]
        productoscomprados = []
    

#---------------------------Ventana de Modificar-------------------------------
def ventanaModificarP():
    ventanaMP= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMP.geometry("400x300")
    ventanaMP.title("Modificar Pasillo")

    codpasillo= Label(ventanaMP, text="Ingrese el cod del pasillo a modificar")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=230, y=10)

    codnombre= Label(ventanaMP, text="Ingrese el nuevo nombre")
    codnombre.place(x=70, y=50)
    cajanombre = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanombre.place(x=230, y=50)
    
    botonAceptar = Button(ventanaMP, text="Aceptar", command=lambda:ModificarPasillo(cajapasillo,cajanombre))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMP, text="Regresar", command=lambda:salirVentana(ventanaMP))
    botonRegresar.place(x=340, y=250)


    
#---------------------------Ventana de Mantenimiento de la base de datos-------------------------------



def ventanaInsert():
    ventanaI = Toplevel()
    ventanaI.geometry("340x340")
    ventanaI.title("Insertar")

    opcion1 = Button(ventanaI , text="Pasillo")
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaI , text="Producto Nuevo")
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaI , text="Marca Nueva")
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaI , text="Inventario")
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaI , text="Registrar Clientes")
    opcion5.place(x=20,y=170)

    opcion6 = Button(ventanaI , text="Registrar Administradores")
    opcion6.place(x=20,y=210)

    opcion7 = Button(ventanaI , text="Registrar Vendedores")
    opcion7.place(x=20,y=250)

    Regresar = Button(ventanaI,text="Regresar", command = lambda:salirVentana(ventanaI))
    Regresar.place(x=20,y=290)

def ventanaEliminar():
    ventanaE = Toplevel()
    ventanaE.geometry("340x340")
    ventanaE.title("Eliminar")

    opcion1 = Button(ventanaE , text="Pasillo")
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaE , text="Producto")
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaE , text="Marca")
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaE , text="Inventario")
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaE , text="Clientes")
    opcion5.place(x=20,y=170)

    opcion6 = Button(ventanaE , text="Administradores")
    opcion6.place(x=20,y=210)

    opcion7 = Button(ventanaE , text="Vendedores")
    opcion7.place(x=20,y=250)

    Regresar = Button(ventanaE,text="Regresar", command = lambda:salirVentana(ventanaE))
    Regresar.place(x=20,y=290)
    
def ventanaModificar():
    ventanaMod = Toplevel()
    ventanaMod.geometry("340x340")
    ventanaMod.title("Modificar")

    opcion1 = Button(ventanaMod , text="Pasillo", command = lambda:ventanaModificarP())
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaMod , text="Producto")
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaMod , text="Marca")
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaMod , text="Inventario")
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaMod , text="Clientes")
    opcion5.place(x=20,y=170)

    opcion6 = Button(ventanaMod , text="Administradores")
    opcion6.place(x=20,y=210)

    opcion7 = Button(ventanaMod , text="Vendedores")
    opcion7.place(x=20,y=250)

    Regresar = Button(ventanaMod,text="Regresar", command = lambda:salirVentana(ventanaMod))
    Regresar.place(x=20,y=290)

def ventanaManteB():
    ventanaMB = Toplevel()
    ventanaMB.geometry("340x340")
    ventanaMB.title("Mantenimiento de base de datos")

    opcion1 = Button(ventanaMB , text="Insertar",command = lambda:ventanaInsert())
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaMB , text="Eliminar",command = lambda:ventanaEliminar())
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaMB , text="Modificar",command = lambda:ventanaModificar())
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaMB , text="Consultar Precio")
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaMB , text="Consultar Descuento")
    opcion5.place(x=20,y=170)

    opcion6 = Button(ventanaMB , text="Modificar el Descuento")
    opcion6.place(x=20,y=210)

    Regresar = Button(ventanaMB,text="Regresar", command = lambda:salirVentana(ventanaMB))
    Regresar.place(x=20,y=250)

#---------------------------Ventana Reportes-------------------------------
def ventanaReportes():
    ventanaRep = Toplevel()
    ventanaRep.geometry("750x700")
    ventanaRep.title("Reportes")

    opcion1 = Button(ventanaRep , text="Pasillo más visitado", command = lambda:PasilloMasVisitado())
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaRep , text="Pasillo menos visitado", command = lambda:PasilloMenosVisitado())
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaRep , text="Productos por pasillo más vendidos", command = lambda:ProductosPorPasilloMasVendido(CodPasillo))
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaRep , text="Marcas más vendidos", command = lambda:MarcasMasVendidas())
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaRep , text="Cliente que más compro", command = lambda:ClienteQueMasCompro())
    opcion5.place(x=20,y=170)

    opcion6 = Button(ventanaRep , text="Cliente que menos compro", command = lambda:ClienteQueMenosCompro())
    opcion6.place(x=20,y=210)

    opcion7 = Button(ventanaRep , text="Producto que más se cargó en las Góndolas", command = lambda:ProductoQueMasSeCargoEnLasGondolas())
    opcion7.place(x=20,y=250)

    opcion8 = Button(ventanaRep , text="Cliente que más facturo", command = lambda:ClienteQueMasFacturo())
    opcion8.place(x=20,y=290)

    opcion9 = Button(ventanaRep , text="Marcas de un producto", command = lambda:MarcasDeUnProducto(CodProducto))
    opcion9.place(x=20,y=330)

    opcion10 = Button(ventanaRep , text="Factura de mayor monto", command = lambda:FacturaDeMayorMonto())
    opcion10.place(x=20,y=370)
    
    opcion11 = Button(ventanaRep , text="Productos de un pasillo", command = lambda:ProductosDeUnPasillo(CodPasillo))
    opcion11.place(x=20,y=410)

    opcion12 = Button(ventanaRep , text="Clientes del supermercado", command = lambda:ClientesDelSupermercado())
    opcion12.place(x=20,y=450)

    opcion13 = Button(ventanaRep , text="Pasillos del supermercado", command = lambda:PasillosDelSupermercado())
    opcion13.place(x=20,y=490)

    opcion14 = Button(ventanaRep , text="Inventario del supermercado", command = lambda:InventarioDelSupermercado())
    opcion14.place(x=20,y=530)

    opcion15 = Button(ventanaRep , text="Últimos dos productos insertados al inventario", command = lambda:UltimosDosProductosInsertadosAlInventario())
    opcion15.place(x=20,y=570)

    opcion16 = Button(ventanaRep , text="Ultimo Producto modificado", command = lambda:ultimoProductoModificado())
    opcion16.place(x=20,y=610)
    
    opcion17 = Button(ventanaRep , text="Promedio de Precios de un producto", command = lambda:PromedioPreciosDeUnProducto())
    opcion17.place(x=20,y=650)

    Regresar = Button(ventanaRep,text="Regresar", command = lambda:salirVentana(ventanaRep))
    Regresar.place(x=20,y=690)


#---------------------------Ventanas Administrador,Cliente R y NR y Vendedor-------------------------------
def ventanaAdmin():
    ventanaAd = Toplevel()
    ventanaAd.geometry("340x340")
    ventanaAd.title("Administrador")

    opcion1 = Button(ventanaAd , text="Mantenimiento de la Base de Datos", command = lambda:ventanaManteB())
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaAd , text="Facturar",command=lambda: facturar())
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaAd , text="Revisar gondolas")
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaAd , text="Verificar inventario")
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaAd , text="Reportes", command= lambda:ventanaReportes())
    opcion5.place(x=20,y=170)

    Regresar = Button(ventanaAd,text="Regresar", command = lambda:salirVentana(ventanaAd))
    Regresar.place(x=20,y=210)

def ventanaClienR():
    ventanaCr = Toplevel()
    ventanaCr.geometry("340x340")
    ventanaCr.title("Cliente Registrado")

    opcion1 = Button(ventanaCr , text="Consultar Precio")
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaCr , text="Consultar Descuento")
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaCr, text="Consultar Productos")
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaCr , text="Comprar",command= lambda:ventanaComprar())
    opcion4.place(x=20,y=130)

    Regresar = Button(ventanaCr,text="Regresar", command = lambda:salirVentana(ventanaCr))
    Regresar.place(x=20,y=170)


#---------------------------------------------Ventana de Comprar-----------------------------------------------------------


#cargar las imagenes
    #imagen1=PhotoImage(file="imagenes del proyecto/arroz.png")
    #imagen_sub=imagen1.subsample(3)
    #lbl_imagen1=Label(ventanaCm, image=imagen_sub).place(x=100,y=100)
    
    #lbl_imagen1.place(x=100,y=100)
botones = []
def ventanaComprar():
    global botones
    ventanaCm=  Toplevel()
    
    ventanaCm.geometry("700x700")
    ventanaCm.config(bg="sky blue")
    ventanaCm.title("Comprar")

    contadorx = 0
    contadory = 150
    contador = 0
    for i in pasillos:
        
        boton = Button(ventanaCm, text=i[0]+":"+i[1])
        boton.place(x=contadorx,y=contadory)
        botones += [boton]
        
        
        contadory += 30
        if contadory >= 750:
            contadory = 150
            contadorx += 50
        contador+= 1
    codPasillo= Label(ventanaCm, text="Seleccione el pasillo")
    codPasillo.place(x=20, y=40)
    
    combo = ttk.Combobox(ventanaCm,values=pasillos,state="readonly")
    combo.place(x=20, y=60)
    
    Aceptar=Button(ventanaCm,text="Aceptar", command= lambda:ventanaProductos(combo.get()))
    Aceptar.place(x=20,y=80)
    
    #for i in botones:
    #    i.config( command= lambda:ventanaProductos(i))
    
    finalizarCompra=Button(ventanaCm,text="Finalizar Compra", command= lambda:Comprar(cedulaActual))
    finalizarCompra.place(x=20,y=650)
    
    Regresar=Button(ventanaCm,text="Regresar", command= lambda:ventanaProductos(ventanaCm))
    Regresar.place(x=620,y=650)
    
    ventanaCm.mainloop()
    
def ventanaProductos(pasillo):
    
    print("***")
    pasillo = pasillo.split(" ")[0]
    print(pasillo)
    ventanaCm=  Toplevel()
    
    ventanaCm.geometry("700x700")
    ventanaCm.config(bg="sky blue")
    ventanaCm.title("Productos")

    contadorx = 0
    contadory = 150
    listaProductosdisponles = []
    for i in productosPasillo:
        
        if i[0] == pasillo:
            print("imagenes del proyecto/"+i[2]+".png")
            
            if (i[2] == "Arroz"):
                imagen1=PhotoImage(file="imagenes del proyecto/"+"Arroz"+".png")
                imagen_sub=imagen1.subsample(3)    
            
                boton = Button(ventanaCm, text=i[2],image=imagen_sub)
                boton.place(x=contadorx,y=contadory)
            elif (i[2] == "Frijoles"):
                imagen2=PhotoImage(file="imagenes del proyecto/"+"Frijoles"+".png")
                imagen_sub2=imagen2.subsample(3)    
            
                boton2 = Button(ventanaCm, text=i[2],image=imagen_sub2)
                boton2.place(x=contadorx,y=contadory)
                
            contadory += 200
            listaProductosdisponles += [i]
            if contadory >= 750:
                contadory = 150
                contadorx += 50

    
    codPasillo= Label(ventanaCm, text="Seleccione el producto")
    codPasillo.place(x=20, y=40)
    
    combo = ttk.Combobox(ventanaCm,values=listaProductosdisponles,state="readonly")
    combo.place(x=20, y=60)
    
    Aceptar=Button(ventanaCm,text="Aceptar", command= lambda:ventanaMarcas(pasillo,combo.get()))
    Aceptar.place(x=20,y=80)
    
    
    Regresar=Button(ventanaCm,text="Regresar", command= lambda:salirVentana(ventanaCm))
    Regresar.place(x=620,y=650)
    finalizarCompra=Button(ventanaCm,text="Finalizar Compra", command= lambda:Comprar(cedulaActual))
    finalizarCompra.place(x=20,y=650)
    
    ventanaCm.mainloop()    

def ventanaMarcas(pasillo,producto):
    ventanaCm=  Toplevel()
    producto = producto.split(" ")[1]
    
    ventanaCm.geometry("700x700")
    ventanaCm.config(bg="sky blue")
    ventanaCm.title("Marcas")

    contadorx = 0
    contadory = 150
    listamarcasDiponibles = []
    for i in marcasProductos:
        if i[0] == pasillo:
            if i[1] == producto:
                boton = Button(ventanaCm, text=i[3])
                boton.place(x=contadorx,y=contadory)
                contadory += 30
                listamarcasDiponibles += [i]
                if contadory >= 750:
                    contadory = 150
                    contadorx += 50
    codPasillo= Label(ventanaCm, text="Seleccione la marca")
    codPasillo.place(x=20, y=40)
    
    combo = ttk.Combobox(ventanaCm,values=listamarcasDiponibles,state="readonly")
    combo.place(x=20, y=60)
    
    Aceptar=Button(ventanaCm,text="Aceptar",command= lambda:FinalizarCompra(pasillo,producto,combo.get()))
    Aceptar.place(x=20,y=80)

    
    Regresar=Button(ventanaCm,text="Regresar", command= lambda:salirVentana(ventanaCm))
    Regresar.place(x=620,y=650)
    finalizarCompra=Button(ventanaCm,text="Finalizar Compra", command= lambda:Comprar(cedulaActual))
    finalizarCompra.place(x=20,y=650)
    
    ventanaCm.mainloop()
    
    
def FinalizarCompra(pasillo,producto,marca):
    ventanaCm=  Toplevel()
    info = marca.split(" ")
    marca = marca.split(" ")[2]
    
    ventanaCm.geometry("700x700")
    ventanaCm.config(bg="sky blue")
    ventanaCm.title("Marcas")

    
    codPasillo= Label(ventanaCm, text="Seleccione la cantidad")
    codPasillo.place(x=20, y=40)
    precio= Label(ventanaCm, text="Cada unidad cuesta = "+ info[5])
    precio.place(x=20, y=60)
    spin_temp = ttk.Spinbox(ventanaCm,from_=0, to=int(info[4]),state="readonly")
    spin_temp.place(x=20, y=80, width=70)
    
    Aceptar=Button(ventanaCm,text="Aceptar",command= lambda:comprando(pasillo,producto,marca,spin_temp.get()))
    Aceptar.place(x=20,y=100)

    
    Regresar=Button(ventanaCm,text="Regresar", command= lambda:salirVentana(ventanaCm))
    Regresar.place(x=620,y=650)
    
    finalizarCompra=Button(ventanaCm,text="Finalizar Compra", command= lambda:Comprar(cedulaActual))
    finalizarCompra.place(x=20,y=650)
    
    ventanaCm.mainloop()







def ventanaClienNR():
    ventanaCnr = Toplevel()
    ventanaCnr.geometry("340x340")
    ventanaCnr.title("Cliente No Registrado")

    opcion1 = Button(ventanaCnr , text="Consultar Precio")
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaCnr , text="Consultar Descuento",fg = "grey")
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaCnr, text="Consultar Productos")
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaCnr , text="Comprar",fg = "grey")
    opcion4.place(x=20,y=130)

    Regresar = Button(ventanaCnr,text="Regresar", command = lambda:salirVentana(ventanaCnr))
    Regresar.place(x=20,y=170)



def ventanaVende():
    ventanaV = Toplevel()
    ventanaV.geometry("340x340")
    ventanaV.title("Vendedor")

    opcion1 = Button(ventanaV , text="Consultar Precio")
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaV , text="Consultar Descuento de un cliente")
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaV, text="Consultar Productos de un pasillo")
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaV , text="Consultar Marcas de un producto")
    opcion4.place(x=20,y=130)

    Regresar = Button(ventanaV,text="Regresar", command = lambda:salirVentana(ventanaV))
    Regresar.place(x=20,y=170)
    

#---------------------------Verificacion de codigo-----------------------------------------------------    
def verificaAdministrador(codigo):#Hace la verifiacion del codigo de administrador
        CA=codigo.get()
        if buscaEnLista(Administradores,CA,0) != -1:
            ventanaAdmin()
        else:
            return messagebox.showinfo("Error en el codigo de administrador","El Codigo ingresado no existe")
            #Regresa mensaje de error
        
def verificaCliente(codigo1):#Hace la verifiacion del codigo de cliente
        global cedulaActual
        CC=codigo1.get()
        if buscaEnLista(clientes,CC,0) != -1:
            cedulaActual = CC
            ventanaClienR()
        else:
            ventanaClienNR()
    
######################################################

def salirVentana(ventana):#Sale de la ventana
    ventana.destroy()

def ventanaVA():
    ventanaVA= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaVA.geometry("400x300")
    ventanaVA.title("Aministrador")

    codadmi= Label(ventanaVA, text="ingrese el cod administrador")
    codadmi.place(x=30, y=10)
    cajaadmi = Entry(ventanaVA) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaadmi.place(x=220, y=10)
    
    botonAceptar = Button(ventanaVA, text="Aceptar", command=lambda:verificaAdministrador(cajaadmi))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaVA, text="Regresar", command=lambda:salirVentana(ventanaVA))
    botonRegresar.place(x=340, y=250)
    
def ventanaVC():
    ventanaVC= Toplevel() #Crea otra ventana aparte de la principal para verificar cliente
    ventanaVC.geometry("400x300")
    ventanaVC.title("Cliente")

    codcli= Label(ventanaVC, text="ingrese el cod cliente")
    codcli.place(x=30, y=10)
    cajacli = Entry(ventanaVC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacli.place(x=220, y=10)
    
    botonAceptar = Button(ventanaVC, text="Aceptar", command=lambda:verificaCliente(cajacli))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaVC, text="Regresar", command=lambda:salirVentana(ventanaVC))
    botonRegresar.place(x=340, y=250)
            



#---------------------------Menú principal-----------------------------------------------------
menu = Tk() 
menu.title("Sistema de Punto y Venta")
menu.geometry("300x300")

adminbttn = Button(menu,text="Administrador",command = lambda:ventanaVA())#Boton administrador
adminbttn.place(x=20,y=10)

clientebttn = Button(menu,text="Cliente",command = lambda:ventanaVC())#Boton Cliente
clientebttn.place(x=20,y=50)

vendedorbttn = Button(menu,text="Vendedor",command = lambda:ventanaVende())#Boton vendedor
vendedorbttn.place(x=20,y=90)

salirbttn = Button(menu,text="Salir", command = lambda:salirVentana(menu))#Boton para salir del menu
salirbttn.place(x=20,y=250)

menu.mainloop()




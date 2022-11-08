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
    CDP=CodPasillo.get()
    Nom=Nombre.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    if not(verificaNumero(CDP)):
        return messagebox.showinfo("Error")
    elif (listaCodigoPasillo)!=[]:
        return messagebox.showinfo("Error")
    else:
        nuevoPasillo = [CDP,Nom]
        pasillos += [nuevoPasillo]
        ventanaPasillosMod()
        
#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto existe   
def Productonuevo(CodPasillo,CodProducto,Nombre):
    global pasillos,productosPasillo
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    Nom=Nombre.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CDP,1)
    if not(verificaNumero(CDP)):
        return messagebox.showinfo("Error")
    elif (listaCodigoPasillo)==[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(CPR)):
        return messagebox.showinfo("Error")
    elif (listaCodigoProducto)!=[]:
        return messagebox.showinfo("Error")
    else:
        nuevoProducto = [CDP,CPR,Nom]
        productosPasillo += [nuevoProducto]
        ventanaProductosMod()
    
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
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    CDM=CodMarca.get()
    Nom=Nombre.get()
    Cant=CantidadGondola.get()
    Prec=Precio.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CPR,1)
    listaCodigoMarcas=buscaEnLista2(marcasProductos,CDM,2)
                
                
    if not(verificaNumero(CDP)):
        return messagebox.showinfo("Error")
    elif (listaCodigoPasillo)==[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(CPR)):
        return messagebox.showinfo("Error")
    elif (listaCodigoProducto)==[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(CDM)):
        return messagebox.showinfo("Error")
    elif (listaCodigoMarcas)!=[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(Cant)):
        return -7
    elif not(verificaNumero(Prec)):
       return messagebox.showinfo("Error")
    else:
        nuevaMarca = [CDP,CPR,CDM,Nom,Cant,Prec]
        marcasProductos += [nuevaMarca]
        ventanaMarcaMod()

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
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    CDM=CodMarca.get()
    Nom=Nombre.get()
    Cant=CantidadStock.get()
    Codc=CodigoCanasta.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CPR,1)
    listaCodigoInventario=buscaEnLista2(inventarios,CDM,2)
                
                
    if not(verificaNumero(CDP)):
        return messagebox.showinfo("Error")
    elif (listaCodigoPasillo)==[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(CPR)):
        return messagebox.showinfo("Error")
    elif (listaCodigoProducto)==[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(CDM)):
        return messagebox.showinfo("Error")
    elif (listaCodigoInventario)!=[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(Cant)):
        return messagebox.showinfo("Error")
    elif not(Codc in ["0","1"]):
        return messagebox.showinfo("Error")
    else:
        nuevaMarca = [CDP,CPR,CDM,Nom,Cant,Codc]
        inventarios += [nuevaMarca]
        ultimo = [CDP,CPR,CDM]
        ultimosDosProductosInsertado += ultimo
        if len(ultimosDosProductosInsertado) > 2:
            ultimosDosProductosInsertado = ultimosDosProductosInsertado[-2]
        ventanaInMod()

#Retorna -1 si la cedula existe
#Retorna -2 la cedula no es un numero    
def RegistrarClientes(Cedula,Nombre,Telefono,Correo):
    global clientes
    Ced=Cedula.get()
    Nom=Nombre.get()
    Tel=Telefono.get()
    Cor=Correo.get()
    listaCedula=buscaEnLista2(clientes,Ced,0)
    if not(verificaNumero(Ced)):
       return messagebox.showinfo("Error")
    elif (listaCedula)!=[]:
       return messagebox.showinfo("Error")
    else:
        nuevoCliente = [Ced,Nom,Tel,Cor]
        clientes += [nuevoCliente]
        ventanaCMod()
        
#Retorna -1 si el codigo adminstrador existe
#Retorna -2 el codigo adminstrador no es un numero      
def RegistrarAdministradores(CodAdministrador,Nombre):
    global Administradores
    Cod=CodAdministrador.get()
    Nom=Nombre.get()
    listaCodigoAdministrador=buscaEnLista2(Administradores,Cod,0)
    if not(verificaNumero(Cod)):
        return messagebox.showinfo("Error")
    elif (listaCodigoAdministrador)!=[]:
        return messagebox.showinfo("Error")
    else:
        nuevoAdministrador = [Cod,Nom]
        Administradores += [nuevoAdministrador]
        ventanaAMod()
    
#Retorna -1 si el codigo vendedor existe
#Retorna -2 el codigo vendedor no es un numero   
def RegistrarVendedores(CodVendedor,Nombre):
    global Vendedores
    Cod=CodVendedor.get()
    Nom=Nombre.get()
    listaCodigoVendedorr=buscaEnLista2(Vendedores,Cod,0)
    if not(verificaNumero(Cod)):
        return messagebox.showinfo("Error")
    elif (listaCodigoVendedorr)!=[]:
        return messagebox.showinfo("Error")
    else:
        nuevoVendedor = [Cod,Nom]
        Vendedores += [nuevoVendedor]
        ventanaVMod()
    
#############
##ParaEliminar

#Retorna -1 si no exite pasiilo con esas datos

def EliminarPasillo(CodPasillo,Nombre):
    global pasillos
    CDP=CodPasillo.get()
    Nom=Nombre.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    listaCodigoPasilloFila=Hagalista(pasillos,CDP,0)
    result = -1
    i = 0
    for n in listaCodigoPasilloFila:
        if (n == [CDP,Nom]):
            pasillos.pop(listaCodigoPasillo[i])
            result = [CDP,Nom]
        i += 1
    if result != -1:
        listaCodigoProducto=buscaEnLista2(productosPasillo,CDP,0)
        for j in listaCodigoProducto:
            productosPasillo.pop(j)
        listaCodigoMarcas=buscaEnLista2(marcasProductos,CDP,0)
        for m in listaCodigoMarcas:
            marcasProductos.pop(m)
        listaCodigoInventario=buscaEnLista2(inventarios,CDP,0)
        for k in listaCodigoInventario:
            inventarios.pop(k)
    ventanaPasillosMod()
    

#Retorna -1 si no exite producto con esas datos   
def EliminarProducto (CodPasillo,CodProducto,Nombre):
    global pasillos,productosPasillo
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    Nom=Nombre.get()
    listaCodigoProducto=buscaEnLista2(productosPasillo,CPR,1)
    listaCodigoProductoFila=Hagalista(productosPasillo,CPR,1)
    result = -1
    i = 0
    for n in listaCodigoProductoFila:
        if (n == [CDP,CPR,Nom]):
            productosPasillo.pop(listaCodigoProducto[i])
            result = [CDP,CPRo,Nom]
        i += 1
    if result != -1:
        
        listaCodigoMarcas=buscaEnLista2(marcasProductos,CPR,1)
        for m in listaCodigoMarcas:
            marcasProductos.pop(m)
        listaCodigoInventario=buscaEnLista2(inventarios,CPR,1)
        for k in listaCodigoInventario:
            inventarios.pop(k)
    ventanaProductosMod()

#Retorna -1 si  marca no existe
def EliminarMarca (CodPasillo,CodProducto,CodMarca,Nombre,CantidadGondola,Precio):
    global pasillos,productosPasillo,marcasProductos
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    CDM=CodMarca.get()
    Nom=Nombre.get()
    Cant=CantidadGondola.get()
    Prec=Precio.get()
    listaCodigoMarca=buscaEnLista2(marcasProductos,CDM,2)
    listaCodigoMarcaFila=Hagalista(marcasProductos,CDM,2)
    result = -1
    i = 0
    for n in listaCodigoMarcaFila:
        if (n == [CDP,CPR,CDM,Nom,Cant,Prec]):
            marcasProductos.pop(listaCodigoMarca[i])
            result = [CDP,CPR,CDM,Nom,Cant,Prec]
        i += 1
    if result != -1:
        listaCodigoInventario=buscaEnLista2(inventarios,CDM,2)
        for k in listaCodigoInventario:
            inventarios.pop(k)
    ventanaMarcaMod()

#Retorna -1 si  marca no existe
def EliminarInventario(CodPasillo,CodProducto,CodMarca,Nombre,CantidadStock,CodigoCanasta):
    global pasillos,productosPasillo,inventarios
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    CDM=CodMarca.get()
    Nom=Nombre.get()
    Cant=CantidadStock.get()
    Codc=CodigoCanasta.get()
    listaCodigoMarca=buscaEnLista2(inventarios,CDM,2)
    listaCodigoMarcaFila=Hagalista(inventarios,CDM,2)
    result = -1
    i = 0
    for n in listaCodigoMarcaFila:
        if (n == [CDP,CPR,CDM,Nom,Cant,Codc]):
            inventarios.pop(listaCodigoMarca[i])
            result = [CDP,CPR,CDM,Nom,Cant,Codc]
        i += 1
    if result != -1:
        listaCodigoInventario=buscaEnLista2(marcasProductos,CDM,2)
        for k in listaCodigoInventario:
            marcasProductos.pop(k)
    ventanaInMod()

#Retorna -1 si  cecula no existe
def EliminarClientes(Cedula,Nombre,Telefono,Correo):
    global clientes
    Ced=Cedula.get()
    Nom=Nombre.get()
    Tel=Telefono.get()
    Cor=Correo.get()
    listaCodigoCedula=buscaEnLista2(clientes,Ced,0)
    listaCodigoCedulaFila=Hagalista(clientes,Ced,0)
    result = -1
    i = 0
    for n in listaCodigoCedulaFila:
        if (n == [Ced,Nom,Tel,Cor]):
            clientes.pop(listaCodigoCedula[i])
            result = [Ced,Nom,Tel,Cor]
        i += 1
        ventanaCMod()
#Retorna -1 si  codigo administrador no existe
def EliminarAdministradores(CodAdministrador,Nombre):
    global Administradores
    Cod=CodAdministrador.get()
    Nom=Nombre.get()
    listaCodigoCodAdmin=buscaEnLista2(Administradores,Cod,0)
    listaCodigoCodAdminFila=Hagalista(Administradores,Cod,0)
    result = -1
    i = 0
    for n in listaCodigoCodAdminFila:
        if (n == [Cod,Nom]):
            Administradores.pop(listaCodigoCodAdmin[i])
            result = [Cod,Nom]
        i += 1
    
    ventanaAMod()
   
#Retorna -1 si  codigo vendedor no existe 
def EliminarVendedores(CodVendedor,Nombre):
    global Vendedores
    Cod=CodVendedor.get()
    Nom=Nombre.get()
    listaCodigoCodVendedor=buscaEnLista2(Vendedores,Cod,0)
    listaCodigoCodVendedorFila=Hagalista(Vendedores,Cod,0)
    result = -1
    i = 0
    for n in listaCodigoCodVendedorFila:
        if (n == [Cod,Nom]):
            Vendedores.pop(listaCodigoCodVendedor[i])
            result = [Cod,Nom]
        i += 1
    
    ventanaVMod()
##################
#Para Modificar

#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero   

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
        ventanaPasillosMod()
        
    
#Retorna -1 si el codigo de pasillo no existe
#Retorna -2 si el codigo pasiilo no es un numero 
#Retorna -4 si el codigo de producto no es un numero
#Retorna -3 si el codigo de producto no existe   
def ModificarProducto(CodPasillo,CodProducto,Nombre):
    global pasillos,productosPasillo,ultimoProductoModificado
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    Nom=Nombre.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CPR,1)
    if not(verificaNumero(CDP)):
        return messagebox.showinfo("Error en el codigo de pasillo","El Codigo ingresado no existe")
    elif (listaCodigoPasillo)==[]:
        return messagebox.showinfo("Error en el codigo de pasillo","El Codigo ingresado no existe")
    elif not(verificaNumero(CPR)):
        return messagebox.showinfo("Error en el codigo de producto","El Codigo ingresado no existe")
    elif (listaCodigoProducto)==[]:
        return messagebox.showinfo("Error en el codigo de producto","El Codigo ingresado no existe")
    else:
        nuevoProducto = [CDP,CPR,Nom]
        productosPasillo[listaCodigoProducto[0]] = nuevoProducto
        ultimoProductoModificado = nuevoProducto
        ventanaProductosMod()

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
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    CDM=CodMarca.get()
    Nom=Nombre.get()
    Cant=CantidadGondola.get()
    Prec=Precio.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CPR,1)
    listaCodigoMarcas=buscaEnLista2(marcasProductos,CDM,2)
    if not(verificaNumero(CDP)):
        return messagebox.showinfo("Error en el codigo de pasillo","El Codigo ingresado no existe")
    elif (listaCodigoPasillo)==[]:
        return messagebox.showinfo("Error en el codigo de pasillo","El Codigo ingresado no existe")
    elif not(verificaNumero(CPR)):
        return messagebox.showinfo("Error en el codigo de producto","El Codigo ingresado no existe")
    elif (listaCodigoProducto)==[]:
        return messagebox.showinfo("Error en el codigo de producto","El Codigo ingresado no existe")
    elif not(verificaNumero(CDM)):
        return messagebox.showinfo("Error en el codigo de marca","El Codigo ingresado no existe")
    elif (listaCodigoMarcas)==[]:
        return messagebox.showinfo("Error en el codigo de marca","El Codigo ingresado no existe")
    elif not(verificaNumero(Cant)):
        return messagebox.showinfo("Error en la gondola","Cantidad erronea")
    elif not(verificaNumero(Prec)):
        return messagebox.showinfo("Error en la gondola","Cantidad erronea")
    else:
        nuevaMarca = [CDP,CPR,CDM,Nom,Cant,Prec]
        marcasProductos[listaCodigoMarcas[0]] = nuevaMarca
        ventanaMarcaMod()

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
    CDP=CodPasillo.get()
    CPR=CodProducto.get()
    CDM=CodMarca.get()
    Nom=Nombre.get()
    Cant=CantidadStock.get()
    Codc=CodigoCanasta.get()
    listaCodigoPasillo=buscaEnLista2(pasillos,CDP,0)
    listaCodigoProducto=buscaEnLista2(productosPasillo,CPR,1)
    listaCodigoInventario=buscaEnLista2(inventarios,CDM,2)
                
                
    if not(verificaNumero(CDP)):
        return messagebox.showinfo("Error")
    elif (listaCodigoPasillo)==[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(CPR)):
        return messagebox.showinfo("Error")
    elif (listaCodigoProducto)==[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(CDM)):
        return messagebox.showinfo("Error")
    elif (listaCodigoInventario)==[]:
        return messagebox.showinfo("Error")
    elif not(verificaNumero(Cant)):
        return messagebox.showinfo("Error")
    elif not(Codc in ["0","1"]):
        return messagebox.showinfo("Error")
    else:
        nuevaMarca = [CDP,CPR,CDM,Nom,Cant,Codc]
        inventarios[listaCodigoInventario[0]] = nuevaMarca
        ventanaInMod()

#Retorna -1 si la cedula no existe
#Retorna -2 la cedula no es un numero    
def ModificarClientes(Cedula,Nombre,Telefono,Correo):
    global clientes
    Ced=Cedula.get()
    Nom=Nombre.get()
    Tel=Telefono.get()
    Cor=Correo.get()
    listaCedula=buscaEnLista2(clientes,Ced,0)
    if not(verificaNumero(Ced)):
        return messagebox.showinfo("Error")
    elif (listaCedula)==[]:
        return messagebox.showinfo("Error")
    else:
        nuevoCliente = [Ced,Nom,Tel,Cor]
        clientes[listaCedula[0]] = nuevoCliente
        ventanaCMod()
        
#Retorna -1 si el codigo adminstrador si existe
#Retorna -2 el codigo adminstrador no es un numero      
def ModificarAdministradores(CodAdministrador,Nombre):
    global Administradores
    Cod=CodAdministrador.get()
    Nom=Nombre.get()
    listaCodigoAdministrador=buscaEnLista2(Administradores,Cod,0)
    if not(verificaNumero(Cod)):
        return messagebox.showinfo("Error")
    elif (listaCodigoAdministrador)==[]:
        return messagebox.showinfo("Error") 
    else:
        nuevoAdministrador = [Cod,Nom]
        Administradores[listaCodigoAdministrador[0]] = nuevoAdministrador
        ventanaAMod()
    
#Retorna -1 si el codigo vendedor no existe
#Retorna -2 el codigo vendedor no es un numero   
def ModificarVendedores(CodVendedor,Nombre):
    global Vendedores
    Cod=CodVendedor.get()
    Nom=Nombre.get()
    listaCodigoVendedor=buscaEnLista2(Vendedores,Cod,0)
    if not(verificaNumero(Cod)):
        return messagebox.showinfo("Error")
    elif (listaCodigoVendedorr)==[]:
        return messagebox.showinfo("Error")
    else:
        nuevoVendedor = [Cod,Nom]
        Vendedores[listaCodigoVendedorr[0]] = nuevoVendedor
        ventanaVMod()

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
        return messagebox.showinfo("Error en el reporte","No se ha echo nada")
    else:
        return messagebox.showinfo("Pasillo mas visitado",moda(pasillosComprados))
#2.Pasillo menos visitado
#Retorna -1 si no se ha facturador nada
def PasilloMenosVisitado():
    if RegistroTodasCompras==[]:
        return messagebox.showinfo("Error en el reporte","No se ha echo nada")
    else:
         return messagebox.showinfo("Pasillo menos visitado",modaInversa(pasillosComprados))

#3.Productos por pasillo mas vendido
#Retorna -1 si no se ha facturador nada
#Retorna -2 si no existe el pasillo
def ProductosPorPasilloMasVendido(CodPasillo):
    global pasillos
    Cod=CodPasillo.get()
    if RegistroTodasCompras==[]:
        return messagebox.showinfo("Error en el reporte")
    elif buscaEnLista(pasillos,Cod,0)== -1:
        return messagebox.showinfo("Error en el reporte")
    else:
        return messagebox.showinfo("Producto Pasillo mas vendido",(moda(Hagalista(PasilloProductosComprados,Cod,0))))
        
#4.Marcas mas vendidas
#Retorna -1 si no se ha facturador nada
def MarcasMasVendidas():
    if RegistroTodasCompras==[]:
        return messagebox.showinfo("Error en el reporte","No se ha echo nada")
    else:
        return messagebox.showinfo("Marca mas vendida",moda(MarcasCompradas))
    
#5.Cliente que mas compro
#Retorna -1 si no se ha facturador nada
def ClienteQueMasCompro():
    if RegistroTodasCompras==[]:
        return messagebox.showinfo("Error en el reporte","No se ha echo nada")
    else:
        return messagebox.showinfo("Cliente que mas compro",ClientesMontoComprados)
    
#6.Cliente que menos compro
#Retorna -1 si no se ha facturador nada
    
def ClienteQueMenosCompro():
    if RegistroTodasCompras==[]:
        return messagebox.showinfo("Error en el reporte","No se ha echo nada")
    else:
        return messagebox.showinfo("Cliente que menos compro",montosFactutadosmenos(ClientesMontoComprados))

#7.Producto que mas se cargo en las Gondolas
def ProductoQueMasSeCargoEnLasGondolas():
    return messagebox.showinfo("Producto mas cargado",montosFactutados(ProductoCantidaCargados))

#8.Cliente que mas facturo
#Retorna -1 si no se ha facturador nada
def ClienteQueMasFacturo():
    if RegistroTodasCompras==[]:
        return messagebox.showinfo("Error en el reporte","No se ha echo nada")
    else:
        return messagebox.showinfo("Cliente que mas facturo",moda(ClientesFacturados))
    
#9.Marcas de un producto
#Retorna -1 si no se ha facturador nada
#Retorna -2 si no existe el producto
    
def MarcasDeUnProducto(CodProducto):
    global productosPasillo
    global marcasProductos
    Cod=CodProducto.get()
    if RegistroTodasCompras==[]:
         return messagebox.showinfo("Error en el reporte")
    elif buscaEnLista(productosPasillo,Cod,1)== -1:
         return messagebox.showinfo("Error en el reporte")
    else:
        return messagebox.showinfo("Marcas de un producto",(Hagalista(marcasProductos,Cod,1))
    
#10.Factura de mayor monto
#Retorna -1 si no se ha facturador nada
    
def FacturaDeMayorMonto():
    if RegistroTodasCompras==[]:
        return messagebox.showinfo("Error en el reporte","No se ha echo nada")
    else:
       return messagebox.showinfo("Factura de mayor monto",montosFactutados(FacturaMontoRealizadas))
        
#11.Productos de un pasillo
#Retorna -1 si el pasillo no existe
def ProductosDeUnPasillo(CodPasillo):
    global pasillos
    global productosPasillo
    Cod=CodPasillo.get()
    if buscaEnLista(pasillos,Cod,0)== -1:
        return messagebox.showinfo("Error en el reporte")
    else:
       eturn messagebox.showinfo("Productos de un pasillo",((Hagalista(productosPasillo,Cod,0)))
    
#12.Clientes del supermercado
def ClientesDelSupermercado():
    ventanaRepClientes()        
#13.Pasillos del supermercado
def PasillosDelSupermercado():
    ventanaRepPasillos()
#14.Inventario del supermercado
def InventarioDelSupermercado():
    ventanaRepInventario()

#15.UltimosDosProductosInsertadosAlInventario
def UltimosDosProductosInsertadosAlInventario():
    return messagebox.showinfo("UltimosDosProductos",ultimosDosProductosInsertado)

#16.ultimoProductoModificado
def ultimoProductoModificado():
    return messagebox.showinfo("ultimoProductoModificado",ultimoProductoModificado)

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
    return messagebox.showinfo("Promedio precios",result)
        



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
#---------------------------Ventana Mostrar Info Final Modicar-------------------------------
def ventanaPasillosMod():
    ventanaPasM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaPasM.geometry("700x700")

    listaPasillos = pasillos #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listaPasillos) #Num de filas
    total_Columnas = len(listaPasillos[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            Pas = Entry(ventanaPasM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            Pas.grid(row=i, column=j) #Coloca en la ventana
            Pas.insert(END, listaPasillos[i][j]) #Inserta la información
    botonRegresar = Button(ventanaPasM, text="Regresar", command=lambda:salirVentana(ventanaPasM))
    botonRegresar.place(x=340, y=250)

def ventanaProductosMod():
    ventanaProM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaProM.geometry("700x700")

    listaproductos = productosPasillo #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listaproductos)-1 #Num de filas
    total_Columnas = len(listaproductos[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            Pro = Entry(ventanaProM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            Pro.grid(row=i, column=j) #Coloca en la ventana
            Pro.insert(END, listaproductos[i][j]) #Inserta la información
    botonRegresar = Button(ventanaProM, text="Regresar", command=lambda:salirVentana(ventanaProM))
    botonRegresar.place(x=340, y=350)

def ventanaMarcaMod():
    ventanaMarM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaMarM.geometry("700x700")

    listamarca = marcasProductos #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listamarca)-1 #Num de filas
    total_Columnas = len(listamarca[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            Mar = Entry(ventanaMarM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            Mar.grid(row=i, column=j) #Coloca en la ventana
            Mar.insert(END, listamarca[i][j]) #Inserta la información
    botonRegresar = Button(ventanaMarM, text="Regresar", command=lambda:salirVentana(ventanaMarM))
    botonRegresar.place(x=540, y=550)

def ventanaInMod():
    ventanaInM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaInM.geometry("700x700")

    listainve = inventarios #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listainve)-1 #Num de filas
    total_Columnas = len(listainve[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            Inv = Entry(ventanaInM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            Inv.grid(row=i, column=j) #Coloca en la ventana
            Inv.insert(END, listainve[i][j]) #Inserta la información
    botonRegresar = Button(ventanaInM, text="Regresar", command=lambda:salirVentana(ventanaInM))
    botonRegresar.place(x=540, y=550)

def ventanaCMod():
    ventanaCM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaCM.geometry("700x700")

    listaC = clientes #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listaC)-1 #Num de filas
    total_Columnas = len(listaC[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            C = Entry(ventanaCM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            C.grid(row=i, column=j) #Coloca en la ventana
            C.insert(END, listaC[i][j]) #Inserta la información
    botonRegresar = Button(ventanaCM, text="Regresar", command=lambda:salirVentana(ventanaCM))
    botonRegresar.place(x=540, y=550)

def ventanaAMod():
    ventanaAM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaAM.geometry("700x700")

    listaA = Administradores #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listaA) #Num de filas
    total_Columnas = len(listaA[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            A = Entry(ventanaAM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            A.grid(row=i, column=j) #Coloca en la ventana
            A.insert(END, listaA[i][j]) #Inserta la información
    botonRegresar = Button(ventanaAM, text="Regresar", command=lambda:salirVentana(ventanaAM))
    botonRegresar.place(x=540, y=550)

def ventanaVMod():
    ventanaVM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaVM.geometry("700x700")

    listaV = Vendedores #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listaV) #Num de filas
    total_Columnas = len(listaV[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            V = Entry(ventanaVM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            V.grid(row=i, column=j) #Coloca en la ventana
            V.insert(END, listaV[i][j]) #Inserta la información
    botonRegresar = Button(ventanaVM, text="Regresar", command=lambda:salirVentana(ventanaVM))
    botonRegresar.place(x=540, y=550)


#---------------------------Ventana Mostrar Info Final Modicar-------------------------------   
    
def ventanaRepClientes():
    ventanaRepC = Toplevel() #Crea otra ventana aparte de la principal
    ventanaRepC.geometry("700x700")

    Clientes = clientes #Devuelve la lista de Clientes, llama la función
    total_Filas = len(Clientes) #Num de filas
    total_Columnas = len(Clientes[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            ReC = Entry(ventanaRepC, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            ReC.grid(row=i, column=j) #Coloca en la ventana
            ReC.insert(END, Clientes[i][j]) #Inserta la información
    botonRegresar = Button(ventanaRepC, text="Regresar", command=lambda:salirVentana(ventanaRepC))
    botonRegresar.place(x=340, y=250)

def ventanaRepInventario():
    ventanaInM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaInM.geometry("700x700")

    listainve = inventarios #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listainve)-1 #Num de filas
    total_Columnas = len(listainve[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            Inv = Entry(ventanaInM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            Inv.grid(row=i, column=j) #Coloca en la ventana
            Inv.insert(END, listainve[i][j]) #Inserta la información
    botonRegresar = Button(ventanaInM, text="Regresar", command=lambda:salirVentana(ventanaInM))
    botonRegresar.place(x=540, y=550)

def ventanaRepPasillos():
    ventanaPasM = Toplevel() #Crea otra ventana aparte de la principal
    ventanaPasM.geometry("700x700")

    listaPasillos = pasillos #Devuelve la lista de Clientes, llama la función
    total_Filas = len(listaPasillos) #Num de filas
    total_Columnas = len(listaPasillos[0]) #Num columnas

    #---Crear la tabla------
    for i in range(total_Filas):
        for j in range(total_Columnas):
            Pas = Entry(ventanaPasM, width=20)
                             #fg='black',
                             #font=('Arial', 12, 'bold')) #Crea la entrada, el textbox
            Pas.grid(row=i, column=j) #Coloca en la ventana
            Pas.insert(END, listaPasillos[i][j]) #Inserta la información
    botonRegresar = Button(ventanaPasM, text="Regresar", command=lambda:salirVentana(ventanaPasM))
    botonRegresar.place(x=340, y=250)

def ventanaRepProductospasillomásvendidos():
    ventanaMP= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMP.geometry("400x300")
    ventanaMP.title("Rep Productos Pasillo")

    codpasillo= Label(ventanaMP, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=230, y=10)
    
    botonAceptar = Button(ventanaMP, text="Aceptar", command=lambda: ProductosPorPasilloMasVendido(cajapasillo))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMP, text="Regresar", command=lambda:salirVentana(ventanaMP))
    botonRegresar.place(x=340, y=250)

def ventanaRepProductosPasillo():
    ventanaMP= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMP.geometry("400x300")
    ventanaMP.title("Rep Productos de un Pasillo")

    codpasillo= Label(ventanaMP, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=230, y=10)
    
    botonAceptar = Button(ventanaMP, text="Aceptar", command=lambda: ProductosDeUnPasillo(cajapasillo))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMP, text="Regresar", command=lambda:salirVentana(ventanaMP))
    botonRegresar.place(x=340, y=250)

def ventanaRepMarcasProductos():
    ventanaMP= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMP.geometry("400x300")
    ventanaMP.title("Rep Marcas de un Producto ")

    codprod= Label(ventanaMP, text="Ingrese el cod del producto")
    codprod.place(x=30, y=10)
    cajaprod = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaprod.place(x=230, y=10)
    
    botonAceptar = Button(ventanaMP, text="Aceptar", command=lambda: MarcasDeUnProducto(cajapasillo))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMP, text="Regresar", command=lambda:salirVentana(ventanaMP))
    botonRegresar.place(x=340, y=250)



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

def ventanaModificarProd():
    ventanaMPR= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMPR.geometry("450x450")
    ventanaMPR.title("Modificar Producto")

    codpasillo= Label(ventanaMPR, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMPR, text="Ingrese el cod del producto a modificar")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codnombre= Label(ventanaMPR, text="Ingrese el nuevo nombre")
    codnombre.place(x=30, y=90)
    cajanombre = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanombre.place(x=250, y=90)
    
    botonAceptar = Button(ventanaMPR, text="Aceptar", command=lambda: ModificarProducto(cajapasillo,cajaproducto,cajanombre))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMPR, text="Regresar", command=lambda:salirVentana(ventanaMPR))
    botonRegresar.place(x=340, y=250)

def ventanaModificarMarc():
    ventanaMM= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMM.geometry("450x450")
    ventanaMM.title("Modificar Marca")
    
    codpasillo= Label(ventanaMM, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMM, text="Ingrese el cod del producto a modificar")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codmarca= Label(ventanaMM, text="Ingrese el cod de marca")
    codmarca.place(x=30, y=90)
    cajamarca = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajamarca.place(x=250, y=90)

    nombre= Label(ventanaMM, text="Ingrese el nombre")
    nombre.place(x=30, y=130)
    cajanom = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=130)
    
    cantgon= Label(ventanaMM, text="Ingrese la cantidad en gondola")
    cantgon.place(x=30, y=170)
    cajagon = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajagon.place(x=250, y=170)

    Prec= Label(ventanaMM, text="Ingrese el precio")
    Prec.place(x=30, y=210)
    cajaprec = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaprec.place(x=250, y=210)
    
    botonAceptar = Button(ventanaMM, text="Aceptar", command=lambda: ModificarMarca(cajapasillo,cajaproducto,cajamarca,cajanom,cajagon,cajaprec))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMM, text="Regresar", command=lambda:salirVentana(ventanaMM))
    botonRegresar.place(x=340, y=250)

def ventanaModificarInve():
    ventanaMI= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMI.geometry("450x450")
    ventanaMI.title("Modificar inventario")
    
    codpasillo= Label(ventanaMI, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMI, text="Ingrese el cod del producto a modificar")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codmarca= Label(ventanaMI, text="Ingrese el cod de marca")
    codmarca.place(x=30, y=90)
    cajamarca = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajamarca.place(x=250, y=90)

    nombre= Label(ventanaMI, text="Ingrese el nombre")
    nombre.place(x=30, y=130)
    cajanom = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=130)
    
    cantin= Label(ventanaMI, text="Ingrese la cantidad en inventario")
    cantin.place(x=30, y=170)
    cajain = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajain.place(x=250, y=170)

    Codcana= Label(ventanaMI, text="Ingrese el cod de canasta")
    Codcana.place(x=30, y=210)
    cajacana = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacana.place(x=250, y=210)
    
    botonAceptar = Button(ventanaMI, text="Aceptar", command=lambda: ModificarInventario(cajapasillo,cajaproducto,cajamarca,cajanom,cajain,cajacana))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMI, text="Regresar", command=lambda:salirVentana(ventanaMI))
    botonRegresar.place(x=340, y=250)

def ventanaModificarCli():
    ventanaC= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaC.geometry("450x450")
    ventanaC.title("Modificar Cliente")

    Cedu= Label(ventanaC, text="Ingrese la cedula")
    Cedu.place(x=30, y=10)
    cajaced = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaced.place(x=250, y=10)

    Nomb= Label(ventanaC, text="Ingrese el nuevo nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)

    Tele= Label(ventanaC, text="Ingrese el nuevo telefono")
    Tele.place(x=30, y=90)
    cajatele = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajatele.place(x=250, y=90)

    Corr= Label(ventanaC, text="Ingrese el correo")
    Corr.place(x=30, y=130)
    cajacorr = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacorr.place(x=250, y=130)
    
    botonAceptar = Button(ventanaC, text="Aceptar", command=lambda: ModificarClientes(cajaced,cajanom,cajatele,cajacorr))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaC, text="Regresar", command=lambda:salirVentana(ventanaC))
    botonRegresar.place(x=340, y=250)

def ventanaModificarAdm():
    ventanaA= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaA.geometry("450x450")
    ventanaA.title("Modificar Administrador")

    Codi= Label(ventanaA, text="Ingrese el codigo")
    Codi.place(x=30, y=10)
    cajacod = Entry(ventanaA) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacod.place(x=250, y=10)

    Nomb= Label(ventanaA, text="Ingrese el nuevo nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaA) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)
    
    botonAceptar = Button(ventanaA, text="Aceptar", command=lambda: ModificarAdministradores(cajacod,cajanom))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaA, text="Regresar", command=lambda:salirVentana(ventanaA))
    botonRegresar.place(x=340, y=250)

def ventanaModificarVen():
    ventanaV= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaV.geometry("450x450")
    ventanaV.title("Modificar Vendedor")

    Codi= Label(ventanaV, text="Ingrese el codigo")
    Codi.place(x=30, y=10)
    cajacod = Entry(ventanaV) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacod.place(x=250, y=10)

    Nomb= Label(ventanaV, text="Ingrese el nuevo nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaV) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)
    
    botonAceptar = Button(ventanaV, text="Aceptar", command=lambda: ModificarVendedores(cajacod,cajanom))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaV, text="Regresar", command=lambda:salirVentana(ventanaV))
    botonRegresar.place(x=340, y=250)

#---------------------------Ventana de Insertar-------------------------------
def ventanaInsertP():
    ventanaMP= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMP.geometry("400x300")
    ventanaMP.title("Insertar Pasillo")

    codpasillo= Label(ventanaMP, text="Ingrese el cod del pasillo nuevo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=230, y=10)

    codnombre= Label(ventanaMP, text="Ingrese el nuevo nombre")
    codnombre.place(x=70, y=50)
    cajanombre = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanombre.place(x=230, y=50)
    
    botonAceptar = Button(ventanaMP, text="Aceptar", command=lambda:InsertarPasillo(cajapasillo,cajanombre))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMP, text="Regresar", command=lambda:salirVentana(ventanaMP))
    botonRegresar.place(x=340, y=250)

def ventanaInsertProd():
    ventanaMPR= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMPR.geometry("450x450")
    ventanaMPR.title("Insertar Producto")

    codpasillo= Label(ventanaMPR, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMPR, text="Ingrese el cod del producto nuevo")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codnombre= Label(ventanaMPR, text="Ingrese el nuevo nombre")
    codnombre.place(x=30, y=90)
    cajanombre = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanombre.place(x=250, y=90)
    
    botonAceptar = Button(ventanaMPR, text="Aceptar", command=lambda: InsertarProducto(cajapasillo,cajaproducto,cajanombre))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMPR, text="Regresar", command=lambda:salirVentana(ventanaMPR))
    botonRegresar.place(x=340, y=250)

def ventanaInsertMarc():
    ventanaMM= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMM.geometry("450x450")
    ventanaMM.title("Insertar Marca")
    
    codpasillo= Label(ventanaMM, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMM, text="Ingrese el cod del producto")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codmarca= Label(ventanaMM, text="Ingrese el cod de marca nuevo")
    codmarca.place(x=30, y=90)
    cajamarca = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajamarca.place(x=250, y=90)

    nombre= Label(ventanaMM, text="Ingrese el nuevo nombre")
    nombre.place(x=30, y=130)
    cajanom = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=130)
    
    cantgon= Label(ventanaMM, text="Ingrese la cantidad en gondola")
    cantgon.place(x=30, y=170)
    cajagon = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajagon.place(x=250, y=170)

    Prec= Label(ventanaMM, text="Ingrese el precio")
    Prec.place(x=30, y=210)
    cajaprec = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaprec.place(x=250, y=210)
    
    botonAceptar = Button(ventanaMM, text="Aceptar", command=lambda: InsertarMarca(cajapasillo,cajaproducto,cajamarca,cajanom,cajagon,cajaprec))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMM, text="Regresar", command=lambda:salirVentana(ventanaMM))
    botonRegresar.place(x=340, y=250)

def ventanaInsertInve():
    ventanaMI= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMI.geometry("450x450")
    ventanaMI.title("Insertar inventario")
    
    codpasillo= Label(ventanaMI, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMI, text="Ingrese el cod del producto")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codmarca= Label(ventanaMI, text="Ingrese el cod de marca")
    codmarca.place(x=30, y=90)
    cajamarca = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajamarca.place(x=250, y=90)

    nombre= Label(ventanaMI, text="Ingrese el nombre")
    nombre.place(x=30, y=130)
    cajanom = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=130)
    
    cantin= Label(ventanaMI, text="Ingrese la cantidad en inventario")
    cantin.place(x=30, y=170)
    cajain = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajain.place(x=250, y=170)

    Codcana= Label(ventanaMI, text="Ingrese el cod de canasta")
    Codcana.place(x=30, y=210)
    cajacana = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacana.place(x=250, y=210)
    
    botonAceptar = Button(ventanaMI, text="Aceptar", command=lambda: InsertarInventario(cajapasillo,cajaproducto,cajamarca,cajanom,cajain,cajacana))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMI, text="Regresar", command=lambda:salirVentana(ventanaMI))
    botonRegresar.place(x=340, y=250)

def ventanaInsertCli():
    ventanaC= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaC.geometry("450x450")
    ventanaC.title("Insertar Cliente")

    Cedu= Label(ventanaC, text="Ingrese la cedula")
    Cedu.place(x=30, y=10)
    cajaced = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaced.place(x=250, y=10)

    Nomb= Label(ventanaC, text="Ingrese el nuevo nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)

    Tele= Label(ventanaC, text="Ingrese el nuevo telefono")
    Tele.place(x=30, y=90)
    cajatele = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajatele.place(x=250, y=90)

    Corr= Label(ventanaC, text="Ingrese el correo")
    Corr.place(x=30, y=130)
    cajacorr = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacorr.place(x=250, y=130)
    
    botonAceptar = Button(ventanaC, text="Aceptar", command=lambda: InsertarClientes(cajaced,cajanom,cajatele,cajacorr))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaC, text="Regresar", command=lambda:salirVentana(ventanaC))
    botonRegresar.place(x=340, y=250)

def ventanaInsertAdm():
    ventanaA= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaA.geometry("450x450")
    ventanaA.title("Insertar Administrador")

    Codi= Label(ventanaA, text="Ingrese el codigo")
    Codi.place(x=30, y=10)
    cajacod = Entry(ventanaA) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacod.place(x=250, y=10)

    Nomb= Label(ventanaA, text="Ingrese el nuevo nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaA) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)
    
    botonAceptar = Button(ventanaA, text="Aceptar", command=lambda: InsertarAdministradores(cajacod,cajanom))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaA, text="Regresar", command=lambda:salirVentana(ventanaA))
    botonRegresar.place(x=340, y=250)

def ventanaInsertVen():
    ventanaV= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaV.geometry("450x450")
    ventanaV.title("Insertar Vendedor")

    Codi= Label(ventanaV, text="Ingrese el codigo")
    Codi.place(x=30, y=10)
    cajacod = Entry(ventanaV) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacod.place(x=250, y=10)

    Nomb= Label(ventanaV, text="Ingrese el nuevo nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaV) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)
    
    botonAceptar = Button(ventanaV, text="Aceptar", command=lambda: InsertarVendedores(cajacod,cajanom))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaV, text="Regresar", command=lambda:salirVentana(ventanaV))
    botonRegresar.place(x=340, y=250)
#---------------------------Ventana de Eliminar-------------------------------

def ventanaEliminP():
    ventanaMP= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMP.geometry("400x300")
    ventanaMP.title("Eliminar Pasillo")

    codpasillo= Label(ventanaMP, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=230, y=10)

    codnombre= Label(ventanaMP, text="Ingrese el nuevo")
    codnombre.place(x=70, y=50)
    cajanombre = Entry(ventanaMP) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanombre.place(x=230, y=50)
    
    botonAceptar = Button(ventanaMP, text="Aceptar", command=lambda:EliminarPasillo(cajapasillo,cajanombre))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMP, text="Regresar", command=lambda:salirVentana(ventanaMP))
    botonRegresar.place(x=340, y=250)

def ventanaEliminProd():
    ventanaMPR= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMPR.geometry("450x450")
    ventanaMPR.title("Eliminar Producto")

    codpasillo= Label(ventanaMPR, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMPR, text="Ingrese el cod del producto")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codnombre= Label(ventanaMPR, text="Ingrese el nuevo")
    codnombre.place(x=30, y=90)
    cajanombre = Entry(ventanaMPR) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanombre.place(x=250, y=90)
    
    botonAceptar = Button(ventanaMPR, text="Aceptar", command=lambda: EliminarProducto(cajapasillo,cajaproducto,cajanombre))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMPR, text="Regresar", command=lambda:salirVentana(ventanaMPR))
    botonRegresar.place(x=340, y=250)

def ventanaEliminMarc():
    ventanaMM= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMM.geometry("450x450")
    ventanaMM.title("Eliminar Marca")
    
    codpasillo= Label(ventanaMM, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMM, text="Ingrese el cod del producto")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codmarca= Label(ventanaMM, text="Ingrese el cod de marca ")
    codmarca.place(x=30, y=90)
    cajamarca = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajamarca.place(x=250, y=90)

    nombre= Label(ventanaMM, text="Ingrese el nombre")
    nombre.place(x=30, y=130)
    cajanom = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=130)
    
    cantgon= Label(ventanaMM, text="Ingrese la cantidad en gondola")
    cantgon.place(x=30, y=170)
    cajagon = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajagon.place(x=250, y=170)

    Prec= Label(ventanaMM, text="Ingrese el precio")
    Prec.place(x=30, y=210)
    cajaprec = Entry(ventanaMM) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaprec.place(x=250, y=210)
    
    botonAceptar = Button(ventanaMM, text="Aceptar", command=lambda: EliminarMarca(cajapasillo,cajaproducto,cajamarca,cajanom,cajagon,cajaprec))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMM, text="Regresar", command=lambda:salirVentana(ventanaMM))
    botonRegresar.place(x=340, y=250)

def ventanaEliminInve():
    ventanaMI= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaMI.geometry("450x450")
    ventanaMI.title("Insertar inventario")
    
    codpasillo= Label(ventanaMI, text="Ingrese el cod del pasillo")
    codpasillo.place(x=30, y=10)
    cajapasillo = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajapasillo.place(x=250, y=10)

    codproducto= Label(ventanaMI, text="Ingrese el cod del producto")
    codproducto.place(x=30, y=50)
    cajaproducto = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaproducto.place(x=250, y=50)

    codmarca= Label(ventanaMI, text="Ingrese el cod de marca")
    codmarca.place(x=30, y=90)
    cajamarca = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajamarca.place(x=250, y=90)

    nombre= Label(ventanaMI, text="Ingrese el nombre")
    nombre.place(x=30, y=130)
    cajanom = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=130)
    
    cantin= Label(ventanaMI, text="Ingrese la cantidad en inventario")
    cantin.place(x=30, y=170)
    cajain = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajain.place(x=250, y=170)

    Codcana= Label(ventanaMI, text="Ingrese el cod de canasta")
    Codcana.place(x=30, y=210)
    cajacana = Entry(ventanaMI) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacana.place(x=250, y=210)
    
    botonAceptar = Button(ventanaMI, text="Aceptar", command=lambda: EliminarInventario(cajapasillo,cajaproducto,cajamarca,cajanom,cajain,cajacana))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaMI, text="Regresar", command=lambda:salirVentana(ventanaMI))
    botonRegresar.place(x=340, y=250)

def ventanaEliminCli():
    ventanaC= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaC.geometry("450x450")
    ventanaC.title("Eliminar Cliente")

    Cedu= Label(ventanaC, text="Ingrese la cedula")
    Cedu.place(x=30, y=10)
    cajaced = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajaced.place(x=250, y=10)

    Nomb= Label(ventanaC, text="Ingrese el nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)

    Tele= Label(ventanaC, text="Ingrese el telefono")
    Tele.place(x=30, y=90)
    cajatele = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajatele.place(x=250, y=90)

    Corr= Label(ventanaC, text="Ingrese el correo")
    Corr.place(x=30, y=130)
    cajacorr = Entry(ventanaC) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacorr.place(x=250, y=130)
    
    botonAceptar = Button(ventanaC, text="Aceptar", command=lambda: EliminarClientes(cajaced,cajanom,cajatele,cajacorr))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaC, text="Regresar", command=lambda:salirVentana(ventanaC))
    botonRegresar.place(x=340, y=250)

def ventanaEliminAdm():
    ventanaA= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaA.geometry("450x450")
    ventanaA.title("Eliminar Administrador")

    Codi= Label(ventanaA, text="Ingrese el codigo")
    Codi.place(x=30, y=10)
    cajacod = Entry(ventanaA) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacod.place(x=250, y=10)

    Nomb= Label(ventanaA, text="Ingrese el nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaA) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)
    
    botonAceptar = Button(ventanaA, text="Aceptar", command=lambda: EliminarAdministradores(cajacod,cajanom))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaA, text="Regresar", command=lambda:salirVentana(ventanaA))
    botonRegresar.place(x=340, y=250)

def ventanaEliminVen():
    ventanaV= Toplevel() #Crea otra ventana aparte de la principal para verificar administrador
    ventanaV.geometry("450x450")
    ventanaV.title("Eliminar Vendedor")

    Codi= Label(ventanaV, text="Ingrese el codigo")
    Codi.place(x=30, y=10)
    cajacod = Entry(ventanaV) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajacod.place(x=250, y=10)

    Nomb= Label(ventanaV, text="Ingrese el nombre")
    Nomb.place(x=30, y=50)
    cajanom = Entry(ventanaV) #Caja de texto donde almacena/captura lo que el usuario ingresa
    cajanom.place(x=250, y=50)
    
    botonAceptar = Button(ventanaV, text="Aceptar", command=lambda: EliminarVendedores(cajacod,cajanom))
    botonAceptar.place(x=250, y=250)
    botonRegresar = Button(ventanaV, text="Regresar", command=lambda:salirVentana(ventanaV))
    botonRegresar.place(x=340, y=250)
#---------------------------Ventana de Mantenimiento de la base de datos-------------------------------



def ventanaInsert():
    ventanaI = Toplevel()
    ventanaI.geometry("340x340")
    ventanaI.title("Insertar")

    opcion1 = Button(ventanaI , text="Pasillo",command=lambda:ventanaInsertP())
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaI , text="Producto Nuevo", command = lambda:ventanaInsertProd())
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaI , text="Marca Nueva", command = lambda:ventanaInsertMarc())
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaI , text="Inventario", command = lambda:ventanaInsertInve())
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaI , text="Registrar Clientes", command = lambda:ventanaInsertCli())
    opcion5.place(x=20,y=170)

    opcion6 = Button(ventanaI , text="Registrar Administradores", command = lambda:ventanaInsertAdm())
    opcion6.place(x=20,y=210)

    opcion7 = Button(ventanaI , text="Registrar Vendedores", command = lambda:ventanaInsertVen())
    opcion7.place(x=20,y=250)

    Regresar = Button(ventanaI,text="Regresar", command = lambda:salirVentana(ventanaI))
    Regresar.place(x=20,y=290)

def ventanaEliminar():
    ventanaE = Toplevel()
    ventanaE.geometry("340x340")
    ventanaE.title("Eliminar")

    opcion1 = Button(ventanaE , text="Pasillo",command = lambda:ventanaEliminP())
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaE , text="Producto",command = lambda:ventanaEliminProd())
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaE , text="Marca",command = lambda:ventanaEliminMarc())
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaE , text="Inventario",command = lambda:ventanaEliminInve())
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaE , text="Clientes",command = lambda:ventanaEliminCli())
    opcion5.place(x=20,y=170)

    opcion6 = Button(ventanaE , text="Administradores",command = lambda:ventanaEliminAdm())
    opcion6.place(x=20,y=210)

    opcion7 = Button(ventanaE , text="Vendedores",command=lambda:ventanaEliminVen())
    opcion7.place(x=20,y=250)

    Regresar = Button(ventanaE,text="Regresar", command = lambda:salirVentana(ventanaE))
    Regresar.place(x=20,y=290)
    
def ventanaModificar():
    ventanaMod = Toplevel()
    ventanaMod.geometry("340x340")
    ventanaMod.title("Modificar")

    opcion1 = Button(ventanaMod , text="Pasillo", command = lambda:ventanaModificarP())
    opcion1.place(x=20,y=10)

    opcion2 = Button(ventanaMod , text="Producto", command = lambda:ventanaModificarProd())
    opcion2.place(x=20,y=50)

    opcion3 = Button(ventanaMod , text="Marca", command= lambda:ventanaModificarMarc())
    opcion3.place(x=20,y=90)

    opcion4 = Button(ventanaMod , text="Inventario",command= lambda:ventanaModificarInve())
    opcion4.place(x=20,y=130)
    
    opcion5 = Button(ventanaMod , text="Clientes",command= lambda:ventanaModificarCli())
    opcion5.place(x=20,y=170)

    opcion6 = Button(ventanaMod , text="Administradores",command= lambda:ventanaModificarAdm())
    opcion6.place(x=20,y=210)

    opcion7 = Button(ventanaMod , text="Vendedores",command= lambda:ventanaModificarVen())
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

    opcion3 = Button(ventanaRep , text="Productos por pasillo más vendidos", command = lambda:ventanaRepProductospasillomásvendidos())
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

    opcion9 = Button(ventanaRep , text="Marcas de un producto", command = lambda:ventanaRepMarcasProductos())
    opcion9.place(x=20,y=330)

    opcion10 = Button(ventanaRep , text="Factura de mayor monto", command = lambda:FacturaDeMayorMonto())
    opcion10.place(x=20,y=370)
    
    opcion11 = Button(ventanaRep , text="Productos de un pasillo", command = lambda:ventanaRepProductosPasillo())
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

    opcion2 = Button(ventanaAd , text="Facturar")
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

    opcion4 = Button(ventanaCr , text="Comprar")
    opcion4.place(x=20,y=130)

    Regresar = Button(ventanaCr,text="Regresar", command = lambda:salirVentana(ventanaCr))
    Regresar.place(x=20,y=170)

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
        CC=codigo1.get()
        if buscaEnLista(clientes,CC,0) != -1:
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




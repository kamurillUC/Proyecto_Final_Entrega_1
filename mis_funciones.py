import mis_clases, os, ast, hashlib

salt = b'KamurillUC'

#Funcion para limpiar consola segun OS
def limpiar_consola():   
    #Unix systems 
    if os.name == "posix":
        os.system("clear")
    #Windows
    elif os.name == "nt":
        os.system("cls")

#Funciones para obtener UI
def get_logo():
    logo = ""
    logo += mis_clases.consolaColor.AZUL
    logo += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"  
    logo += mis_clases.consolaColor.MAGENTA
    logo += "___________________________________________________________________________________________\n\n"    
    logo += mis_clases.consolaColor.CYAN
    logo += "████████╗██╗███████╗███╗   ██╗██████╗  █████╗     ███████╗██╗███╗   ███╗ ██████╗ ███╗   ██╗\n"
    logo += "╚══██╔══╝██║██╔════╝████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██║████╗ ████║██╔═══██╗████╗  ██║\n"
    logo += "   ██║   ██║█████╗  ██╔██╗ ██║██║  ██║███████║    ███████╗██║██╔████╔██║██║   ██║██╔██╗ ██║\n"
    logo += "   ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══██║    ╚════██║██║██║╚██╔╝██║██║   ██║██║╚██╗██║\n"
    logo += "   ██║   ██║███████╗██║ ╚████║██████╔╝██║  ██║    ███████║██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║\n"
    logo += "   ╚═╝   ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n"
    logo += mis_clases.consolaColor.MAGENTA
    logo += "___________________________________________________________________________________________\n" 
        
    logo += mis_clases.consolaColor.NORMAL  

    return logo


def get_gracias():
    gracias = ""
    gracias += mis_clases.consolaColor.AZUL
    gracias += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"  
    gracias += mis_clases.consolaColor.MAGENTA
    gracias += "___________________________________________________________________________________________\n\n"    
    gracias += mis_clases.consolaColor.CYAN
    gracias += "                    ██████╗ ██████╗  █████╗  ██████╗██╗ █████╗ ███████╗\n"
    gracias += "                   ██╔════╝ ██╔══██╗██╔══██╗██╔════╝██║██╔══██╗██╔════╝\n"
    gracias += "                   ██║  ███╗██████╔╝███████║██║     ██║███████║███████╗\n"
    gracias += "                   ██║   ██║██╔══██╗██╔══██║██║     ██║██╔══██║╚════██║\n"
    gracias += "                   ╚██████╔╝██║  ██║██║  ██║╚██████╗██║██║  ██║███████║\n"
    gracias += "                    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝\n"
    gracias += mis_clases.consolaColor.MAGENTA
    gracias += "___________________________________________________________________________________________\n" 
        
    gracias += mis_clases.consolaColor.NORMAL  

    return gracias


def get_portada():      
    portada = ""
    portada += mis_clases.consolaColor.AZUL   
    portada += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"        
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|                                        | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|             {mis_clases.consolaColor.NORMAL}Proyecto Final{mis_clases.consolaColor.AMARILLO}             | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|........................................| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|         {mis_clases.consolaColor.NORMAL}Kevin A. Murillo Rojas{mis_clases.consolaColor.AMARILLO}         | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    portada += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    portada += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    portada += mis_clases.consolaColor.MAGENTA
    portada += "___________________________________________________________________________________________\n" 
    portada += mis_clases.consolaColor.NORMAL  

    return portada


def get_login():   
    login = "" 
    login += mis_clases.consolaColor.AZUL   
    login += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"     
    login += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    login += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|                                        | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    login += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|            {mis_clases.consolaColor.NORMAL}Inicio de sesión{mis_clases.consolaColor.AMARILLO}            | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"        
    login += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    login += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    login += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    login += mis_clases.consolaColor.MAGENTA
    login += "___________________________________________________________________________________________\n" 
    login += mis_clases.consolaColor.NORMAL 
    return login


def cargar_archivo(opcion):
    path = os.getcwd()

    if opcion == 'usuarios':
        path += '\\datafiles\\users.txt'
            
    file = open(path, "r")
    content = file.read()
    file.close()

    return ast.literal_eval(content)


def encontrar_usuario(usuarios, nombre_usuario, password):
    
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)       
    
    for usuario in usuarios:
        if nombre_usuario == usuario['usuario']:
            if dk.hex() == usuario['password']:
                return usuario
            else:
                return usuario


def generar_hash(password):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000) 
    return dk.hex()


def get_departamento():   
    depa = ""
    depa += mis_clases.consolaColor.AZUL  
    depa += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"   
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|       Seleccione un departamento       | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|........................................| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 1. Damas                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"           
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 2. Caballeros                          | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 3. Niños                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 4. Salir                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    depa += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    depa += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    depa += mis_clases.consolaColor.MAGENTA
    depa += "___________________________________________________________________________________________\n" 
    depa += mis_clases.consolaColor.NORMAL 

    return depa


def generar_linea(departamento):
    if departamento.lower() == 'damas':
        return "..................Damas................."
    elif departamento.lower() == 'caballeros':
        return "...............Caballeros..............."
    elif departamento.lower() == 'kids':
        return "..................Niños................."


def get_menu(usuario_actual, departamento):
    menu = ""
    menu += mis_clases.consolaColor.AZUL  
    menu += f"< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"   
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO} _________________________________________  {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|   Menú de productos del departamento   | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|{generar_linea(departamento)}| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 1. Consultar                           | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    if usuario_actual['role'] == 'admin':        
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 2. Ingresar                            | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 3. Actualizar                          | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 4. Eliminar                            | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 5. Volver                              | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 6. Salir                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    elif usuario_actual['role'] == 'invitado':        
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 2. Volver                              | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
        menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[| 3. Salir                               | {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += f"< >< >< >< >< >< >< > {mis_clases.consolaColor.AMARILLO}[|________________________________________| {mis_clases.consolaColor.AZUL}< >< >< >< >< >< >< >< >\n"
    menu += "< >< >< >< >< >< >< >                                             < >< >< >< >< >< >< >< >\n"
    menu += "< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >\n"
    menu += mis_clases.consolaColor.MAGENTA
    menu += "___________________________________________________________________________________________\n" 
    menu += mis_clases.consolaColor.NORMAL 
    
    return menu


def get_cantidad_opciones(usuario_actual):
    if usuario_actual['role'] == 'admin':
        return 6
    elif usuario_actual['role'] == 'invitado':
        return 3
    else:
        return 0


def opcion_menu(cantidad_opciones):
    bandera = 0
    opcion = 0
    while bandera == 0:
        respuesta = input(f"{mis_clases.consolaColor.AMARILLO}Opción: {mis_clases.consolaColor.NORMAL}")
        es_numero = respuesta.isdigit()
        if es_numero == True:                    
            opcion = int(respuesta)
            if opcion > 0 and opcion <= cantidad_opciones:                
                break          
                            
        print(f"{mis_clases.consolaColor.ROJO}¡Por favor ingresar un número válido!{mis_clases.consolaColor.NORMAL}")   
               
    return opcion


def get_opciones_producto(usuario_actual, opcion):
    respuesta = ""
    if usuario_actual['role'] == 'admin':
        if opcion == 1:
            respuesta += "Consulta de productos"
        elif opcion == 2:
            respuesta += "Ingrese el producto"
        elif opcion == 3:
            respuesta += "Actualice el producto"
        elif opcion == 4:
            respuesta += "Elimine el producto"
    elif usuario_actual['role'] == 'invitado':
        if opcion == 1:
            respuesta += "Consulta de productos"

    return respuesta    


def menu_por_departamento(usuario_actual, departamento):
    bandera = 0
    while bandera == 0:        
        limpiar_consola()    
        print(get_menu(usuario_actual, departamento))
        opcion = opcion_menu(get_cantidad_opciones(usuario_actual))
                            
        if usuario_actual['role'] == 'admin':
            if opcion == 6: 
                bandera = 1
                return 1
            elif opcion == 5:
                break
            else:
                limpiar_consola() 
                print(get_opciones_producto(usuario_actual, opcion))
                respuesta = input(f"{mis_clases.consolaColor.AMARILLO}Presione cualquier tecla para continuar...{mis_clases.consolaColor.NORMAL}")
        elif usuario_actual['role'] == 'invitado':
            if opcion == 3: 
                bandera = 1
                return 1
            elif opcion == 2:
                break
            else:
                limpiar_consola() 
                print(get_opciones_producto(usuario_actual, opcion))
                respuesta = input(f"{mis_clases.consolaColor.AMARILLO}Presione cualquier tecla para continuar...{mis_clases.consolaColor.NORMAL}")

    return 0
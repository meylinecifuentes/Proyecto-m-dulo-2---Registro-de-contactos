# Proyecto Sistema de Gestión de Contactos - 

import sys   #para usar exit() terminar la ejecución del programa

def nombre_validar():
    """
    Validar que los nombres que se registran solo tengan letras y espacios.
    """
    while True:
        nom = input("Ingrese nombre:")
        if nom.replace(" ","").isalpha():
            return nom
        else:
            print("\n ERROR - El nombre solo debe contener letras.")

def cel_validar():
    """
    Validar que el número de celular solo contenga números y que tenga 8 dígitos
    """
    while True:
        cel = input("Ingrese número celular: ")
        if cel.replace(" ","").isdigit() and len(cel.replace(" ","")) == 8:
            return cel
        else:
            print("\n ERROR - Rectifique número celular")

def correo_validar():
    """
    Validar que el correo contenga el símbolo "@"  
    """
    while True:
        email = input("Ingrese su correo electrónico: ")
        if email.count("@"):
            return email
        else:
            print(" \n ERROR - Ingrese un correo válido.")
            
def buscar_contacto(termino, lista):
    """
    Busca el contacto o número celular coincida con lo que el usuario busca y
    retorna el índice del contacto en la lista base o un -1 si no existe 
    """
    for i in range(len(lista)):
        if (termino.lower() in lista[i]["nombre"].lower() or 
            termino in lista[i]["celular"]):
            return i
    return -1

#CLASES (POO)
class usuario:   #clase base
    """
    Estructura base de cualquiera de los usuarios en el sistema
    """
    def __init__(self, nombre, correo, celular, direccion):
        self._nombre = nombre
        self._celular = celular
        self._correo = correo
        self._direccion = direccion 
        
    def diccionario(self):
        """
        Convierte los atributos de cada contacto en un diccionario para almacenarlos
        """
        return {
            "nombre":self._nombre,
            "correo":self._correo,
            "celular":self._celular,
            "direccion":self._direccion
            }
    
class contacto(usuario):
    """
    Clase para contactos, hereda todo de la clase de usuario base 
    """
    def __init__(self, nombre, correo, celular, direccion):
        super().__init__(nombre, correo, celular, direccion)

class administrador(usuario):
    """
    Clase par el administrador, incluye la contraseña para realizar modificaciones a la agenda de contactos
    """
    def __init__(self, nombre, correo, celular, direccion, contraseña):
        super().__init__(nombre, correo, celular, direccion)
        self.contraseña = contraseña

adm_base = administrador("administrador", "administrador@gmail.com", 
                        "12345678", "empresa base", "administrador.124")      

opciones = ["1","2","3","4"]
lista_contactos = []    #almacenamiento principal de la agenda

#bucle principal para el interfaz del usuario (MENU)
while True:
    print("\n -- SISTEMA DE GESTIÓN DE CONTACTOS --\n 1.Registro de contacto \n 2.Modificar/Eliminar un contacto \n 3.Buscar datos de un contacto \n 4.Salir")
    opcion = input("\n Ingrese la acción que desea realizar (1-4): ")

#validar el valor de entrada al menu
    if not opcion.isdigit():
        print("\n ERROR - debe ingresar un número ")
        continue #Reiniciar el menú

    
#REGISTRO- REGISTRO- REGISTRO- REGISTRO
    if opcion in opciones:
        if opcion == "1":
            print("\n REGISTRAR")
            nombre = nombre_validar()
            celular = cel_validar()
            correo = correo_validar()
            direccion = input("Ingrese la dirección: ")
            
            #se crea el contacto y se almacena 
            reg_contacto = contacto(nombre, correo, celular, direccion)
            lista_contactos.append(reg_contacto.diccionario())

            print(f"{nombre} registrado como contacto")


#MODIFICAR- MODIFICAR- MODIFICAR- MODIFICAR
        elif opcion == "2":
            #verificar que existan datos, de lo contrario volver al menú
            if not lista_contactos:
                print("\n ERROR - No existen contactos registrados aún.")
                continue  #VOLVER AL MENÚ
            #SEGURIDAD DE INGRESO
            intentos = 4   #(3)
            aceptar = False 
            
            for i in range(1, intentos):
                ingreso = input("Ingrese contraseña de administrador: ")
                if ingreso == adm_base.contraseña:
                    print("Ingreso correcto")
                    aceptar = True
                    break  #SALIR DEL BUCLE
                else:
                    intentos_rest = intentos - (i +1)
                    if intentos_rest > 0:
                        print("ERROR - Contraseña incorrecta")
                        print(f"Te quedan {intentos_rest} intentos")
                    else:
                        print("ACCESO BLOQUEADO, el sistema se cerrará")
                        sys.exit()  #SALIR DEL PROGRAMA - 
            
            
            #INGRESO ACEPTADO 
            
            if aceptar: 
                print("\n MODIFICAR/ELIMINAR CONTACTO \n 1.Modificar contacto \n 2.Eliminar contacto")
                accion = input("\n Ingrese la opción que desea realizar (1-2): ")
                while accion not in ["1","2"]:
                    accion = input("ERROR - Ingrese la opción que desea realizar: ")
                
                #OPCION 1 = MODIFICAR
                if accion == "1":
                    print("\n -- MODIFICAR CONTACTO --")
                    
                    while True:                
                        nom_buscar = nombre_validar()
                        if nom_buscar == "salir":
                            break
                        
                        ind_registro = buscar_contacto(nom_buscar, lista_contactos)
                        #FUNCIÓN
                                
                        if ind_registro != -1:
                            print("Datos actuales")
                            print("nombre: ", lista_contactos[ind_registro]['nombre'])
                            print("correo: ", lista_contactos[ind_registro]['correo'])
                            print("celular: ", lista_contactos[ind_registro]['celular'])
                            print("direccion: ", lista_contactos[ind_registro]['direccion'])
                            
                            print("\n INGRESE LOS NUEVOS DATOS")
                            nom_nuevo = nombre_validar()
                            cor_nuevo = correo_validar()
                            cel_nuevo = cel_validar()
                            dir_nueva = input("Ingrese dirección: ")
                            
                            lista_contactos[ind_registro] ={
                                "nombre":nom_nuevo,
                                "correo":cor_nuevo,
                                "celular":cel_nuevo,
                                "direccion":dir_nueva
                                }
                            print(f"El contacto {nom_nuevo} ha sido modificado con éxito.")
                            break  #IMPOPRTANTE CIERRA EL BUCLE
                        else:
                            print("El contacto no existe en los registros")
                    
                #OPCION 2 = ELIMINAR
                elif accion == "2":
                    print("\n  -- ELIMINAR CONTACTO --")
                    
                    while True:
                        nom_buscar = input("Ingrese nombre del contacto a eliminar (o salir): ")
                        if nom_buscar.lower() == "salir":
                            break
                        
                        ind_registro = buscar_contacto(nom_buscar, lista_contactos)
                        
                        if ind_registro != -1:
                            print(f"Contacto {lista_contactos[ind_registro]['nombre']} encontrado")
                            
                            confirmar = input(f"¿Está seguro que desea eliminar a {lista_contactos[ind_registro]['nombre']}? (s/n): ")
                            
                            if confirmar.lower() == "s":
                                eliminado = lista_contactos.pop(ind_registro)
                                print(f"El contacto '{eliminado['nombre']}' ha sido eliminado.")
                                break # MENU PRINCIPAL
                            else:
                                print("Operación cancelada.")
                                break # MENU PRINCIPAL
                        else:
                            print("\n El contacto no existe en los registros")
            
            
#BUSCAR- BUSCAR- BUSCAR- BUSCAR- BUSCAR- BUSCAR
        elif opcion == "3":
            print("\n --- BUSCAR CONTACTO ---")
            if not lista_contactos:
                print("\n ERROR - No existen contactos registrados aún.")
                continue  #VOLVER AL MENÚ

            else:
                nom_buscar = input("Ingrese el nombre del contacto a buscar (o 'salir'): ")
                if nom_buscar.lower() != "salir":
                    
                    ind_registro = buscar_contacto(nom_buscar, lista_contactos)
                    
                    if ind_registro != -1:
                        print("\n CONTACTO ENCONTRADO:")
                        print(f"Nombre:    {lista_contactos[ind_registro]['nombre']}")
                        print(f"Correo:    {lista_contactos[ind_registro]['correo']}")
                        print(f"Celular:   {lista_contactos[ind_registro]['celular']}")
                        print(f"Dirección: {lista_contactos[ind_registro]['direccion']}\n")
                    else:
                        print("\n El contacto no existe en los registros")
            
        elif opcion == "4":
            print("  --  SESIÓN FINALIZADA  --  ")
            break
    else:
        print("ERROR - Debe seleccionar una opción del 1 al 4")
    

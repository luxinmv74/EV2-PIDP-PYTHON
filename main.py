print()

class Usuario:

    def __init__(self, nombre_completo, rut):

        self.nombre_completo = nombre_completo
        self.rut = rut

class Alumno(Usuario):

    def __init__(self, nombre_completo, rut, ramo_inscrito):
        super().__init__(nombre_completo, rut)
        self.ramo_inscrito = ramo_inscrito

    def guardar_alumno(self):

        archivo_alumno = "alumnos.csv"
        with open(archivo_alumno, "a") as f:
            f.write(f"Nombre: {self.nombre_completo}, RUT: {self.rut}, Ramos Inscritos: {self.ramo_inscrito}\n")

    @classmethod
    def mostrar_alumno(cls, archivo_alumno="alumnos.csv"):

        with open(archivo_alumno, "r") as f:
            #datos_alumno = f.read().split(",")
            try:
                for linea in f:
                    nombre_completo, rut, ramo_inscrito = linea.strip().split(",")
                    print(f"{nombre_completo}, {rut}, {ramo_inscrito}")
                #ramo_inscrito, nombre_completo, rut = datos_alumno
                #return cls(nombre_completo, rut, ramo_inscrito)
            except FileNotFoundError as file_not_found:
                print(f"No hay alumnos ingresados! Detalle: {file_not_found}")

class Ramo:

    def __init__(self, __id_ramo, __nombre_ramo):
        self.__id_ramo = __id_ramo
        self.__nombre_ramo = __nombre_ramo

    def guardar_ramo(self):

        archivo_ramo = "ramos.csv"
        with open(archivo_ramo, "a") as f:
            f.write(f"ID: {self.__id_ramo}, Nombre: {self.__nombre_ramo}\n")

    @classmethod
    def mostrar_ramo(cls, archivo_ramo="ramos.csv"):

        try:

            with open(archivo_ramo, "r") as f:
                #datos_ramo = f.read().split(",")
                #nombre_ramo, id_ramo = datos_ramo
                #return cls(nombre_ramo, int(id_ramo))
                for linea in f:
                    __id_ramo, __nombre_ramo = linea.strip().split(",")
                    print(f"{__id_ramo}, {__nombre_ramo}")
        except FileNotFoundError as file_not_found:
            print(f"No hay ramos ramos ingresados! Detalle: {file_not_found}")
    
    @classmethod
    def obtener_siguiente_id(cls, archivo_ramo="ramos.csv"):
        try:
            with open(archivo_ramo, "r") as f:
                ids = []
                for linea in f:
                    id_ramo, _ = linea.strip().split(",")
                    id_ramo = id_ramo.replace("ID: ", "").strip()
                    ids.append(int(id_ramo))
                if ids:
                    return max(ids) + 1
                else:
                    return 1
        except FileNotFoundError:
            return 1

gestionar_matriculas = True

while gestionar_matriculas == True:

    print("1) Mostrar ramos existentes")
    print("2) Mostrar alumnos existentes")
    print("3) Agregar Ramo")
    print("4) Agregar Alumno")
    print("5) Agregar Ramo a Alumno")
    print("6) Eliminar Ramo a Alumno")
    print("0) Salir")

    print()

    ingreso_opcion = input("Ingrese una opción para gestionar matrículas: ")

    print()

    if ingreso_opcion == "1": # MOSTRAR RAMOS
        
        try:
            #ramos = Ramo(id_ramo, nombre_ramo)
            #ramos.mostrar_ramo()
            Ramo.mostrar_ramo()
            print()
        except FileNotFoundError as file_not_found:
            print(f"Error al leer el archivo de los ramos ingresados! Detalle: {file_not_found}")
            print()
        except Exception as e:
            print(f"Error al leer archivo! Detalle: {e}")
            print()
    elif ingreso_opcion == "2": # MOSTRAR ALUMNOS
        try:
            #alumno = Alumno(nombre_alumno, rut_alumno, ramo_alumno)
            #alumno.mostrar_alumno()
            Alumno.mostrar_alumno()
            print()
        except FileNotFoundError as file_not_found:
            print("Error al leer alumno verifica que existe el archivo!")
            print()
        except Exception as e:
            print(f"Error al leer archivo! Detalle: {e}")
            print()
    elif ingreso_opcion == "3": # AGREGAR RAMO
        
        #v_id_ramo = input("Ingrese el ID del ramo: ")

        #while v_id_ramo == "":
            
        #    print("El ID del ramo está vacío por favor complétalo!")
        #    print()

        #    v_id_ramo = input("Ingrese el ID del ramo: ")
        
        v_nombre_ramo = input("Ingrese el nombre del ramo: ")

        while v_nombre_ramo == "":
            
            print("El Nombre del ramo está vacío por favor complétalo!")
            print()

            v_nombre_ramo = input("Ingrese el nombre del ramo: ")
        
        try:
            
            v_id_ramo = Ramo.obtener_siguiente_id()
            
            ramo = Ramo(v_id_ramo, v_nombre_ramo)
            ramo.guardar_ramo()
            print("Ramo Guardado! Para verlo selecciona la opción del menú: Mostrar ramos existentes")
            print()
        except FileNotFoundError as file_not_found:
            print("Error al guardar ramo, archivo NO encontrado!")
            print()
        except Exception as e:
            print(f"Error al guardar ramo! Detalle: {e}")
            print()
    elif ingreso_opcion == "4": # AGREGAR ALUMNO
        
        nombre_alumno = input("Ingrese el nombre del alumno: ")

        while nombre_alumno == "":

            print("El nombre está vacío por favor completalo!")

            nombre_alumno = input("Ingrese el nombre del alumno: ")

        rut_alumno = input("Ingrese el RUT del alumno: ")

        while rut_alumno == "":

            print("El RUT está vacío por favor completalo!")

            rut_alumno = input("Ingrese el RUT del alumno: ")

        ramo_alumno = input("Ingrese el ramo del alumno: ")

        while ramo_alumno == "":

            print("El ramo está vacío por favor completalo!")

            nombre_alumno = input("Ingrese el ramo del alumno: ")
        
        try:
            alumno = Alumno(nombre_alumno, rut_alumno, ramo_alumno)
            alumno.guardar_alumno()

            print("Alumno Guardado! Para verlo selecciona la opción del menú: Mostrar alumnos existentes")
            print()

        except FileNotFoundError as file_not_found:
            print("Error al guardar alumno, archivo NO encontrado!")
            print()
        except Exception as e:
            print(f"Error al guardar alumno! Detalle: {e}")
            print()
    elif ingreso_opcion == "5": # AGREGAR RAMO A ALUMNO....

        try:
            rut_alumno = input("Ingrese el RUT del alumno al que desea agregar el ramo: ").strip()

            while rut_alumno == "":
                
                print("Campo de RUT vacío por favor ingresa de nuevo un RUT!")
                print()

                rut_alumno = input("Ingrese el RUT del alumno al que desea agregar el ramo: ").strip()
            
            nuevo_ramo = input("Ingrese el nombre del ramo a agregar: ").strip()

            while nuevo_ramo == "":
                
                print("Campo de Nuevo Ramo vacío por favor ingresa de nuevo un Ramo nuevo!")
                print()

                nuevo_ramo = input("Ingrese el nombre del ramo a agregar: ").strip()
            
            # LEER ALUMNOS DEL ARCHIVO
            alumnos = []
            with open("alumnos.csv", "r") as f:
                for linea in f:
                    nombre, rut, ramos = linea.strip().split(",")
                    ramos = ramos.replace("Ramos Inscritos: ", "").strip()
                    alumnos.append([nombre, rut.replace(" RUT: ", "").strip(), ramos])
            
            # ACTUALIZAR RAMOS
            encontrado = False
            for i, (nombre, rut, ramos) in enumerate(alumnos):
                if rut == rut_alumno:
                    ramos_list = [r.strip() for r in ramos.split(";")] if ramos else []
                    if nuevo_ramo not in ramos_list:
                        ramos_list.append(nuevo_ramo)
                    alumnos[i][2] = "; ".join(ramos_list)
                    encontrado = True
                    break
                
            if not encontrado:
                print(f"No se encontró un alumno con RUT {rut_alumno}.\n")
            else:
                with open("alumnos.csv", "w") as f:
                    for nombre, rut, ramos in alumnos:
                        f.write(f"Nombre: {nombre}, RUT: {rut}, Ramos Inscritos: {ramos}\n")
                print("Ramo agregado correctamente al alumno!\n")

            print()
        except Exception as e:
            print(f"Error al agregar ramo al alumno! Detalle: {e}")
    elif ingreso_opcion == "6": # ELIMINAR RAMO A ALUMNO....

        try:
            rut_alumno = input("Ingrese el RUT del alumno al que desea eliminar un ramo: ").strip()
            while rut_alumno == "":
                print("Campo de RUT vacío, por favor ingresa un RUT válido!\n")
                rut_alumno = input("Ingrese el RUT del alumno al que desea eliminar un ramo: ").strip()
            
            ramo_eliminar = input("Ingrese el nombre del ramo a eliminar: ").strip()
            while ramo_eliminar == "":
                print("Campo de Ramo vacío, por favor ingresa un Ramo válido!\n")
                ramo_eliminar = input("Ingrese el nombre del ramo a eliminar: ").strip()
            
            # LEER ALUMNOS DEL ARCHIVO
            alumnos = []
            with open("alumnos.csv", "r") as f:
                for linea in f:
                    nombre, rut, ramos = linea.strip().split(",")
                    ramos = ramos.replace("Ramos Inscritos: ", "").strip()
                    alumnos.append([nombre, rut.replace(" RUT: ", "").strip(), ramos])
            
            # ACTUALIZAR RAMOS
            encontrado = False
            for i, (nombre, rut, ramos) in enumerate(alumnos):
                if rut == rut_alumno:
                    ramos_list = [r.strip() for r in ramos.split(";")] if ramos else []
                    if ramo_eliminar in ramos_list:
                        ramos_list.remove(ramo_eliminar)
                        alumnos[i][2] = "; ".join(ramos_list)
                        print(f"Ramo '{ramo_eliminar}' eliminado correctamente del alumno.\n")
                    else:
                        print(f"El alumno no tiene registrado el ramo '{ramo_eliminar}'.\n")
                    encontrado = True
                    break
            
            if not encontrado:
                print(f"No se encontró un alumno con RUT {rut_alumno}.\n")
            else:
                with open("alumnos.csv", "w") as f:
                    for nombre, rut, ramos in alumnos:
                        f.write(f"Nombre: {nombre}, RUT: {rut}, Ramos Inscritos: {ramos}\n")
            print()
        except Exception as e:
            print(f"Error al eliminar ramo al alumno! Detalle: {e}")
            
    elif ingreso_opcion == "0":
        gestionar_matriculas = False
        print("Saliendo de la Gestión de Matrículas")
        print()
    else:
        print("No hay más opciones en la Gestión de Matriculas!")
        print()
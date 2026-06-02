


medicamentos = {} #codigo: nombre/disponible/cantidad mínima/Unidad
instrumentos = {} #codigo: nombre/disponible/cantidad mínima/unidad/total
dispositivos = {} #codigo: nombre/disponible/cantidad mínima/unidad/total
medicamentos = {
    "MED001": ["Paracetamol", 10, 20, "tabletas"],
    "MED002": ["Ibuprofeno", 80, 10, "cápsulas"],
    "MED003": ["Amoxicilina", 40, 15, "frascos"]
}
# codigo : [nombre, disponible, cantidad mínima, unidad]


instrumentos = {
    "INS001": ["Bisturí", 9, 8, "unidades"],
    "INS002": ["Pinza quirúrgica", 16, 15, "unidades",20],
    "INS003": ["Termómetro digital", 4, 5, "unidades",40]
}
# codigo : [nombre, disponible, cantidad mínima, unidad]


dispositivos = {
    "DIS001": ["Monitor cardíaco", 5, 9, "equipos",30],
    "DIS002": ["Electrocardiógrafo", 7, 8, "equipos",12],
    "DIS003": ["Oxímetro", 12, 20, "unidades",24]
}
import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "inventario_medico.json")

# =========================
# CARGAR DATOS GUARDADOS
# =========================
if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

        medicamentos = datos.get("medicamentos", {})
        instrumentos = datos.get("instrumentos", {})
        dispositivos = datos.get("dispositivos", {})

else:
    # DATOS INICIALES SOLO SI NO EXISTE EL ARCHIVO
    medicamentos = {
        "MED001": ["Paracetamol", 10, 20, "tabletas"],
        "MED002": ["Ibuprofeno", 80, 10, "cápsulas"],
        "MED003": ["Amoxicilina", 40, 15, "frascos"]
    }

    instrumentos = {
        "INS001": ["Bisturí", 9, 8, "unidades"],
        "INS002": ["Pinza quirúrgica", 16, 15, "unidades", 20],
        "INS003": ["Termómetro digital", 4, 5, "unidades", 40]
    }

    dispositivos = {
        "DIS001": ["Monitor cardíaco", 5, 9, "equipos", 30],
        "DIS002": ["Electrocardiógrafo", 7, 8, "equipos", 12],
        "DIS003": ["Oxímetro", 12, 20, "unidades", 24]
    }

# =========================
# FUNCIÓN PARA GUARDAR
# =========================
def guardar_datos():
    datos = {
        "medicamentos": medicamentos,
        "instrumentos": instrumentos,
        "dispositivos": dispositivos
    }

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


# codigo : [nombre, disponible, cantidad mínima, unidad]
def agregar_med(codigo_med):
   medicamentos[codigo_med] = []
   medicamento = input("Ingrese el nombre del Medicamento: ")
   disponibilidad = int(input("Ingrese la cantidad disponible: "))
   unidad = input("Ingrese la Unidad de medida (EJ: Tabletas, Pastillas, Jarabes, etc): ")
   stock_min = int(input(f"Ingrese la cantidad mínima de disponibilidad de {unidad}: "))
   medicamentos[codigo_med] = [medicamento, disponibilidad, stock_min, unidad]
   print(f"Se agrego correctamente: {medicamentos[codigo_med]}")

def agregar_inst(codigo_inst):
   instrumentos[codigo_inst] = []
   instrumento = input("Ingrese el nombre del Instrumento: ")
   disponibilidad = int(input("Ingrese la cantidad disponible: "))
   unidad = input("Ingrese la Unidad de medida (EJ: Unidades, Piezas, etc): ")
   stock_min = int(input(f"Ingrese la cantidad mínima de disponibilidad de {unidad}: "))

   reutilizable = input("¿El instrumento es reutilizable?")
   if reutilizable.lower() == "si":
      total = disponibilidad
      instrumentos[codigo_inst] = [instrumento, disponibilidad, stock_min, unidad, total]
   if reutilizable.lower()== "no":
      instrumentos[codigo_inst] = [instrumento, disponibilidad, stock_min, unidad]
   print(f"Se agrego correctamente: {instrumentos[codigo_inst]}")

def agregar_disp(codigo_disp):
   dispositivos[codigo_disp] = []
   dispositivo = input("Ingrese el nombre del Dispositivo: ")
   disponibilidad = int(input("Ingrese la cantidad disponible: "))
   total = disponibilidad
   unidad = input("Ingrese la Unidad de medida (EJ: Unidades, Equipos, etc): ")
   stock_min = int(input(f"Ingrese la cantidad mínima de disponibilidad de {unidad}: "))
   dispositivos[codigo_disp] = [dispositivo, disponibilidad, stock_min, unidad, total]
   print(f"Se agrego correctamente: {dispositivos[codigo_disp]}")

def alerta_med(codigo):
   if medicamentos[codigo][1] < medicamentos[codigo][2]:
      print(f"🚨 ¡ALERTA!: El medicamento {medicamentos[codigo][0]} ({codigo}) tiene stock bajo.")
      print(f"   Actual: {medicamentos[codigo][1]} {medicamentos[codigo][3]} | Mínimo requerido: {medicamentos[codigo][2]} {medicamentos[codigo][3]}\n ")

def alerta_inst(codigo):
   if instrumentos[codigo][1] < instrumentos[codigo][2]:
      print(f"🚨 ¡ALERTA!: El instrumento {instrumentos[codigo][0]} ({codigo}) tiene stock bajo.")
      print(f"   Actual: {instrumentos[codigo][1]} {instrumentos[codigo][3]} | Mínimo requerido: {instrumentos[codigo][2]} {instrumentos[codigo][3]}\n ")

def alerta_disp(codigo):
   if dispositivos[codigo][1] < dispositivos[codigo][2]:
      print(f"🚨 ¡ALERTA!: El dispositivo / Equipo {dispositivos[codigo][0]} ({codigo}) tiene stock bajo.")
      print(f"   Actual: {dispositivos[codigo][1]} {dispositivos[codigo][3]} | Mínimo requerido: {dispositivos[codigo][2]} {dispositivos[codigo][3]} \n ")

def alerta_falta1(codigo):
   if len(instrumentos[codigo]) == 5:
      if instrumentos[codigo][1] < instrumentos[codigo][4]:
         print(f"☢️ ¡ALERTA!: Faltan Unidades del Instrumento {instrumentos[codigo][0]} ({codigo}): ")
         print(f"   Actual: {instrumentos[codigo][1]} {instrumentos[codigo][3]} | Total de Inventario: {instrumentos[codigo][4]} {instrumentos[codigo][3]} \n ")

def alerta_falta2(codigo):
   if dispositivos[codigo][1] < dispositivos[codigo][4]:
      print(f"☢️ ¡ALERTA!: Faltan Unidades del Dispositivo / Equipo {dispositivos[codigo][0]} ({codigo}): ")
      print(f"   Actual: {dispositivos[codigo][1]} {dispositivos[codigo][3]} | Total de Inventario: {dispositivos[codigo][4]} {dispositivos[codigo][3]} \n ")

def menu_ingresos():
   print("\n╔═════════════════════════════════════╗")
   print("║    ¿Ingreso nuevo o devolución?     ║")
   print("╠═════════════════════════════════════╣")
   print("║         1. DEVOLUCIÓN               ║")
   print("║         2. INGRESO NUEVO            ║")
   print("╚═════════════════════════════════════╝")


def menu_papelera():
   print("\n╔═════════════════════════════════════╗")
   print("║  ¿Que desea hacer en específico?    ║")
   print("╠═════════════════════════════════════╣")
   print("║  1. ELIMINAR REGISTRO COMPLETO      ║")
   print("║  2. DAR DE BAJA UNIDADES            ║")
   print("╚═════════════════════════════════════╝")



option = None
while option != 0:
   print("\n╔══════════════════════════════════════╗")
   print("║   INVENTARIO DE INSUMOS MÉDICOS      ║")
   print("╠══════════════════════════════════════╣")
   print("║  1. Ver inventario completo          ║")
   print("║  2. Agregar insumo nuevo             ║")
   print("║  3. Registrar entrada (reposición)   ║")
   print("║  4. Registrar salida (consumo)       ║")
   print("║  5. Ver alertas de stock bajo        ║")
   print("║  6. Eliminar insumo                  ║")
   print("║  0. Salir                            ║")
   print("╚══════════════════════════════════════╝")
   option = int(input("Ingrese la opción a realizar: "))
   match option:
      case 1:
         print("siendo la estructura: # codigo : [nombre, disponible, cantidad mínima, unidad, cantidad total]")
         print("--- MEDICAMENTOS ---")
         for c_m, v_m in medicamentos.items():
            print(f"{c_m}: {v_m}")

         print("--- INSTRUMENTOS ---")
         for c_i, v_i in instrumentos.items():
            print(f"{c_i}: {v_i}")

         print("--- DISPOSITIVOS ---")
         for c_d, v_d in dispositivos.items():
            print(f"{c_d}: {v_d}")

      case 2:
         op2 = None
         while op2 != 0:
            print("\n╔═════════════════════════╗")
            print("║   ¿Qué desea agregar?   ║")
            print("╠═════════════════════════╣")
            print("║    1. MEDICAMENTOS      ║")
            print("║    2. INSTRUMENTOS      ║")
            print("║    3. DISPOSITIVOS      ║")
            print("║    0. SALIR             ║")
            print("╚═════════════════════════╝")
            op2 = int(input("Ingrese el elemento que desea agregar: "))
            match op2:
               case 1:
                  while op2 != 0:
                     codigo_med = str(input("Ingrese el CÓDIGO del medicamento: ")).upper()
                     if codigo_med in medicamentos:
                        print(f"{codigo_med} ya esta registrado en el inventario de medicamentos disponibles ")
                        break
                     else:
                        agregar_med(codigo_med)
                        guardar_datos()
                        break
               case 2:
                  while op2 != 0:
                     codigo_inst = input("Ingrese el CÓDIGO del instrumento a agregar: ").upper()
                     if codigo_inst in instrumentos:
                        print(f"{codigo_inst} ya está registrado como instrumento disponible")
                        break
                     else:
                        agregar_inst(codigo_inst)
                        guardar_datos()
                        break

               case 3:
                  while op2 !=0:
                     codigo_disp = input("Ingrese el Dispositivo a agregar: ").upper()
                     if codigo_disp in dispositivos:
                        print(f"{codigo_disp} ya está registrado como dispositivo disponible")
                        break
                     else:
                        agregar_disp(codigo_disp)
                        guardar_datos()
                        break

      case 3:
         op3 = None
         while op3 !=0:
            print("\n╔════════════════════════════════════╗")
            print("║   ¿Qué se va reponer o devolver?   ║")
            print("╠════════════════════════════════════╣")
            print("║         1. MEDICAMENTOS            ║")
            print("║         2. INSTRUMENTOS            ║")
            print("║         3. DISPOSITIVOS            ║")
            print("║         0. SALIR                   ║")
            print("╚════════════════════════════════════╝")
            op3 = int(input("Ingrese la opción de lo que desea añadir: "))
            match op3:
               case 1:
                  codigo_med = input("Ingrese el codigo del Medicamento: ").upper()
                  if codigo_med in medicamentos:
                     cantidad = int(input(f"Ingrese la cantidad de reposición de {medicamentos[codigo_med][3]} que ingresa: "))
                     medicamentos[codigo_med][1] += cantidad
                     guardar_datos()

                  if not codigo_med in  medicamentos: 
                     print("El medicamento no está registrado, ¿Desea agregarlo?: ")
                     new_agree = input("¿si o no?: ")
                     if new_agree.lower() == "si":
                        agregar_med(codigo_med)
                        guardar_datos()
            
               case 2:
                  menu_ingresos()
                  deseo = int(input("Ingrese la opción de lo que desea añadir: "))                  
                  codigo_inst = input("Ingrese el codigo del Instrumento: ").upper()
                  if codigo_inst in instrumentos:
                     if deseo==1:
                        cantidad = int(input(f"Ingrese la cantidad de devolución de {instrumentos[codigo_inst][3]} que ingresa: "))
                        instrumentos[codigo_inst][1] += cantidad
                        guardar_datos()
                     if deseo==2:
                        cantidad = int(input(f"Ingrese la cantidad de {instrumentos[codigo_inst][3]} nuevos que ingresan al inventario: "))
                        instrumentos[codigo_inst][1] += cantidad
                        if len(instrumentos[codigo_inst]) == 5:
                           instrumentos[codigo_inst][4] += cantidad
                           
                        guardar_datos()
                  if not codigo_inst in  instrumentos: 
                     print("El instrumento no está registrado, ¿Desea agregarlo?: ")
                     new_agree = input("¿si o no?: ")
                     if new_agree.lower() == "si":
                        agregar_inst(codigo_inst)
                        guardar_datos()

               case 3:
                  menu_ingresos()
                  deseo = int(input("Ingrese la opción de lo que desea añadir: "))                  
                  codigo_disp = input("Ingrese el codigo del Dispositivo: ").upper()
                  if codigo_disp in dispositivos:
                     if deseo==1:
                        cantidad = int(input(f"Ingrese la cantidad de devolución de {dispositivos[codigo_disp][3]} que ingresa: "))
                        dispositivos[codigo_disp][1] += cantidad
                        guardar_datos()
                     if deseo==2:
                        cantidad = int(input(f"Ingrese la cantidad de {dispositivos[codigo_disp][3]} nuevos que ingresan al inventario: "))
                        dispositivos[codigo_disp][4] += cantidad
                        dispositivos[codigo_disp][1] += cantidad
                        guardar_datos()
                  if not codigo_disp in  dispositivos: 
                     print("El dispositivo no está registrado, ¿Desea agregarlo?: ")
                     new_agree = input("¿si o no?: ")
                     if new_agree.lower() == "si":
                        agregar_disp(codigo_disp)
                        guardar_datos()

      case 4:
         print("\n╔═════════════════════════╗")
         print("║   ¿Qué desea retirar?   ║")
         print("╠═════════════════════════╣")
         print("║    1. MEDICAMENTOS      ║")
         print("║    2. INSTRUMENTOS      ║")
         print("║    3. DISPOSITIVOS      ║")
         print("╚═════════════════════════╝")

         op4 = int(input("Qué desea retirar del inventario?: "))
         match op4:
            case 1:
               codigo_med = input("Ingrese el codigo del medicamento: ").upper()
               if codigo_med in medicamentos:
                  unidades_back = int(input(f"¿Cuantxs {medicamentos[codigo_med][3]} de {medicamentos[codigo_med][0]} se van a retirar?: "))
                  if unidades_back > medicamentos[codigo_med][1]:
                     print("No hay suficiente stock.")
                  else:
                     medicamentos[codigo_med][1] -= unidades_back
               print(f"Quedan {medicamentos[codigo_med][1]} {medicamentos[codigo_med][3]} de {medicamentos[codigo_med][0]} disponibles")
               alerta_med(codigo_med)
               guardar_datos()
            case 2:
               codigo_inst = input("Ingrese el codigo del Intrumento: ").upper()
               if codigo_inst in instrumentos:
                  unidades_back = int(input(f"¿Cuantxs {instrumentos[codigo_inst][3]} de {instrumentos[codigo_inst][0]} se van a retirar?: "))
                  if unidades_back > instrumentos[codigo_inst][1]:
                     print("No hay suficiente stock.")
                  else:
                     instrumentos[codigo_inst][1] -= unidades_back
                  print(f"Quedan {instrumentos[codigo_inst][1]} {instrumentos[codigo_inst][3]} de {instrumentos[codigo_inst][0]} disponibles")
                  alerta_inst(codigo_inst)
                  guardar_datos()
            case 3:
               codigo_disp = input("Ingrese el codigo del Dispositivo: ").upper()
               if codigo_disp in dispositivos:
                  unidades_back = int(input(f"¿Cuantxs {dispositivos[codigo_disp][3]} de {dispositivos[codigo_disp][0]} se van a retirar?: "))                 
                  if unidades_back > dispositivos[codigo_disp][1]:
                     print("No hay suficiente stock.")
                  else:
                     dispositivos[codigo_disp][1] -= unidades_back
                  print(f"Quedan {dispositivos[codigo_disp][1]} {dispositivos[codigo_disp][3]} de {dispositivos[codigo_disp][0]} disponibles")
                  alerta_disp(codigo_disp)
                  guardar_datos()

      case 5:
         print("⚠️ ALERTAS DE STOCK BAJO: ")
         print("MEDICAMENTOS: ")
         for c_med  in medicamentos.keys():
            alerta_med(c_med)
         print("INSTRUMENTOS: ")
         for c_inst in instrumentos.keys():
            alerta_inst(c_inst)
         print("DISPOSITIVOS: ")
         for c_disp in dispositivos.keys():
            alerta_disp(c_disp)

         print("⚠️ ALERTAS: FALTAN ITEMS ")
         print("INSTRUMENTOS: ")
         for c_falta1 in instrumentos.keys():
            alerta_falta1(c_falta1)
         print("DISPOSITIVOS: ")
         for c_falta2 in dispositivos.keys():
            alerta_falta2(c_falta2)
      
      case 6:
         op6 = None
         while op6 != 0:
            print("\n╔══════════════════════════════════════╗")
            print("║   ¿Qué desea eliminar o dar de baja  ║")
            print("╠══════════════════════════════════════╣")
            print("║           1. MEDICAMENTOS            ║")
            print("║           2. INSTRUMENTOS            ║")
            print("║           3. DISPOSITIVOS            ║")
            print("╚══════════════════════════════════════╝")
            op6 = int(input("Escriba la opción de la operación a realizar: "))
            match op6:
               case 1:
                  papelera = input("Ingrese el código del medicamento: ").upper()
                  if papelera in medicamentos:
                     del medicamentos[papelera]
                     print("Medicamento eliminado por completo.")
                     guardar_datos()
               case 2:
                  menu_papelera()
                  deseo = int(input("Escriba la opción a realizar: "))
                  papelera = input("Ingrese el código del instrumento: ").upper()
                  if papelera in instrumentos:
                     if deseo == 1:
                        del instrumentos[papelera]
                        print("Instrumento eliminado por completo.")
                        guardar_datos()
                     elif deseo == 2:
                        baja = int(input("¿Cuántas unidades se dañaron/perdieron definitivamente?: "))
                        instrumentos[papelera][1] -= baja 
                        if len(instrumentos[papelera]) == 5:
                           instrumentos[papelera][4] -= baja 
                           print(f"Baja registrada. Inventario actual: {instrumentos[papelera]}")
                           guardar_datos()
               case 3:
                  menu_papelera()
                  deseo = int(input("Escriba la opción a realizar: "))
                  papelera = input("Ingrese el código del Dispositivo: ").upper()
                  if papelera in dispositivos:
                     if deseo == 1:
                        del dispositivos[papelera]
                        print("Dispositivo eliminado por completo.")
                        guardar_datos()
                     elif deseo == 2:
                        baja = int(input("¿Cuántas unidades se dañaron/perdieron definitivamente?: "))
                        dispositivos[papelera][1] -= baja # Resta de disponible
                        dispositivos[papelera][4] -= baja # Resta de total
                        print(f"Baja registrada. Inventario actual: {dispositivos[papelera]}")
                        guardar_datos()
pacientes = [{"id": 1, "rut": "15432198K", "nombre": "Ana Gómez Pérez", "activo": True},
            {"id": 2, "rut": "128765432", "nombre": "Carlos Ruiz Morales", "activo": True},
            {"id": 3, "rut": "201234568", "nombre": "Lucía Fernández Silva",  "activo": False}
]

def limpiar_rut(rut):
    if rut is None:
        return ""
    return str(rut).replace(".", "").replace("-", "").replace(" ", "").strip().upper()

def buscar_pacientes_lista(lista_pacientes, rut_buscado):
    rut_limpio_busqueda = limpiar_rut(rut_buscado)

    encontrados = [
        pacientes for pacientes in lista_pacientes
        if limpiar_rut(pacientes["rut"]) == rut_limpio_busqueda
    ]
    return encontrados if encontrados else "paciente no encontado"

rut_ingresado = input("Ingrese el rut del paciente a buscar: ")
resultado = buscar_pacientes_lista(pacientes, rut_ingresado)

if isinstance(resultado, list):
    for paciente in resultado:
        print("\n --- Datos del Paciente ---")
        for clave, valor in paciente.items():
            print(f"{clave.capitalize()}: {valor}")
else:
    print(resultado)
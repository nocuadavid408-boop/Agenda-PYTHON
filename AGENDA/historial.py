# historial.py
ARCHIVO = 'historial_notas.txt'

def guardar_historial(notas):
    try:
        with open(ARCHIVO, 'w', encoding='utf-8') as f:
            f.write('=== HISTORIAL DE NOTAS ===\n')
            for nota in notas:
                linea = (f"ID:{nota['id']} | Tarea:{nota['tarea']} | "
                         f"Inicio:{nota['fecha_inicio']} | "
                         f"Final:{nota['fecha_final']} | "
                         f"Estado:{nota['estado']}\n")
                f.write(linea)
        print('Historial guardado.')
    except Exception as e:
        print(f'Error al guardar: {e}')

def ver_historial():
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('No hay historial guardado aún.')

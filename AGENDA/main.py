# main.py
import gestor_notas
import historial

def mostrar_menu():
    print('\n===== AGENDA DE NOTAS =====')
    print('1. Crear nota')
    print('2. Ver notas')
    print('3. Ver historial')
    print('4. Cambiar estado de nota')
    print('5. Guardar historial')
    print('0. Salir')
    print('===========================')

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input('Selección: '))
        except ValueError:
            print('Ingresa un número válido.')
            continue

        if opcion == 1:
            tarea = input('Tarea: ')
            inicio = input('Fecha inicio (AAAA-MM-DD): ')
            final = input('Fecha final (AAAA-MM-DD): ')
            nota = gestor_notas.crear_nota(tarea, inicio, final)
            print(f'Nota creada con ID {nota["id"]}.')

        elif opcion == 2:
            notas = gestor_notas.ver_notas()
            if not notas:
                print('No hay notas.')
            else:
                for n in notas:
                    print(f"[{n['id']}] {n['tarea']} | {n['fecha_inicio']} - {n['fecha_final']} | {n['estado']}")

        elif opcion == 3:
            historial.ver_historial()

        elif opcion == 4:
            try:
                id_n = int(input('ID de nota: '))
                nuevo = input('Nuevo estado (realizado/pendiente): ')
                if gestor_notas.cambiar_estado(id_n, nuevo):
                    print('Estado actualizado.')
                else:
                    print('Nota no encontrada.')
            except ValueError:
                print('ID inválido.')

        elif opcion == 5:
            historial.guardar_historial(gestor_notas.ver_notas())

        elif opcion == 0:
            historial.guardar_historial(gestor_notas.ver_notas())
            print('¡Hasta luego!')
            break

        else:
            print('Opción no válida.')

if __name__ == '__main__':
    main()

import sqlite3
from unittest import case

DB_NAME = "escuela.db"
class Docente:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS docentes (
            id_docente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            curso TEXT NOT NULL
            );
        """)
        conn.commit()
        return conn
    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO docentes (nombre, curso) VALUES (?, ?)",
                (self.nombre, self.curso)
            )
        print(f"Docente '{self.nombre}' guardado con éxito.")


    @staticmethod
    def listar():
        with Docente._conn() as conn:
            cur = conn.execute("SELECT * FROM docentes")
            filas = cur.fetchall()
            if not filas:
                print("No hay docentes registrados.")
                return
            print("\n--- LISTADO DE DOCENTES ---")
            for f in filas:
                print(f"ID: {f['id_docente']} | Nombre: {f['nombre']} | Curso: {f['curso']}")
    @staticmethod
    def modificar():
        ide = input("Ingrese ID del docente a modificar: ")
        with Docente._conn() as conn:
            cur = conn.execute("SELECT * FROM docentes WHERE id_docente = ?", (ide,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el docente.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            curso = input(f"Nuevo curso [{fila['curso']}]: ") or fila['curso']
            conn.execute("UPDATE docentes SET nombre=?, curso=? WHERE id_docente=?",
                         (nombre, curso, ide))
        print("Docente actualizado con éxito.")

    @staticmethod
    def eliminar():
        ide = input("Ingrese ID del docente a eliminar: ")
        with Docente._conn() as conn:
            cur = conn.execute("DELETE FROM docentes WHERE id_docente = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el docente.")
            else:
                print("Docente eliminado con éxito.")


class Estudiante:
    def __init__(self, nombre, carrera, promedio):
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                carrera TEXT NOT NULL,
                promedio REAL
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO estudiantes (nombre, carrera, promedio) VALUES (?, ?, ?)",
                (self.nombre, self.carrera, self.promedio)
            )
        print(f"Estudiante '{self.nombre}' guardado con éxito.")

    @staticmethod
    def listar():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes")
            filas = cur.fetchall()
            if not filas:
                print("No hay estudiantes registrados.")
                return
            print("\n--- LISTADO DE ESTUDIANTES ---")
            for f in filas:
                print(f"ID: {f['id_estudiante']} | Nombre: {f['nombre']} | Carrera: {f['carrera']} | Promedio: {f['promedio']}")

    @staticmethod
    def modificar():
        ide = input("Ingrese ID del estudiante a modificar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes WHERE id_estudiante = ?", (ide,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el estudiante.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            carrera = input(f"Nueva carrera [{fila['carrera']}]: ") or fila['carrera']
            promedio = input(f"Nuevo promedio [{fila['promedio']}]: ") or fila['promedio']
            conn.execute("UPDATE estudiantes SET nombre=?, carrera=?, promedio=? WHERE id_estudiante=?",
                         (nombre, carrera, promedio, ide))
        print("Estudiante actualizado con éxito.")

    @staticmethod
    def eliminar():
        ide = input("Ingrese ID del estudiante a eliminar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("DELETE FROM estudiantes WHERE id_estudiante = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el estudiante.")
            else:
                print("Estudiante eliminado con éxito.")

    @staticmethod
    def promedio_general():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT AVG(promedio) AS prom FROM estudiantes")
            prom = cur.fetchone()["prom"]
            if prom:
                print(f"\nPromedio general: {prom:.2f}")
            else:
                print("No hay datos para calcular el promedio.")

class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre
    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cursos (
                id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO cursos (nombre) VALUES (?)",
                (self.nombre, self.carrera, self.promedio)
            )
        print(f"Curso '{self.nombre}' guardado con éxito.")

    @staticmethod
    def listar():
        with Asignatura._conn() as conn:
            cur = conn.execute("SELECT * FROM cursos")
            filas = cur.fetchall()
            if not filas:
                print("No hay cursos registrados.")
                return
            print("\n--- LISTADO DE CURSOS ---")
            for f in filas:
                print(f"ID: {f['id_curso']} | Nombre: {f['nombre']} ")

    @staticmethod
    def modificar():
        ide = input("Ingrese ID del curso a modificar: ")
        with Asignatura._conn() as conn:
            cur = conn.execute("SELECT * FROM cursos WHERE id_curso = ?", (ide,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el curso.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            conn.execute("UPDATE curso SET nombre=? WHERE id_curso=?",
                         (nombre, ide))
        print("curso actualizado con éxito.")

    @staticmethod
    def eliminar():
        ide = input("Ingrese ID del curso a eliminar: ")
        with Asignatura._conn() as conn:
            cur = conn.execute("DELETE FROM cursos WHERE id_curso = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el curso.")
            else:
                print("curso eliminado con éxito.")

# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        try:
            print("\n===== MENÚ =====")
            print("1. Ingresar")
            print("2. Listar ")
            print("3. Modificar ")
            print("4. Eliminar ")
            print("5. Promedio de estudiantes")
            print("0. Salir")
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    print("1. Ingresar alumno")
                    print("2. Ingresar docente")
                    print("3. Ingresar curso")
                    print("0. Salir")
                    opcion2= int(input("Seleccione una opción: "))
                    match opcion2:
                        case 1:
                            nombre = input("Nombre: ")
                            carrera = input("Carrera: ")
                            promedio = float(input("Promedio: "))
                            e = Estudiante(nombre, carrera, promedio)
                            e.guardar()
                        case 2:
                            nombre = input("Nombre: ")
                            curso = input("Curso: ")
                            d = Docente(nombre, curso)
                            d.guardar()
                        case 3:
                            nombre = input("Nombre: ")
                            a = Asignatura(nombre)
                            a.guardar()
                        case 0:
                            print("Saliendo del submenú...")
                            break
                case 2:
                    print("1. Listado de alumnos")
                    print("2. Listado de docentes")
                    print("3. Listado de cursos")
                    print("0. Salir")
                    opcion2 = int(input("Seleccione una opción: "))
                    match opcion2:
                        case 1:
                            Estudiante.listar()
                        case 2:
                            Docente.listar()
                        case 3:
                            Asignatura.listar()
                        case 0:
                            print("Saliendo del submenú...")
                            break
                case 3:
                    print("1. Modificar alumno")
                    print("2. Ingresar alumno")
                    print("3. Modificar curso")
                    print("0. Salir")
                    opcion2 = int(input("Seleccione una opción: "))
                    match opcion2:
                        case 1:
                            Estudiante.modificar()
                        case 2:
                            Docente.modificar()
                        case 3:
                            Asignatura.modificar()
                        case 0:
                            print("Saliendo del submenú...")
                            break
                case 4:
                    print("1. Eliminar alumno")
                    print("2. Eliminar docente")
                    print("3. Eliminar curso")
                    print("0. Salir")
                    opcion2 = int(input("Seleccione una opción: "))
                    match opcion2:
                        case 1:
                            Estudiante.eliminar()
                        case 2:
                            Docente.eliminar()
                        case 3:
                            Asignatura.eliminar()
                        case 0:
                            print("Saliendo del submenú...")
                            break
                case 5:
                    Estudiante.promedio_general()
                    print("Presione ENTER para volver al menú")
                    input()
                    break
                case 0:
                    print("Saliendo del submenú...")
                    break
        except ValueError:
            print(ValueError)

if __name__ == "__main__":
    menu()
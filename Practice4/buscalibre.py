import sqlite3
from datetime import datetime


class Libreria:
    def __init__(self):
        self.conn = sqlite3.connect('libreria.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Libros
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ISBN TEXT UNIQUE,
            Titulo TEXT,
            Autor TEXT,
            Genero TEXT,
            Precio REAL,
            FechaUltimoPrecio TEXT,
            CantDisponible INTEGER)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Ventas
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LibroID INTEGER,
            Cantidad INTEGER,
            FechaVenta TEXT,
            FOREIGN KEY (LibroID) REFERENCES Libros(ID))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS historico_libros
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ISBN TEXT UNIQUE,
            Titulo TEXT,
            Autor TEXT,
            Genero TEXT,
            Precio REAL,
            FechaUltimoPrecio TEXT,
            CantDisponible INTEGER)''')

        self.conn.commit()

    def menu(self):
        while True:
            print("\n--- MENÚ ---")
            print("1. Cargar Libros")
            print("2. Modificar precio de un libro")
            print("3. Borrar un libro")
            print("4. Cargar disponibilidad")
            print("5. Listado de Libros")
            print("6. Ventas")
            print("7. Actualizar Precios")
            print("8. Mostrar registros anteriores a una fecha")
            print("0. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == '1':
                self.cargar_libros()
            elif opcion == '2':
                self.modificar_precio_libro()
            elif opcion == '3':
                self.borrar_libro()
            elif opcion == '4':
                self.cargar_disponibilidad()
            elif opcion == '5':
                self.listar_libros()
            elif opcion == '6':
                self.realizar_venta()
            elif opcion == '7':
                self.actualizar_precios()
            elif opcion == '8':
                fecha = input("Ingrese una fecha (YYYY-MM-DD): ")
                self.mostrar_registros_anteriores(fecha)
            elif opcion == '0':
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    def cargar_libros(self):
        isbn = input("Ingrese el ISBN: ")
        titulo = input("Ingrese el título: ")
        autor = input("Ingrese el autor: ")
        genero = input("Ingrese el género: ")
        precio = float(input("Ingrese el precio: "))
        fecha_ultimo_precio = datetime.now().strftime('%Y-%m-%d')
        cant_disponible = int(input("Ingrese la cantidad disponible: "))

        try:
            self.cursor.execute('''INSERT INTO Libros (ISBN, Titulo, Autor, Genero, Precio, FechaUltimoPrecio, CantDisponible)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                (isbn, titulo, autor, genero, precio, fecha_ultimo_precio, cant_disponible))
            self.conn.commit()
            print("Libro agregado correctamente.")
        except sqlite3.Error as e:
            print("Error al cargar el libro:", str(e))

    def modificar_precio_libro(self):
        libro_id = int(input("Ingrese el ID del libro a modificar: "))
        nuevo_precio = float(input("Ingrese el nuevo precio: "))

        try:
            self.cursor.execute("SELECT Titulo FROM Libros WHERE ID = ?", (libro_id,))
            libro = self.cursor.fetchone()
            if libro:
                confirmacion = input(f"¿Está seguro que desea modificar el precio del libro '{libro[0]}'? (s/n): ")
                if confirmacion.lower() == 's':
                    self.cursor.execute("UPDATE Libros SET Precio = ? WHERE ID = ?", (nuevo_precio, libro_id))
                    self.conn.commit()
                    print("Precio modificado correctamente.")
            else:
                print("No se encontró un libro con el ID proporcionado.")
        except sqlite3.Error as e:
            print("Error al modificar el precio del libro:", str(e))

    def borrar_libro(self):
        libro_id = int(input("Ingrese el ID del libro a borrar: "))

        try:
            self.cursor.execute("SELECT Titulo FROM Libros WHERE ID = ?", (libro_id,))
            libro = self.cursor.fetchone()
            if libro:
                confirmacion = input(f"¿Está seguro que desea borrar el libro '{libro[0]}'? (s/n): ")
                if confirmacion.lower() == 's':
                    self.cursor.execute("DELETE FROM Libros WHERE ID = ?", (libro_id,))
                    self.conn.commit()
                    print("Libro borrado correctamente.")
            else:
                print("No se encontró un libro con el ID proporcionado.")
        except sqlite3.Error as e:
            print("Error al borrar el libro:", str(e))

    def cargar_disponibilidad(self):
        libro_id = int(input("Ingrese el ID del libro a cargar disponibilidad: "))
        cantidad = int(input("Ingrese la cantidad a cargar: "))

        try:
            self.cursor.execute("SELECT Titulo FROM Libros WHERE ID = ?", (libro_id,))
            libro = self.cursor.fetchone()
            if libro:
                self.cursor.execute("UPDATE Libros SET CantDisponible = CantDisponible + ? WHERE ID = ?",
                                    (cantidad, libro_id))
                self.conn.commit()
                print("Disponibilidad cargada correctamente.")
            else:
                print("No se encontró un libro con el ID proporcionado.")
        except sqlite3.Error as e:
            print("Error al cargar la disponibilidad:", str(e))

    def listar_libros(self):
        try:
            self.cursor.execute("SELECT * FROM Libros ORDER BY ID")
            libros = self.cursor.fetchall()
            if libros:
                print("\n--- Listado de Libros ---")
                for libro in libros:
                    print(f"ID: {libro[0]}")
                    print(f"ISBN: {libro[1]}")
                    print(f"Título: {libro[2]}")
                    print(f"Autor: {libro[3]}")
                    print(f"Género: {libro[4]}")
                    print(f"Precio: {libro[5]}")
                    print(f"Fecha Último Precio: {libro[6]}")
                    print(f"Cantidad Disponible: {libro[7]}")
                    print("------------------------")
            else:
                print("No hay libros registrados.")
        except sqlite3.Error as e:
            print("Error al listar los libros:", str(e))

    def realizar_venta(self):
        libro_id = int(input("Ingrese el ID del libro vendido: "))
        cantidad = int(input("Ingrese la cantidad vendida: "))
        fecha_venta = datetime.now().strftime('%Y-%m-%d')

        try:
            self.cursor.execute("SELECT Titulo, CantDisponible FROM Libros WHERE ID = ?", (libro_id,))
            libro = self.cursor.fetchone()
            if libro:
                if cantidad <= libro[1]:
                    confirmacion = input(f"¿Está seguro que desea registrar la venta del libro '{libro[0]}'? (s/n): ")
                    if confirmacion.lower() == 's':
                        self.cursor.execute("INSERT INTO Ventas (LibroID, Cantidad, FechaVenta) VALUES (?, ?, ?)",
                                            (libro_id, cantidad, fecha_venta))
                        self.cursor.execute("UPDATE Libros SET CantDisponible = CantDisponible - ? WHERE ID = ?",
                                            (cantidad, libro_id))
                        self.conn.commit()
                        print("Venta registrada correctamente.")
                else:
                    print("La cantidad vendida supera la disponibilidad del libro.")
            else:
                print("No se encontró un libro con el ID proporcionado.")
        except sqlite3.Error as e:
            print("Error al realizar la venta:", str(e))

    def actualizar_precios(self):
        porcentaje = float(input("Ingrese el porcentaje de aumento de precios: "))

        try:
            # Insertar registros actuales en la tabla historico_libros
            self.cursor.execute("INSERT INTO historico_libros SELECT * FROM Libros")

            # Actualizar precios en la tabla Libros
            self.cursor.execute("UPDATE Libros SET Precio = Precio + (Precio * ? / 100)", (porcentaje,))
            self.cursor.execute("UPDATE Libros SET FechaUltimoPrecio = ?", (datetime.now().strftime('%Y-%m-%d'),))
            self.conn.commit()
            print("Precios actualizados correctamente.")
        except sqlite3.Error as e:
            print("Error al actualizar los precios:", str(e))

    def mostrar_registros_anteriores(self, fecha):
        print("************ Falta este metodo **********")

    def __del__(self):
        self.cursor.close()
        self.conn.close()


libreria = Libreria()
libreria.menu()

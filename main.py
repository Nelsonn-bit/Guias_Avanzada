"""
Módulo principal del proyecto Gestor de Estudiantes.
Genera un archivo CSV y una base de datos SQLite de ejemplo.
"""

import csv
import sqlite3
import os

def generar_csv(nombre_archivo: str = "estudiantes.csv") -> None:
    """Crea un archivo CSV con encabezados y tres registros de prueba."""
    datos = [
        ['nombre', 'correo', 'nota'],
        ['Ana', 'ana@mail.com', 4.5],
        ['Luis', 'luis@mail.com', 3.8],
        ['Sara', 'sara@mail.com', 4.2]
    ]

    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(datos)

    print(f"[OK] Archivo {nombre_archivo} generado correctamente.")


def crear_base(nombre_bd: str = "estudiantes.db") -> None:
    """Crea una base de datos SQLite con la tabla 'estudiantes'."""
    conn = sqlite3.connect(nombre_bd)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            nota REAL
        )
    """)

    conn.commit()
    conn.close()
    print(f"[OK] Base de datos {nombre_bd} creada y lista para uso.")


if __name__ == "__main__":
    generar_csv()
    crear_base()

"""
Módulo principal del proyecto Gestor de Estudiantes .
Este bloque genera un archivo CSV de ejemplo para pruebas .
"""

import csv


def generar_csv(nombre_archivo: str = "estudiantes.csv") ->None:
    """
    Crea un archivo CSV con encabezados y tres registros de prueba .
    : param nombre_archivo : nombre del archivo a generar .
    """
    datos = [
        ["nombre ", "correo ", "nota "],
        ["Ana ", "ana@mail . com ", 4.5],
        ["Luis ", "luis@mail . com ", 3.8],
        ["Sara ", "sara@mail . com ", 4.2],
    ]

    with open(nombre_archivo, "w", newline="", encoding="utf -8 ") as f:
        csv.writer(f).writerows(datos)
    print(f"[OK] Archivo { nombre_archivo } generado correctamente .")


if __name__ == " __main__ ":
    generar_csv()

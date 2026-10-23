
class GeneradorResumen:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def generar_resumen(self, nombre_archivo="resumen.txt"):
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("RESUMEN DEL CONJUNTO DE DATOS\n")
            archivo.write("=" * 40 + "\n\n")

            archivo.write(f"Cantidad de filas: {self.dataframe.shape[0]}\n")
            archivo.write(f"Cantidad de columnas: {self.dataframe.shape[1]}\n\n")

            archivo.write("Nombres de las columnas:\n")
            archivo.write(", ".join(self.dataframe.columns) + "\n\n")

            archivo.write("Tipos de datos:\n")
            archivo.write(self.dataframe.dtypes.to_string() + "\n\n")

            archivo.write("Primeras cinco filas:\n")
            archivo.write(self.dataframe.head().to_string() + "\n\n")

            archivo.write("Valores faltantes por columna:\n")
            archivo.write(self.dataframe.isnull().sum().to_string() + "\n")

        print(f"Resumen guardado en: {nombre_archivo}")

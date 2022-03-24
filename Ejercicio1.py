class Libro():

    def __init__(self, titulo, autor, editorial, fecha_lanz, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.autor = autor
        self.editorial = editorial
        self.fecha_lanz = fecha_lanz
        self.genero = genero
        self.precio = precio

    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_editorial(self):
        return self.editorial
    def get_fecha_lanz(self):
        return self.fecha_lanz
    def get_genero(self):
        return self.genero
    def get_precio(self):
        return self.precio
class Libro():

    def __init__(self, titulo, autor, editorial, fecha_lanz, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.autor = autor
        self.editorial = editorial
        self.fecha_lanz = fecha_lanz
        self.genero = genero
        self.precio = precio
    def __str__(self):
        return "{"+(str(self.titulo))+', ' +(str(self.autor))+', '+(str(self.editorial))+', '+(str(self.fecha_lanz))+', '+(str(self.genero))+' '+(str(self.precio))+"}"
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

    def set_titulo(self, title):
        self.titulo = title
    def set_autor(self, author):
        self.autor = author
    def set_editorial(self, editor):
        self.editorial=editor
    def set_fecha_lanz(self, date):
        self.fecha_lanz=date
    def set_genero(self, genre):
        self.genero = genre
    def set_precio(self,price):
        self.precio=price

libro1 = Libro('ESDLA','Tolkien','Minotauro','20-10-1995','Fantasía',20)
libro1.set_autor('J.Tolkien')


class Libreria:

    def __int__(self):
        self.codigo=''
        self.titulo=''
        self.autor=''
        self.precio=0
        self.pais=''
        self.categoria=''
        self.ano_publicacion=''

    def setCodigo(self,codigo):
        self.codigo = codigo
        if codigo.isalpha() and codigo.upper() == '-' and codigo.isdigit():
            return True
        else:
            print("Formato incorrecto")
            return False

    def setPrecio(self,precio):
        self.precio = precio
        if precio >= 10000 and precio <= 150000:
           return True
        else:
            print("El precio debe estar entre 10000 y 150000")
            return False

    def setCategoria(self,categoria):
        self.categoria = categoria
        if categoria.upper() == 'FANTASIA' or 'ACCION' or 'NOVELA' or 'FICCION':
            return True
        else:
            print("Categoria incorrecta")
            return False

    def setAnopublicacion(self,ano_pub):
        self.ano_publicacion = ano_pub
        if ano_pub >= 1780 and ano_pub <=2023:
            return True
        else:
             print("Año de publicacion incorrecto debe estar entre 1780 y 2023")
             return False





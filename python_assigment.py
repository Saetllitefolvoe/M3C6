#M3C6 Assigment 

# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.

class Usuario:

    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def __str__(self):
        return f"El nombre de usuario es {self.nombre_usuario} y su constraseña es {self.contraseña}."

usuario_uno = Usuario('Juncal89', 'password123')
usuario_dos = Usuario('Camilo97','asdf123' )

print(usuario_uno)
print(usuario_dos)

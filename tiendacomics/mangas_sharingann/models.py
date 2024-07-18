from django.db import models

# Modelo para los roles de usuario
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre_rol

# Modelo para los usuarios
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(max_length=50, unique=True)
    clave = models.CharField(max_length=128)  # Longitud mayor para mayor seguridad
    telefono = models.CharField(max_length=15)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

# Modelo para ventas
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    f_venta = models.DateField()
    f_despacho = models.DateField()
    f_entrega = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Cambiado a DecimalField
    carrito = models.BooleanField(verbose_name='¿El usuario tiene objetos en el carrito?')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

# Modelo para categorías
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nombre

# Modelo para cómics
class Comic(models.Model):
    cod_comic = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.IntegerField()
    foto = models.ImageField(upload_to="comics")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

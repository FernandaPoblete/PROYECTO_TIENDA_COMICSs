from django.contrib import admin
from .models import Usuario, Venta, Categoria, Comic, Rol

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Venta)
admin.site.register(Categoria)
admin.site.register(Comic)

# Register your models here.

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import ComicForm

# Create your views here.

def home(request):
    return render(request,"mangas_sharingann/pagina_principal.html")

def flash1(request):
    return render(request,"mangas_sharingann/flash1.html")

def linternaverde1(request):
    return render(request,"mangas_sharingann/linternaverde1.html")

def antman(request):
    return render(request,"mangas_sharingann/antman.html")

def aquaman(request):
    return render(request,"mangas_sharingann/Aquaman.html")

def attackontitan(request):
    return render(request,"mangas_sharingann/attackontitan.html")

def batman1(request):
    return render(request,"mangas_sharingann/batman1.html")

def batman2(request):
    return render(request,"mangas_sharingann/batman2.html")

def batman3(request):
    return render(request,"mangas_sharingann/batman3.html")

def blackwidow(request):
    return render(request,"mangas_sharingann/blackwidow.html")

def capitanamerica(request):
    return render(request,"mangas_sharingann/capitanamerica.html")

def carrito(request):
    return render(request,"mangas_sharingann/carrito.html")

def comicsDC(request):
    return render(request,"mangas_sharingann/comicsDC.html")

def comicsMarvel(request):
    return render(request,"mangas_sharingann/comicsMarvel.html")

def demonslayer(request):
    return render(request,"mangas_sharingann/demonslayer.html")

def dragonball(request):
    return render(request,"mangas_sharingann/dragonball.html")

def hulk(request):
    return render(request,"mangas_sharingann/hulk.html")

def hunterxhunter(request):
    return render(request,"mangas_sharingann/hunterxhunter.html")

def ironman(request):
    return render(request,"mangas_sharingann/ironman.html")

def jujutsukaisen(request):
    return render(request,"mangas_sharingann/jujutsukaisen.html")

def ligadelajusticia(request):
    return render(request,"mangas_sharingann/ligadelajusticia.html")

def login(request):
    return render(request,"mangas_sharingann/login.html")

def Mangas(request):
    return render(request,"mangas_sharingann/Mangas.html")

def myheroacademia(request):
    return render(request,"mangas_sharingann/myheroacademia.html")

def naruto(request):
    return render(request,"mangas_sharingann/naruto.html")
 
def pokeapi(request):
    return render(request,"mangas_sharingann/pokeapi.html")

def registro(request):
    return render(request,"mangas_sharingann/registro.html")

def secretwars(request):
    return render(request,"mangas_sharingann/secretwars.html")

def spiderman1(request):
    return render(request,"mangas_sharingann/spiderman1.html")

def supergirl(request):
    return render(request,"mangas_sharingann/supergirl.html")

def superman(request):
    return render(request,"mangas_sharingann/superman.html")

def thor(request):
    return render(request,"mangas_sharingann/thor.html")

def titans(request):
    return render(request,"mangas_sharingann/titans.html")

def tokyorevengers(request):
    return render(request,"mangas_sharingann/tokyorevengers.html")

def comic_form(request):
    return render(request,"mangas_sharingann/comic_form.html")

def comic_list(request):
    return render(request,"mangas_sharingann/comic_list.html")

def comic_list(request):
    comics = Comic.objects.all()
    return render(request, 'mangas_sharingann/comic_list.html', {'comics': comics})

def comic_view(request, cod_comic):
    comic = get_object_or_404(Comic, cod_comic=cod_comic)

    if request.method == 'POST':
        form = ComicForm(request.POST, request.FILES, instance=comic)
        if form.is_valid():
            form.save()
            return redirect('comic_list')
    else:
        form = ComicForm(instance=comic)

    return render(request, 'tu_app/comic_form.html', {'form': form, 'comic': comic})





def comic_list(request):
    comics = Comic.objects.all()
    return render(request, 'mangas_sharingann/comic_list.html', {'comics': comics})


def comic_list(request):
    comics = Comic.objects.all()
    return render(request, 'mangas_sharingann/comic_list.html', {'comics': comics})

def delete_comic(request, cod_comic):
    comic = get_object_or_404(Comic, cod_comic=cod_comic)
    if request.method == 'POST':
        comic.delete()
        return redirect('comic_list')
    return render(request, 'tu_app/comic_confirm_delete.html', {'comic': comic})

#*************************************************************************************



def inicio_sesion_verificar(request):
    if request.method == 'POST':
        correo = request.POST.get('username')
        contraseña = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            messages.error(request, 'El correo electrónico o la contraseña son incorrectos.')
            return render(request, 'ruta_a_tu_plantilla/login.html')

        if usuario.clave == contraseña:
            # Autenticación exitosa, procedemos a loguear al usuario
            user = authenticate(request, username=correo, password=contraseña)
            if user is not None:
                login(request, user)
                return redirect('pagina_principal')
            else:
                messages.error(request, 'El correo electrónico o la contraseña son incorrectos.')
                return render(request, 'ruta_a_tu_plantilla/login.html')
        else:
            messages.error(request, 'El correo electrónico o la contraseña son incorrectos.')
            return render(request, 'ruta_a_tu_plantilla/login.html')

    return render(request, 'ruta_a_tu_plantilla/login.html')



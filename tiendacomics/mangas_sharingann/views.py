from django.shortcuts import render

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


from django.shortcuts import render
from .models import Comic

def lista_comics(request):
    comics = Comic.objects.all()
    return render(request, 'tienda/lista_comics.html', {'comics': comics})
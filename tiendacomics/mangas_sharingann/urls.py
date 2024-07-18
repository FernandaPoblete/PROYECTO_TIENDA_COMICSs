
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import comic_list
from .views import comic_list, comic_view, delete_comic


urlpatterns = [
    
    path('', views.home, name="pagina_principal"),
    path('flash1', views.flash1, name="flash1"),
    path('linternaverde1', views.linternaverde1, name="linternaverde1"),
    path('antman', views.antman, name="antman"),
    path('aquaman', views.aquaman, name="aquaman"),
    path('attackontitan', views.attackontitan, name="attackontitan"),
    path('batman1', views.batman1, name="batman1"),
    path('batman2', views.batman2, name="batman2"),
    path('batman3', views.batman3, name="batman3"),
    path('blackwidow', views.blackwidow, name="blackwidow"),
    path('capitanamerica', views.capitanamerica, name="capitanamerica"),
    path('carrito', views.carrito, name="carrito"),
    path('comicsDC', views.comicsDC, name="comicsDC"),
    path('comicsMarvel', views.comicsMarvel, name="comicsMarvel"),
    path('demonslayer', views.demonslayer, name="demonslayer"),
    path('dragonball', views.dragonball, name="dragonball"),
    path('hulk', views.hulk, name="hulk"),
    path('hunterxhunter', views.hunterxhunter, name="hunterxhunter"),
    path('ironman', views.ironman, name="ironman"),
    path('jujutsukaisen', views.jujutsukaisen, name="jujutsukaisen"),
    path('ligadelajusticia', views.ligadelajusticia, name="ligadelajusticia"),
    path('login', views.login, name="login"),
    path('Mangas', views.Mangas, name="Mangas"),
    path('myheroacademia', views.myheroacademia, name="myheroacademia"),
    path('naruto', views.naruto, name="naruto"),
    path('pokeapi', views.pokeapi, name="pokeapi"),
    path('registro', views.registro, name="registro"),
    path('secretwars', views.secretwars, name="secretwars"),
    path('spiderman1', views.spiderman1, name="spiderman1"),
    path('supergirl', views.supergirl, name="supergirl"),
    path('superman', views.superman, name="superman"),
    path('thor', views.thor, name="thor"),
    path('titans', views.titans, name="titans"),
    path('tokyorevengers', views.tokyorevengers, name="tokyorevengers"),
    path('inicio_sesion_verificar/', views.inicio_sesion_verificar, name="inicio_sesion_verificar"),
    path('comic_list', views.comic_list, name='comic_list'),
    path('comics/', comic_list, name='comic_list'),

    path('comics/<int:cod_comic>/', comic_view, name='comic_view'),
    path('comics/<int:cod_comic>/delete/', delete_comic, name='delete_comic'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
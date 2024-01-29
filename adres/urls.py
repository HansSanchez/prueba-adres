"""
URL configuration for adres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud_adres.views import list, store, show, update, delete, disable, enable

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # La ruta 'leer' en donde listamos todos los registros o adquisiciones de la Base de Datos
    path('adquisiciones/', list.as_view(template_name = "adquisiciones/index.html"), name='leer'),

    # La ruta 'store' en donde mostraremos un formulario para store una nueva adquisión o registro  
    path('adquisiciones/store', store.as_view(template_name = "adquisiciones/store.html"), name='store'),
    
    # La ruta 'show' en donde mostraremos una página con los show de una adquisión o registro 
    path('adquisiciones/show/<int:pk>', show.as_view(template_name = "adquisiciones/show.html"), name='show'),
 
    # La ruta 'update' en donde mostraremos un formulario para update una adquisión o registro de la Base de Datos 
    path('adquisiciones/update/<int:pk>', update.as_view(template_name = "adquisiciones/update.html"), name='update'), 
 
    # La ruta 'delete' que usaremos para delete una adquisión o registro de la Base de Datos 
    path('adquisiciones/delete/<int:pk>', delete.as_view(), name='delete'),    
    
    # La ruta 'disable' que usaremos para deshabilitar una adquisión o registro de la Base de Datos 
    path('adquisiciones/disable/<int:pk>', disable.as_view(), name='disable'),  
    
    # La ruta 'enable' que usaremos para habilitar una adquisión o registro de la Base de Datos 
    path('adquisiciones/enable/<int:pk>', enable.as_view(), name='enable'),  
]

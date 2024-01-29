from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Acquisitions' para poder usarlo en nuestras Vistas CRUD
from .models import Acquisition
from history.models import History

import logging
logger = logging.getLogger(__name__)
 
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms
from django.utils import timezone
from django.db.models import Q

from django.forms.models import model_to_dict
import json

class list(ListView):
    model = Acquisition

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search', '')
        if search_term:
            queryset = queryset.filter(
                Q(budget__icontains=search_term) |
                Q(administrative_unit__icontains=search_term) |
                Q(type_of_goods_or_services__icontains=search_term) |
                Q(quantity__icontains=search_term) |
                Q(unit_value__icontains=search_term) |
                Q(total_value__icontains=search_term) |
                Q(acquisition_date__icontains=search_term) |
                Q(supplier__icontains=search_term) |
                Q(documentation__icontains=search_term)
            )
        return queryset
class store(SuccessMessageMixin, CreateView): 
    model = Acquisition # Llamamos a la clase 'Acquisition' que se encuentra en nuestro archivo 'models.py'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'acquisition' de nuestra Base de Datos 
    success_message = 'Adquisición registrada con éxito !' # Mostramos este Mensaje luego de registrar una adquisición
    
    def form_invalid(self, form):
        print(form)
        logger.debug("Form invalid: %s", form.errors)
        return super().form_invalid(form)

    # Redireccionamos a la página principal luego de crear un registro o adquisición
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class show(DetailView): 
    model = Acquisition # Llamamos a la clase 'Acquisition'
    
class update(SuccessMessageMixin, UpdateView): 
    model = Acquisition  # Llamamos a la clase 'Acquisition' 
    
    # Especificamos los campos que queremos actualizar
    fields = [
        "budget",
        "administrative_unit",
        "type_of_goods_or_services",
        "quantity",
        "unit_value",
        "total_value",
        "acquisition_date",
        "supplier",
        "documentation"
    ]
    
    success_message = 'Adquisición actualizada con éxito !'  # Mensaje de éxito

    def form_invalid(self, form):
        print(form)
        logger.debug("Form invalid: %s", form.errors)
        return super().form_invalid(form)
    
    def form_valid(self, form):
        # Estado actual antes de la actualización
        original_acquisition = Acquisition.objects.get(id=self.object.id)
        original_acquisition_str = str(model_to_dict(original_acquisition))

        # Registro en History antes de la actualización
        History.objects.create(
            action="Actualización",
            module="Acquisition",
            description=f"Estado anterior: {original_acquisition_str}",
            created_at=timezone.now()
        )

        # Guardar la adquisición actualizada
        response = super().form_valid(form)

        # Estado después de la actualización
        updated_acquisition_str = str(model_to_dict(self.object))

        # Registro en History después de la actualización
        History.objects.create(
            action="Actualización",
            module="Acquisition",
            description=f"Estado actualizado: {updated_acquisition_str}",
            created_at=timezone.now()
        )
        
        return response

    # Redireccionamos a la página principal luego de actualizar un registro o adquisición
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'

 
class delete(SuccessMessageMixin, DeleteView): 
    model = Acquisition 
    form = Acquisition
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o adquisición
    def get_success_url(self): 
        success_message = 'Adquisición eliminada con éxito !' # Mostramos este Mensaje luego de Editar un Adquisición 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

 
class disable(SuccessMessageMixin, UpdateView):
    model = Acquisition
    form = Acquisition # Asegúrate de que este sea tu formulario de modelo correcto
    fields = ['disabled_at'] 

    def form_valid(self, form):
        # Aquí puedes definir el nuevo valor para el campo específico
        form.instance.disabled_at = timezone.now()

        # Luego, guardas el objeto modificado
        form.save()

        # Mensaje de éxito
        success_message = 'Registro deshabilitado con éxito!' 
        messages.success(self.request, success_message)

        return super().form_valid(form)

    def get_success_url(self):
        # Redireccionamos a la vista principal 'leer'
        return reverse('leer')
    
class enable(SuccessMessageMixin, UpdateView):
    model = Acquisition
    form = Acquisition # Asegúrate de que este sea tu formulario de modelo correcto
    fields = ['disabled_at'] 

    def form_valid(self, form):
        # Aquí puedes definir el nuevo valor para el campo específico
        form.instance.disabled_at = None

        # Luego, guardas el objeto modificado
        form.save()

        # Mensaje de éxito
        success_message = 'Registro habilitado con éxito!' 
        messages.success(self.request, success_message)

        return super().form_valid(form)

    def get_success_url(self):
        # Redireccionamos a la vista principal 'leer'
        return reverse('leer')